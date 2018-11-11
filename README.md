# Infosec Trello
Live Updating Infosec Dashboard on Trello

# Run your own

`git clone https://github.com/becksteadn/infosec-trello.git`

## Trello API and Authentication

`mkdir auth && touch auth/trello.yml`

Your key, secret, and token can be found on the [Trello Developers](https://trello.com/app-key) page. Use the link where it says `you can manually generate a Token` to get your token. Add them to `auth/trello.yml`

```yaml
---
trello_api_key: 'MYKEY'
trello_api_secret: 'MYSECRET'
trello_auth_token: 'MYTOKEN'
```

## Dependencies
```bash
virtualenv .env
source .env/bin/activate
pip install -r requirements.txt
```

## Run

`python infosec_board.py`