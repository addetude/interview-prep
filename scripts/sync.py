"""Pull new LeetCode submissions, enrich them, and rebuild data/dashboard.json.

Run by .github/workflows/sync.yml; safe to run locally too:
    LEETCODE_USERNAME=you python scripts/sync.py
"""
from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

import complexity
from leetcode import AuthExpired, LeetCode

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
SOLUTIONS = ROOT / "solutions"
MAX_PAGES = int(os.environ.get("MAX_PAGES", "10"))  # 20 submissions per page

EXT = {
    "python": "py", "python3": "py", "java": "java", "cpp": "cpp", "c": "c", "csharp": "cs",
    "javascript": "js", "typescript": "ts", "golang": "go", "go": "go", "rust": "rs", "kotlin": "kt",
    "swift": "swift", "ruby": "rb", "scala": "scala", "php": "php", "mysql": "sql", "mssql": "sql",
    "oraclesql": "sql", "postgresql": "sql", "bash": "sh", "dart": "dart", "elixir": "ex",
}


def load(name: str, default):
    p = DATA / name
    return json.loads(p.read_text()) if p.exists() else default


def save(name: str, obj) -> None:
    (DATA / name).write_text(json.dumps(obj, indent=1, ensure_ascii=False) + "\n")


def key_of(s: dict) -> str:
    return f"{s['timestamp']}-{s['slug']}"


# ---------------------------------------------------------------------------
def fetch_new(lc: LeetCode, known: set[str], state: dict) -> list[dict]:
    if lc.authed:
        try:
            me = lc.signed_in_as()
            if not me:
                raise AuthExpired()
            print(f"Signed in to LeetCode as {me}")
            out, offset, lastkey = [], 0, ""
            for _ in range(MAX_PAGES):
                rows, has_next, lastkey = lc.submissions_page(offset, lastkey)
                fresh = [r for r in rows if key_of(r) not in known]
                out += fresh
                if len(fresh) < len(rows) or not has_next:
                    break
                offset += 20
                time.sleep(1.5)
            state["auth"] = "ok"
            return out
        except AuthExpired:
            print("! LeetCode says these cookies aren't signed in (expired or copied wrong); using public data")
            state["auth"] = "expired"
            lc.authed = False
        except Exception as e:
            print(f"! Signed-in fetch failed ({e!r}); using public data this run")
            state["auth"] = "blocked"
            lc.authed = False
    else:
        state["auth"] = "public"
    return [r for r in lc.recent_public() if key_of(r) not in known]


def save_solution(sub: dict, problem: dict) -> str | None:
    if not sub.get("code") or sub["status"] != "Accepted":
        return None
    pid = problem.get("id")
    folder = SOLUTIONS / (f"{pid:04d}-{sub['slug']}" if pid else sub["slug"])
    folder.mkdir(parents=True, exist_ok=True)
    day = datetime.fromtimestamp(sub["timestamp"], timezone.utc).strftime("%Y-%m-%d")
    path = folder / f"{day}_{sub['id']}.{EXT.get(sub['lang'], 'txt')}"
    path.write_text(sub["code"])
    return str(path.relative_to(ROOT))


# ---------------------------------------------------------------------------
def manual_for(subs: list[dict], manual: list[dict]) -> dict[str, dict]:
    """Map submission key -> your manual complexity entry (latest entry wins)."""
    by_key: dict[str, dict] = {}
    for m in sorted(manual, key=lambda m: m.get("logged_at", "")):
        target = None
        if m.get("submission"):
            target = next((s for s in subs if s["key"] == m["submission"] or s.get("id") == m["submission"]), None)
        if not target and m.get("slug"):
            same = [s for s in subs if s["slug"] == m["slug"]]
            target = next((s for s in same if s["status"] == "Accepted"), same[0] if same else None)
        if target:
            by_key[target["key"]] = m
    return by_key


def effective_claims(sub: dict, m: dict | None) -> dict:
    claims = dict(sub.get("claims") or {"time": None, "space": None})
    if m:
        claims["time"] = m.get("my_time") or claims.get("time")
        claims["space"] = m.get("my_space") or claims.get("space")
    return claims


