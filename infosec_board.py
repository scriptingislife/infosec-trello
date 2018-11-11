from trellohelp import TrelloCLI, UpdatedList
from rsshelp import RSSFeed

def main():
    cli = TrelloCLI(board='API Test')

    # Why the prefix? I don't know.
    # r = subreddit
    # b = blog
    # n = news

    r_netsec = UpdatedList(cli, '/r/netsec', RSSFeed('https://reddit.com/r/netsec/.rss'), limit=10)
    r_redteamsec = UpdatedList(cli, '/r/redteamsec', RSSFeed('https://reddit.com/r/redteamsec/.rss'), limit=5)
    r_blueteamsec = UpdatedList(cli, '/r/blueteamsec', RSSFeed('https://reddit.com/r/blueteamsec/.rss'), limit=5)
    r_asknetsec = UpdatedList(cli, '/r/asknetsec', RSSFeed('https://reddit.com/r/asknetsec/.rss'), limit=5)

    b_krebs = UpdatedList(cli, 'Krebs on Security', RSSFeed('https://krebsonsecurity.com/feed/'))
    b_schneier = UpdatedList(cli, 'Schneier on Security', RSSFeed('https://www.schneier.com/blog/atom.xml'))
    
    n_wired = UpdatedList(cli, 'Wired - Security', RSSFeed('https://www.wired.com/feed/security/rss'))
    n_motherboard = UpdatedList(cli, 'Motherboard', RSSFeed('https://motherboard.vice.com/en_us/rss'))
    n_thehackernews = UpdatedList(cli, 'The Hacker News', RSSFeed('https://thehackernews.com/feeds/posts/default'))
    n_zdnet = UpdatedList(cli, 'ZDNet', RSSFeed('https://www.zdnet.com/news/rss.xml'))

    board_lists = [r_netsec, b_krebs, b_schneier, n_thehackernews, n_zdnet, n_wired, n_motherboard, r_redteamsec, r_blueteamsec, r_asknetsec]
    for board in board_lists:
        board.update_list()


if __name__ == '__main__':
    main()