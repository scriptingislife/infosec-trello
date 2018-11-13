# Infosec Trello
Live updating infosec news dashboard on Trello.

https://trello.com/b/rKgxV8ZS/infosec-news

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

## Automatic Updates

Enter the cron job editor using `crontab -e`. Select an editor if prompted. Add the bottom of the file add the following line.

`0 * * * * cd INSTALL_LOCATION/infosec-trello && ./cron.sh`

Replace `INSTALL_LOCATION` with the directory you cloned the repository to. This default job runs every hour on the hour. Use a timeframe like `0 */4 * * *` to run the script every four hours.
