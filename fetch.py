#!/usr/bin/env python3
"""Fetch new posts from the Substacks in sources.json.

Usage:
  python3 fetch.py                 Fetch feeds, save new posts, list unbriefed posts as JSON.
  python3 fetch.py --days 3        Only list unbriefed posts published in the last 3 days (default 7).
  python3 fetch.py --mark-briefed  Mark every currently listed post as briefed (run after the brief is written).

Posts are saved as markdown in data/posts/<source>/<date>-<slug>.md.
State lives in data/state.json. Standard library only.
"""
import argparse
import json
import re
import ssl
import sys
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parent
POSTS = ROOT / "data" / "posts"
STATE = ROOT / "data" / "state.json"
MAC_CERTS = "/etc/ssl/cert.pem"
NS = {
    "content": "http://purl.org/rss/1.0/modules/content/",
    "dc": "http://purl.org/dc/elements/1.1/",
}
SKIP_TAGS = {"script", "style", "svg", "button", "form", "iframe", "figcaption"}
BLOCK_TAGS = {"p", "div", "blockquote", "ul", "ol", "figure", "hr", "table", "tr"}
BOILERPLATE = re.compile(
    r"^(subscribe now|share|leave a comment|read more|thanks for reading.*|share .{0,60})$", re.I
)


class Markdownify(HTMLParser):
    """Small HTML-to-markdown converter: headings, paragraphs, lists, links."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip = 0
        self.href = None
        self.link_text = []

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self.skip += 1
        elif self.skip:
            return
        elif tag in ("h1", "h2", "h3", "h4"):
            self.out.append("\n\n" + "#" * (int(tag[1]) + 1) + " ")
        elif tag == "li":
            self.out.append("\n- ")
        elif tag == "br":
            self.out.append("\n")
        elif tag in BLOCK_TAGS:
            self.out.append("\n\n")
        elif tag == "a":
            self.href = dict(attrs).get("href")
            self.link_text = []

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS:
            self.skip = max(0, self.skip - 1)
        elif self.skip:
            return
        elif tag == "a" and self.href is not None:
            text = "".join(self.link_text).strip()
            href, self.href = self.href, None
            if text:
                self.out.append(f"[{text}]({href})" if href.startswith("http") else text)
        elif tag in BLOCK_TAGS or tag in ("h1", "h2", "h3", "h4"):
            self.out.append("\n\n")

    def handle_data(self, data):
        if self.skip:
            return
        (self.link_text if self.href is not None else self.out).append(data)


def to_markdown(html):
    parser = Markdownify()
    parser.feed(html)
    lines = [re.sub(r"[ \t\xa0]+", " ", ln).strip() for ln in "".join(parser.out).split("\n")]
    lines = [ln for ln in lines if not BOILERPLATE.match(re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", ln))]
    return re.sub(r"\n{3,}", "\n\n", "\n".join(lines)).strip()


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (feed reader)"})
    ctx = ssl.create_default_context()
    # python.org builds on macOS ship without root certificates; use the system bundle.
    if Path(MAC_CERTS).exists():
        ctx.load_verify_locations(MAC_CERTS)
    with urllib.request.urlopen(req, timeout=30, context=ctx) as resp:
        return resp.read()


def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:70] or "post"


def load_state():
    return json.loads(STATE.read_text()) if STATE.exists() else {}


def save_state(state):
    STATE.parent.mkdir(parents=True, exist_ok=True)
    STATE.write_text(json.dumps(state, indent=1, sort_keys=True))


def pull(source, state):
    """Save any unseen posts from one feed. Returns the number of new posts."""
    root = ET.fromstring(fetch(source["feed"]))
    new = 0
    for item in root.iter("item"):
        guid = (item.findtext("guid") or item.findtext("link") or "").strip()
        if not guid or guid in state:
            continue
        title = (item.findtext("title") or "Untitled").strip()
        link = (item.findtext("link") or "").strip()
        html = item.findtext("content:encoded", default="", namespaces=NS) or item.findtext("description") or ""
        try:
            published = parsedate_to_datetime(item.findtext("pubDate")).astimezone(timezone.utc)
        except (TypeError, ValueError):
            published = datetime.now(timezone.utc)
        # Substack ends the feed body of a paywalled post with a "Read more" link.
        preview_only = bool(re.search(r"Read more\s*(</a>)?\s*(</p>|</div>|\s)*$", html))
        body = to_markdown(html)
        folder = POSTS / source["slug"]
        folder.mkdir(parents=True, exist_ok=True)
        path = folder / f"{published:%Y-%m-%d}-{slugify(title)}.md"
        header = {
            "title": title,
            "source": source["name"],
            "author": (item.findtext("dc:creator", default="", namespaces=NS) or "").strip(),
            "url": link,
            "published": published.isoformat(),
            "words": len(body.split()),
            "preview_only": preview_only,
        }
        front = "\n".join(f"{k}: {json.dumps(v, ensure_ascii=False)}" for k, v in header.items())
        path.write_text(f"---\n{front}\n---\n\n# {title}\n\n{body}\n", encoding="utf-8")
        state[guid] = {**header, "path": str(path.relative_to(ROOT)), "briefed": False}
        new += 1
    return new


def pending(state, days):
    cutoff = datetime.now(timezone.utc) - timedelta(days=days)
    rows = [
        {"guid": g, **v}
        for g, v in state.items()
        if not v["briefed"] and datetime.fromisoformat(v["published"]) >= cutoff
    ]
    return sorted(rows, key=lambda r: r["published"])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--days", type=int, default=7, help="lookback window for unbriefed posts (default 7)")
    ap.add_argument("--mark-briefed", action="store_true", help="mark listed posts as briefed, without fetching")
    args = ap.parse_args()
    state = load_state()

    if args.mark_briefed:
        rows = pending(state, args.days)
        for row in rows:
            state[row["guid"]]["briefed"] = True
        save_state(state)
        print(f"Marked {len(rows)} posts as briefed.")
        return

    errors = []
    for source in json.loads((ROOT / "sources.json").read_text()):
        try:
            pull(source, state)
        except Exception as exc:  # one bad feed should not block the others
            errors.append(f"{source['name']}: {exc}")
    save_state(state)
    rows = pending(state, args.days)
    for row in rows:
        row.pop("guid")
        row.pop("briefed")
    json.dump({"posts": rows, "errors": errors}, sys.stdout, indent=1, ensure_ascii=False)
    print()


if __name__ == "__main__":
    main()
