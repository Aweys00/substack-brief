# Substack brief

A daily investing brief built from a list of Substacks. Claude fetches new posts, explains them, connects them to running themes, suggests long-only trade ideas and recommends further reading.

- `sources.json`: the reading list.
- `profile.md`: mandate, portfolio, watchlist, explanation preferences.
- `fetch.py`: pulls the RSS feeds into `data/posts/` (standard-library Python 3).
- `.claude/skills/substack-brief/SKILL.md`: the instructions Claude follows to write a brief.
- `notes/`: running theme notes and the idea log, updated by every brief.
- `briefs/`: one brief per day.

Run locally by asking Claude Code for "my Substack brief". A scheduled cloud routine runs it each morning, emails the brief and commits the updated files back here.
