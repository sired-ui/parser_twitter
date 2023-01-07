from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from api import *
from queryModels import *
import threading


proxy = "http://uJEM1BHn:HBPjf7Tc@212.193.143.51:48707"

API_BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADFbbgEAAAAAgbDQ72%2BKSSj4LUlfXndxsYyAs1c%3D7rYx14Ozbpzl7dJF4DkCsWxj198YKHM60emOl7bDtZhO24TQ4h"

app = FastAPI()

parser = Api(proxy,API_BEARER_TOKEN)
 
@app.post("/")
def read_root(links: Links):
    session_id = parser.getSession()
    thread = threading.Thread(target=parser.parse, args=(links.links,))
    thread.start()
    return {"session_id": session_id}


@app.get("/api/users/status")
def get_statuses(session_id: Session):
	return get_session(session_id.session_id)


@app.get("/api/user/{username}")
def get_user(username):
	return get_user_data(username)


@app.get("/api/tweets/{twitter_id}")
def get_tweets(twitter_id):
	return parser.parseTwits(twitter_id)