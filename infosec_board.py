from trellohelp import TrelloCLI, UpdatedList
from rsshelp import RSSFeed

def main():
    cli = TrelloCLI(board='API Test')

    r_netsec = UpdatedList(cli, '/r/netsec', RSSFeed('https://reddit.com/r/netsec/.rss'))
    r_redteamsec = UpdatedList(cli, '/r/redteamsec', RSSFeed('https://reddit.com/r/redteamsec/.rss'))
    r_blueteamsec = UpdatedList(cli, '/r/blueteamsec', RSSFeed('https://reddit.com/r/blueteamsec/.rss'))
    r_asknetsec = UpdatedList(cli, '/r/asknetsec', RSSFeed('https://reddit.com/r/asknetsec/.rss'))

    w_krebs = UpdatedList(cli, 'Krebs on Security', RSSFeed('https://krebsonsecurity.com/feed/'))
    w_schneier = UpdatedList(cli, 'Schneier on Security', RSSFeed('https://www.schneier.com/blog/atom.xml'))
    
    n_wired = UpdatedList(cli, 'Wired Security', RSSFeed('https://www.wired.com/feed/security/rss'))
    n_motherboard = UpdatedList(cli, 'Motherboard', RSSFeed('https://motherboard.vice.com/en_us/rss'))

    board_lists = [r_netsec, r_redteamsec, r_blueteamsec, r_asknetsec, w_krebs, w_schneier, n_wired, n_motherboard]
    for board in board_lists:
        board.update_list()

if __name__ == '__main__':
    main()