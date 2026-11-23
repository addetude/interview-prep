"""Turn a "Log complexity" issue (see .github/ISSUE_TEMPLATE) into an entry in data/manual.json."""
from __future__ import annotations

import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path

MANUAL = Path(__file__).resolve().parent.parent / "data" / "manual.json"
FIELDS = {
    "problem": "slug",
    "submission": "submission",
    "my time complexity": "my_time",
    "my space complexity": "my_space",
    "actual time complexity": "actual_time",
    "actual space complexity": "actual_space",
    "notes": "notes",
}


def parse(body: str) -> dict:
    entry: dict = {}
    for section in re.split(r"^###\s+", body or "", flags=re.M)[1:]:
        label, _, value = section.partition("\n")
        value = value.strip()
        field = next((f for prefix, f in FIELDS.items() if label.strip().lower().startswith(prefix)), None)
        if field and value and value != "_No response_":
            entry[field] = value
    if "slug" in entry:  # accept a full URL or a slug
        m = re.search(r"/problems/([\w-]+)", entry["slug"])
        entry["slug"] = (m.group(1) if m else entry["slug"]).strip().strip("/").lower()
    return entry


def main() -> None:
    entry = parse(os.environ.get("ISSUE_BODY", ""))
    if not entry.get("slug") and not entry.get("submission"):
        raise SystemExit("Issue has no problem or submission; nothing to log.")
    entry["logged_at"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    entry["issue"] = os.environ.get("ISSUE_NUMBER")
    manual = json.loads(MANUAL.read_text()) if MANUAL.exists() else []
    manual.append(entry)
    MANUAL.write_text(json.dumps(manual, indent=1, ensure_ascii=False) + "\n")
    print(f"Logged: {entry}")


if __name__ == "__main__":
    main()
