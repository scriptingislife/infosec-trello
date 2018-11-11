import feedparser
from trellohelp import TrelloCLI

class RSSFeed:
    def __init__(self, url):
        self.url = url
        self.feed = None
        self.update_feed()

    def update_feed(self):
        self.feed = feedparser.parse(self.url)

    def print_feed(self):
        entries = self.feed.entries
        for entry in entries:
            print(entry['title'])

    def get_feed(self, limit=None):
        if limit:
            return self.feed['entries'][:limit]
        else:
            return self.feed['entries']