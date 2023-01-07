import requests
from base import *
from time import sleep
import time


class Api:


	def __init__(self,proxy,auth_token):
		self.s = requests.Session()
		self.proxies = {
		  "http": proxy,
		  "https": proxy
		}
		self.s.proxies = self.proxies
		self.s.headers.update({"Authorization":f"Bearer {auth_token}"})


	def getSession(self):
		return db.get(Conf,1).session_id


	def parse(self,links):
		accounts = []
		added = []
		inbase = db.query(Account).all()
		session_id = self.getSession()
		for i in inbase:
			added.append(i.username)
		for l in links:
			name = l.split('/')[-1].lower()
			db.add(Sessions(session_id=session_id,username=name,status=2))
		db.commit()
		for l in links:
			name = l.split('/')[-1].lower()
			session = db.query(Sessions).filter_by(username=name,session_id=session_id).first()
			try:
				r = self.s.get(f'https://api.twitter.com/1.1/users/show.json?screen_name={name}')
				if int(r.headers['x-rate-limit-remaining'])>5:
					pass
				else:
					print('wait limit reset')
					sleep(int(r.headers['x-rate-limit-reset'])-time.time())
					r = self.s.get(f'https://api.twitter.com/1.1/users/show.json?screen_name={name}')
			except Exception as e:
				session.status = 3
				db.commit()
				continue
			data = r.json()
			if data.get('errors'):
				session.status = 3
				db.commit()
				continue
			try:
				description = data['status']['text']
			except:
				description = ""
			if name not in added:
				db.add(
					Account(
						twitter_id = data['id'], 
						name = data['name'], 
						username = data['screen_name'].lower(), 
						following_count = data['friends_count'],
						followers_count = data['followers_count'],
						description = description
					))
				session.status = 1
				db.commit()
			else:
				account = db.query(Account).filter_by(username=name).first()
				account.twitter_id = data['id']
				account.name = data['name']
				account.username = data['screen_name'].lower()
				account.following_count = data['friends_count']
				account.followers_count = data['followers_count']
				account.description = description
				session.status = 1
				db.commit()
		nsi = db.get(Conf,1)
		nsi.session_id+=1
		db.commit()
		return {"session_id": session_id}


	def parseTwits(self, twitter_id):
		r = self.s.get(f'https://api.twitter.com/2/users/{twitter_id}/tweets?max_results=10')
		if int(r.headers['x-rate-limit-remaining'])>5:
			pass
		else:
			print('wait limit reset')
			sleep(int(r.headers['x-rate-limit-reset'])-time.time())
			r = self.s.get(f'https://api.twitter.com/2/users/{twitter_id}/tweets?max_results=10')
		data = r.json()
		return data