def verdicts(sub: dict, m: dict | None) -> dict:
    claims = effective_claims(sub, m)
    res = {"my_time": claims["time"], "my_space": claims["space"], "source": "manual" if m else "code"}
    for dim in ("time", "space"):
        actual = (m or {}).get(f"actual_{dim}")
        correct = None
        if claims[dim] and actual:
            correct = complexity.normalize(claims[dim]) == complexity.normalize(actual)
        res[f"actual_{dim}"] = actual
        res[f"{dim}_ok"] = correct
    res["notes"] = (m or {}).get("notes")
    return res


# ---------------------------------------------------------------------------
def main() -> None:
    DATA.mkdir(exist_ok=True)
    lc = LeetCode.from_env()
    subs: list[dict] = load("submissions.json", [])
    problems: dict = load("problems.json", {})
    manual: list[dict] = load("manual.json", [])
    state: dict = load("state.json", {})
    by_key = {s["key"]: s for s in subs}

    # When authenticated, re-fetch entries first seen via the public feed so we pick up their code.
    known = {k for k, s in by_key.items() if s.get("id")} if lc.authed else set(by_key)
    new = fetch_new(lc, known, state)
    print(f"{len(new)} new submission(s) [{state['auth']} mode]")

    for s in sorted(new, key=lambda s: s["timestamp"]):
        s["key"] = key_of(s)
        if s["slug"] not in problems:
            problems[s["slug"]] = lc.question(s["slug"])
            time.sleep(0.5)
        if lc.authed and s.get("id"):
            d = lc.submission_details(s["id"])
            s["code"] = s.get("code") or d.get("code")
            s.update(
                runtime=d.get("runtimeDisplay") or s.get("runtime"),
                memory=d.get("memoryDisplay") or s.get("memory"),
                runtime_pct=d.get("runtimePercentile"),
                memory_pct=d.get("memoryPercentile"),
                passed=d.get("totalCorrect"),
                total=d.get("totalTestcases"),
            )
            if s["status"] != "Accepted":
                s.update(
                    last_input=d.get("lastTestcase"),
                    expected=d.get("expectedOutput"),
                    output=d.get("codeOutput"),
                    error=d.get("runtimeError") or d.get("compileError"),
                )
            time.sleep(0.5)
        s["claims"] = complexity.parse_claims(s.get("code"))
        s["solution_path"] = save_solution(s, problems[s["slug"]])
        s.pop("code", None)
        by_key[s["key"]] = {k: v for k, v in s.items() if v not in (None, "")} | {"claims": s["claims"]}
        print(f"  + {s['status']:<22} {s['title']}")

    subs = sorted(by_key.values(), key=lambda s: s["timestamp"], reverse=True)
    manual_map = manual_for(subs, manual)

    state["last_sync"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    save("submissions.json", subs)
    save("problems.json", problems)
    save("state.json", state)

    dashboard = {
        "generated_at": state["last_sync"],
        "username": lc.username,
        "repo": os.environ.get("GITHUB_REPOSITORY"),
        "auth": state["auth"],
        "submissions": [
            {
                **{k: s.get(k) for k in (
                    "key", "id", "slug", "timestamp", "status", "lang", "runtime", "memory", "runtime_pct",
                    "passed", "total", "last_input", "expected", "output", "error", "solution_path")},
                **problems.get(s["slug"], {}),
                "complexity": verdicts(s, manual_map.get(s["key"])),
            }
            for s in subs
        ],
    }
    save("dashboard.json", dashboard)

    acc = sum(1 for s in new if s["status"] == "Accepted")
    msg = f"sync: {len(new)} new submission(s), {acc} accepted"
    if not new:
        msg = "sync: refresh"
    if out := os.environ.get("GITHUB_OUTPUT"):
        with open(out, "a") as f:
            f.write(f"message={msg}\n")


if __name__ == "__main__":
    main()
