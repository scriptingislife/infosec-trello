from trellohelp import TrelloCLI, UpdatedList
from rsshelp import RSSFeed
import yaml
import os

def main():
    try:
        with open('config.yml', 'r') as f:
            config_file = yaml.safe_load(f)
        if config['trello_api_key'] is None:
            config['trello_api_key'] = os.environ.get('TRELLO_API_KEY')
        
        if config['trello_api_secret'] is None:
            config['trello_api_secret'] = os.environ.get('TRELLO_API_SECRET')
        
        if config['trello_auth_token'] is None:
            config['trello_auth_token'] = os.environ.get('TRELLO_AUTH_TOKEN')
        
        if config['board'] is None:
            config['board'] = os.environ.get('INFOSEC_BOARD')
    except FileNotFoundError as e:
        config['trello_api_key'] = os.environ.get('TRELLO_API_KEY')
        config['trello_api_secret'] = os.environ.get('TRELLO_API_SECRET')
        config['trello_auth_token'] = os.environ.get('TRELLO_AUTH_TOKEN')
        config['board'] = os.environ.get('INFOSEC_BOARD')

    cli = TrelloCLI(board=config['board'])

    # Why the prefix? I don't know.
    # r = subreddit
    # b = blog
    # n = news

    r_netsec = UpdatedList(cli, '/r/netsec', RSSFeed('https://reddit.com/r/netsec/.rss'), limit=10)
    r_redteamsec = UpdatedList(cli, '/r/redteamsec', RSSFeed('https://reddit.com/r/redteamsec/.rss'), limit=5)
    r_blueteamsec = UpdatedList(cli, '/r/blueteamsec', RSSFeed('https://reddit.com/r/blueteamsec/.rss'), limit=5)
    r_asknetsec = UpdatedList(cli, '/r/asknetsec', RSSFeed('https://reddit.com/r/asknetsec/.rss'), limit=5)

    #b_krebs = UpdatedList(cli, 'Krebs on Security', RSSFeed('https://krebsonsecurity.com/feed/'))
    b_schneier = UpdatedList(cli, 'Schneier on Security', RSSFeed('https://www.schneier.com/blog/atom.xml'))
    
    n_darkreading = UpdatedList(cli, 'Dark Reading', RSSFeed('https://www.darkreading.com/rss_simple.asp'))
    n_bleepingcomputer = UpdatedList(cli, 'Bleeping Computer', RSSFeed('https://www.bleepingcomputer.com/feed/'))
    n_theregister = UpdatedList(cli, 'The Register - Security', RSSFeed('https://www.theregister.co.uk/security/headlines.atom'), limit=20)
    n_wired = UpdatedList(cli, 'Wired - Security', RSSFeed('https://www.wired.com/feed/security/rss'))
    n_motherboard = UpdatedList(cli, 'Motherboard', RSSFeed('https://motherboard.vice.com/en_us/rss'))
    #n_thehackernews = UpdatedList(cli, 'The Hacker News', RSSFeed('https://thehackernews.com/feeds/posts/default'))
    n_zdnet = UpdatedList(cli, 'ZDNet', RSSFeed('https://www.zdnet.com/news/rss.xml'))

    board_lists = [r_netsec, n_darkreading, n_bleepingcomputer, n_theregister, b_schneier, n_zdnet, n_wired, n_motherboard, r_redteamsec, r_blueteamsec, r_asknetsec]
    for board in board_lists:
        board.update_list()


if __name__ == '__main__':
    main()