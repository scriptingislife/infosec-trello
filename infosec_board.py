from trellohelp import TrelloCLI, UpdatedList
from rsshelp import RSSFeed
import yaml
import os

def lambda_handler(event, context):
    main()

def main():
    config = dict()
    try:
        with open('config.yml', 'r') as f:
            config = yaml.safe_load(f)
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
        config['board'] = os.environ.get('TRELLO_BOARD')

    cli = TrelloCLI(config=config)

    board_lists = [
        UpdatedList(cli, '/r/netsec', RSSFeed('https://reddit.com/r/netsec/.rss')),
        UpdatedList(cli, 'Schneier on Security', RSSFeed('https://www.schneier.com/blog/atom.xml')),
        UpdatedList(cli, 'Dark Reading', RSSFeed('https://www.darkreading.com/rss_simple.asp')),
        UpdatedList(cli, 'Bleeping Computer', RSSFeed('https://www.bleepingcomputer.com/feed/')),
        UpdatedList(cli, 'The Register - Security', RSSFeed('https://www.theregister.co.uk/security/headlines.atom')),
        UpdatedList(cli, 'Wired - Security', RSSFeed('https://www.wired.com/feed/security/rss')),
        UpdatedList(cli, 'Motherboard', RSSFeed('https://motherboard.vice.com/en_us/rss')),
        UpdatedList(cli, 'ZDNet', RSSFeed('https://www.zdnet.com/news/rss.xml'))
    ]

    for board in board_lists:
        board.update_list()


if __name__ == '__main__':
    main()