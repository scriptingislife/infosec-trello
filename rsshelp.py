import feedparser
from datetime import datetime
from time import mktime

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

def is_recent(entry, limit=4):
    # This is a real jank way to see if date_parsed or published_parsed exists
    feed_date = None
    today = False
    recent = False
    try:
        feed_date = entry.date_parsed
    except AttributeError:
        pass
    try:
        if feed_date is None:
            feed_date = entry.published_parsed
    except AttributeError:
        return {'today': True, 'recent': True}

    feed_elapsed = datetime.now() - datetime.fromtimestamp(mktime(feed_date))
    if feed_elapsed.days == 0:
        today = True
        if feed_elapsed.seconds / 3600 > limit:
            recent = True

    return {'today': today, 'recent': recent}