# Interview Prep Dashboard

Every time you submit on LeetCode, a GitHub Action checks your submissions. It logs each attempt (Accepted, Wrong Answer, TLE, and so on), saves accepted code into `solutions/`, records the time and space complexity you wrote down, commits the result, and redeploys your dashboard to GitHub Pages.

```
LeetCode submit ──► GitHub Action (every ~15 min, or "Run workflow")
                      ├─ scripts/sync.py     pulls new submissions + failing test cases
                      ├─ complexity.py       reads "Time: O(..) Space: O(..)" from your code
                      ├─ git commit          data/*.json + solutions/<id>-<slug>/...
                      └─ deploy Pages        index.html reads data/dashboard.json
```

## Setup (about 5 minutes)

1. **Create a public GitHub repo** (Pages is free for public repos) and push this folder to it.
2. **Settings → Pages → Source: "GitHub Actions".**
3. **Settings → Secrets and variables → Actions**:
   | Kind | Name | Value | Needed for |
   |---|---|---|---|
   | Variable | `LEETCODE_USERNAME` | your LeetCode username | everything |
   | Secret | `LEETCODE_SESSION` | `LEETCODE_SESSION` cookie from leetcode.com | your code, failing test cases, older history |
   | Secret | `LEETCODE_CSRF` | `csrftoken` cookie from leetcode.com | (same) |

   To get the cookies: log in at leetcode.com, open DevTools → Application → Cookies → `https://leetcode.com`, and copy the two values. They expire every few weeks. When that happens the dashboard shows a banner and falls back to public data until you paste in fresh ones.
4. **Actions tab → "Sync LeetCode" → Run workflow.** The first run backfills up to 200 recent submissions.

With only the username set, the dashboard still tracks every verdict from your public profile. That feed only shows your ~20 most recent submissions, so syncing every 15 minutes is enough unless you submit 20+ times in 15 minutes.

## Tracking complexity

**1. State your answer** in a comment while you solve (you should be saying it out loud in an interview anyway):

```python
# Time: O(n log n)
# Space: O(n)
class Solution: ...
```

`TC = O(n)`, `time complexity - O(n^2)` and `SC: O(h)` also work. The sync picks it up automatically (needs the cookie secrets, since that's how it reads your code).

**2. Log the actual answer:** after checking the editorial or discussion, click **log** on that row in the dashboard. It opens a pre-filled *Log complexity* issue. Fill in the actual time and space (and fix your own answer if the comment was missing), add notes, and submit. The workflow records it in `data/manual.json`, closes the issue, and redeploys. The row then shows ✓ or ✗, and the accuracy tiles update. Notation is compared loosely, so `O(n log n)` matches `O(N*logN)`. Only issues you open yourself are processed.

## What's on the dashboard

- Problems solved (Easy/Medium/Hard), acceptance rate, first-try solve rate, streak
- Time and space complexity accuracy
- Activity heatmap and weekly accepted vs. failed submissions
- **What goes wrong**: failure types and wrong-complexity count
- **Topics**, weakest first: failure rate and complexity misses per tag
- **Review queue**: unsolved problems, ones you failed, or ones where your complexity was wrong
- Full submission log with the failing input / expected / actual output and a link to your saved code

Filters for 7d / 30d / 90d / all and difficulty are at the top.

## Run locally

```bash
pip install -r requirements.txt
LEETCODE_USERNAME=you python scripts/sync.py
python -m http.server   # open http://localhost:8000
```

## Knobs

- Sync interval: `cron` in `.github/workflows/sync.yml`. GitHub may delay scheduled runs, and pauses them after 60 days without repo activity.
- `MAX_PAGES` (backfill depth, 20 per page) is an env var on the sync step.
