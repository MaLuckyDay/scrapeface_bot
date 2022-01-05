import os
import requests
from slack import WebClient
from slack.errors import SlackApiError
from dotenv import load_dotenv
from trello import TrelloApi
from firebase import firebase

load_dotenv()

client = WebClient(token=os.environ['SLACK_API_TOKEN'])
def sendMessage(message):
    try:
        response = client.chat_postMessage(channel= '#general', text=message)
        assert response["message"]["text"] == "Hello world!"
    except SlackApiError as e:
        assert e.response["ok"] is False
        assert e.response["error"]
        print(f"Got an error: {e.response['error']}")

#sendMessage("Hello world!")

trello = TrelloApi(os.environ['TRELLO_APP_KEY'])
#trello.get_token_url('Scrapeface', expires='30days', write_access=True)
trello.set_token(os.environ['TRELLO_USER_TOKEN'])
board = trello.boards.get('8QowJ5O7')
backlog_list = trello.lists.get('61c353039846a238d597862c')
def create_card(list_id, card_name):
    url = f"https://api.trello.com/1/cards"
    querystring = {"name": card_name, "idList": list_id, "key": os.environ['TRELLO_APP_KEY'], "token": os.environ['TRELLO_USER_TOKEN']}
    response = requests.request("POST", url, params=querystring)
    card_id = response.json()
#create_card('61c353039846a238d597862c', "PROGRAM TEST ONE")

scrapebase = firebase.FirebaseApplication(os.environ['REAL_TIME_DATABASE'])
def cardToDatabase(category, card_id, card_title, list_id):
    result = scrapebase.put('/scrapeface_bot', category, {"id": card_id, "title": card_title, "list_id": list_id})
    return result

cardToDatabase("/card1", "003", "TEST_003", "003")
#help