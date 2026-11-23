"""Read the complexity you claimed in your code comments."""
from __future__ import annotations

import re

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
