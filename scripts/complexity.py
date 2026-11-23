"""Read the complexity you claimed in your code, and (optionally) have Claude check it."""
from __future__ import annotations

import os
import re
from typing import Optional

from pydantic import BaseModel

# "Time: O(n log n)", "TC = O(n)", "time complexity - O(n^2)", "Space: O(1)", "SC: O(h)" ...
_LABELS = {
    "time": r"(?:time(?:\s+complexity)?|tc)",
    "space": r"(?:space(?:\s+complexity)?|sc)",
}


def _balanced_o(text: str, start: int) -> str | None:
    """Return 'O(...)' starting at text[start] == 'O', honouring nested parentheses."""
    depth = 0
    for i in range(start + 1, min(len(text), start + 80)):
        if text[i] == "(":
            depth += 1
        elif text[i] == ")":
            depth -= 1
            if depth == 0:
                return text[start : i + 1]
    return None


def parse_claims(code: str | None) -> dict:
    """Find the complexity you wrote in a comment, e.g. `# Time: O(n)  Space: O(1)`."""
    out = {"time": None, "space": None}
    if not code:
        return out
    for key, label in _LABELS.items():
        m = re.search(rf"\b{label}\b\s*[:=\-–]?\s*(?=[oOΘθ]\s*\()", code, re.IGNORECASE)
        if m:
            claim = _balanced_o(code, m.end())
            if claim:
                out[key] = "O" + claim[1:]
    return out


def normalize(expr: str | None) -> str:
    """Loose canonical form so 'O(n log n)' == 'O(N*logN)' == 'o(nlog(n))'."""
    if not expr:
        return ""
    s = expr.lower().replace("θ", "o")
    s = re.sub(r"[\s*·×⋅]", "", s)
    s = re.sub(r"log\((\w+)\)", r"log\1", s)
    s = s.replace("^", "").replace("**", "")
    return s


class Grade(BaseModel):
    time: str
    space: str
    time_correct: Optional[bool]
    space_correct: Optional[bool]
    explanation: str


_SYSTEM = """You grade time/space complexity answers for coding-interview practice.
Given a LeetCode problem and an accepted solution, determine the tight worst-case
big-O time and auxiliary space of THIS code (not the optimal solution).
Conventions: use the problem's natural variables (n, m, k, V, E, ...); auxiliary space
includes recursion stack and data structures the code allocates, but excludes the input
and the returned output. If the candidate stated a complexity, mark it correct when it
is asymptotically equivalent to yours (notation differences don't matter); a looser
bound (e.g. O(n^2) for an O(n) algorithm) or a tighter-than-true bound is incorrect.
If they did not state one, the *_correct field is null.
Keep the explanation to 1-3 short sentences an interviewer would say."""


def grade(title: str, lang: str, code: str, claims: dict) -> Grade | None:
    """Ask Claude for the true complexity and whether your claims hold. None if no API key."""
    if not os.environ.get("ANTHROPIC_API_KEY"):
        return None
    import anthropic

    client = anthropic.Anthropic()
    prompt = (
        f"Problem: {title}\nLanguage: {lang}\n"
        f"Candidate's stated time complexity: {claims.get('time') or '(not stated)'}\n"
        f"Candidate's stated space complexity: {claims.get('space') or '(not stated)'}\n\n"
        f"<solution>\n{code}\n</solution>"
    )
    try:
        resp = client.beta.messages.parse(
            model="claude-opus-5-5",
            max_tokens=4000,
            betas=["server-side-fallback-2026-07-01"],
            fallbacks="default",
            output_config={"effort": "medium"},
            system=_SYSTEM,
            messages=[{"role": "user", "content": prompt}],
            output_format=Grade,
        )
    except anthropic.APIStatusError as e:
        print(f"  ! Claude API error ({e.status_code}); will retry next sync")
        return None
    except anthropic.APIConnectionError:
        print("  ! could not reach the Claude API; will retry next sync")
        return None
    if resp.stop_reason == "refusal" or resp.parsed_output is None:
        print(f"  ! grading skipped (stop_reason={resp.stop_reason})")
        return None
    return resp.parsed_output
