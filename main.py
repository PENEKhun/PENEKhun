import feedparser
import time

URL = "https://blog.huni.kr/feed.xml"
RSS_FEED = feedparser.parse(URL)
MAX_POST = 5

markdown_text = ""

# Load contents of original.md
with open("original.md", mode="r", encoding="utf-8") as f:
    markdown_text = f.read().strip()

markdown_text += "<br/>\n\n## ✅ Latest Blog Post\n\n"  # list of blog posts will be appended here

for idx, feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_date = feed['published_parsed']
        markdown_text += f"[{time.strftime('%Y/%m/%d', feed_date)} - {feed['title']}]({feed['link']}) <br/>\n"

# Write modified content to README.md
with open("README.md", mode="w", encoding="utf-8") as f:
    f.write(markdown_text)
