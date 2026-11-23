"""Thin LeetCode client: public profile data, plus richer data when a session cookie is set."""
from __future__ import annotations

import os
import time

import requests

BASE = "https://leetcode.com"
UA = "Mozilla/5.0 (X11; Linux x86_64) interview-prep-dashboard"


class AuthExpired(Exception):
    """Cookies rejected: LeetCode says we're not signed in."""


class LeetCode:
    def __init__(self, username: str, session: str | None = None, csrf: str | None = None):
        self.username = username
        self.authed = bool(session and csrf)
        self.http = requests.Session()
        self.http.headers.update({"User-Agent": UA, "Referer": f"{BASE}/", "Origin": BASE})
        if self.authed:
            self.http.cookies.set("LEETCODE_SESSION", session, domain=".leetcode.com")
            self.http.cookies.set("csrftoken", csrf, domain=".leetcode.com")
            self.http.headers["x-csrftoken"] = csrf

    @classmethod
    def from_env(cls) -> "LeetCode":
        username = os.environ.get("LEETCODE_USERNAME", "").strip()
        if not username:
            raise SystemExit("LEETCODE_USERNAME is not set (add it as a repository variable).")
        return cls(username, os.environ.get("LEETCODE_SESSION") or None, os.environ.get("LEETCODE_CSRF") or None)

    # ---- transport -------------------------------------------------------
    def gql(self, query: str, variables: dict | None = None) -> dict:
        for attempt in range(4):
            r = self.http.post(f"{BASE}/graphql/", json={"query": query, "variables": variables or {}}, timeout=30)
            if r.status_code == 429 or r.status_code >= 500:
                time.sleep(2 ** attempt * 2)
                continue
            r.raise_for_status()
            body = r.json()
            if body.get("errors") and not body.get("data"):
                raise RuntimeError(f"LeetCode GraphQL error: {body['errors']}")
            return body.get("data") or {}
        raise RuntimeError("LeetCode kept rate-limiting; try again later.")

    # ---- public ----------------------------------------------------------
    def recent_public(self, limit: int = 20) -> list[dict]:
        """Recent submissions (all verdicts) from the public profile. No code, ~20 most recent only."""
        q = """query r($username: String!, $limit: Int) {
          recentSubmissionList(username: $username, limit: $limit) {
            title titleSlug timestamp statusDisplay lang
          }
        }"""
        rows = self.gql(q, {"username": self.username, "limit": limit}).get("recentSubmissionList") or []
        return [
            {
                "id": None,
                "slug": r["titleSlug"],
                "title": r["title"],
                "timestamp": int(r["timestamp"]),
                "status": r["statusDisplay"],
                "lang": r["lang"],
            }
            for r in rows
        ]

    def solved_counts(self) -> dict:
        """LeetCode's own solved-problem counts, e.g. {"All": 91, "Easy": 50, ...}."""
        q = """query p($username: String!) {
          matchedUser(username: $username) {
            submitStatsGlobal { acSubmissionNum { difficulty count } }
          }
        }"""
        try:
            d = self.gql(q, {"username": self.username}).get("matchedUser") or {}
            return {r["difficulty"]: r["count"] for r in d["submitStatsGlobal"]["acSubmissionNum"]}
        except Exception as e:
            print(f"  ! could not fetch profile counts: {e}")
            return {}

    def question(self, slug: str) -> dict:
        q = """query q($titleSlug: String!) {
          question(titleSlug: $titleSlug) {
            questionFrontendId title difficulty topicTags { name }
          }
        }"""
        d = self.gql(q, {"titleSlug": slug}).get("question") or {}
        return {
            "id": int(d["questionFrontendId"]) if d.get("questionFrontendId", "").isdigit() else None,
            "title": d.get("title") or slug,
            "difficulty": d.get("difficulty") or "Unknown",
            "tags": [t["name"] for t in d.get("topicTags") or []],
        }

    # ---- authenticated ---------------------------------------------------
    def signed_in_as(self) -> str | None:
        d = self.gql("query { userStatus { isSignedIn username } }").get("userStatus") or {}
        return d.get("username") if d.get("isSignedIn") else None

    def submissions_page(self, offset: int, lastkey: str = "") -> tuple[list[dict], bool, str]:
        q = """query s($offset: Int!, $limit: Int!, $lastKey: String) {
          submissionList(offset: $offset, limit: $limit, lastKey: $lastKey) {
            lastKey hasNext
            submissions { id title titleSlug timestamp statusDisplay lang runtime memory isPending }
          }
        }"""
        d = self.gql(q, {"offset": offset, "limit": 20, "lastKey": lastkey or None}).get("submissionList") or {}
        rows = [
            {
                "id": str(s["id"]),
                "slug": s["titleSlug"],
                "title": s["title"],
                "timestamp": int(s["timestamp"]),
                "status": s["statusDisplay"],
                "lang": s["lang"],
                "runtime": s.get("runtime"),
                "memory": s.get("memory"),
                "code": None,  # filled from submissionDetails
            }
            for s in d.get("submissions") or []
            if s.get("isPending") in (None, "Not Pending")
        ]
        return rows, bool(d.get("hasNext")), d.get("lastKey") or ""

    def submission_details(self, submission_id: str) -> dict:
        q = """query d($submissionId: Int!) {
          submissionDetails(submissionId: $submissionId) {
            code runtimeDisplay runtimePercentile memoryDisplay memoryPercentile
            totalCorrect totalTestcases lastTestcase codeOutput expectedOutput
            runtimeError compileError
          }
        }"""
        try:
            return self.gql(q, {"submissionId": int(submission_id)}).get("submissionDetails") or {}
        except Exception as e:  # details are a nice-to-have; never fail the sync over them
            print(f"  ! could not fetch details for {submission_id}: {e}")
            return {}
