import yaml
import trello
from time import sleep

class TrelloCLI:
    def __init__(self, authfile='auth/trello.yml', board=None):
        self.auth_file = authfile
        self.cli = self.authenticate()
        self.board = self.get_board_by_name(board)


    def set_board(self, board):
        self.board = self.get_board_by_name(board)
        return self.board


    def get_board_by_name(self, board):
        boards = self.cli.list_boards()
        for b in boards:
            if b.name == board:
                return b
        return None


    def get_creds(self):
        with open(self.auth_file, 'r') as f:
            auth_map = yaml.safe_load(f)
        return auth_map


    def authenticate(self):
        creds = self.get_creds()
        client = trello.TrelloClient(
            api_key = creds['trello_api_key'],
            api_secret = creds['trello_api_secret'],
            token = creds['trello_auth_token']
        )
        del creds
        return client


    def get_lists(self):
        return self.board.list_lists()


    def get_list_by_name(self, list_name):
        lists = self.board.list_lists()
        for l in lists:
            if l.name == list_name:
                return l
        return None


    def get_label_by_name(self, label_name):
        labels = self.board.get_labels()
        for label in labels:
            if label.name == label_name:
                return label
        return None


    def archive_list_cards(self, trl_list):
        lst = self.get_list_by_name(trl_list)
        lst.archive_all_cards()


    def add_card(self, list_name, card_name, card_desc=None, labels=None):
        lst = self.get_list_by_name(list_name)
        lst.add_card(card_name, card_desc, labels)


    def get_card_by_name(self, list_name, card_name):
        lst = self.get_list_by_name(list_name)
        cards = lst.list_cards()
        for card in cards:
            if card.name == card_name:
                return card
        return None


    def add_label(self, name, color):
        self.board.add_label(name, color)


class UpdatedList:
    def __init__(self, trello_client, name, feed):
        self.cli = trello_client
        self.name = name
        self.feed = feed


    def update_list(self):
        try:
            trl_list = self.cli.get_list_by_name(self.name)
            if trl_list:
                if trl_list.cardsCnt():
                    self.cli.archive_list_cards(self.name)
                for entry in self.feed.get_feed():
                    self.cli.add_card(self.name, entry['title'], entry['link'])
                    sleep(0.1)
            else:
                self.cli.board.add_list(self.name, pos='bottom')
            self.update_list()
        except trello.exceptions.ResourceUnavailable:
            sleep(10)
