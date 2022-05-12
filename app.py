# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask import request
from twilio.rest import Client
import json, time
import requests
from websocket import create_connection
import os
import pickle

from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC6ad5ff1f49211e3f0a635dbea3a664f2'
auth_token = 'cb30e22c26adba34605f96dc66e8a381'
client = Client(account_sid, auth_token)


app = Flask(__name__)
app.debug = True
queue = []

@app.route('/', methods=['POST', 'GET'])

def request_handler():
	print("Getting Mined tx!!!")
	print(request)
	if request.method == 'POST':
		data = (request.json)
		print(data)
		if len(data['event']['activity'])==1:
			timestamp = data['createdAt']
			from_address = data['event']['activity'][0]['fromAddress']
			to_address = data['event']['activity'][0]['toAddress']
			blockNum =  data['event']['activity'][0]['blockNum']
			hash =  data['event']['activity'][0]['hash']


		else:
			for i in range(len(data['event']['activity'])):
				timestamp = data['createdAt']
				from_address = data['event']['activity'][i]['fromAddress']
				to_address = data['event']['activity'][i]['toAddress']
				blockNum =  data['event']['activity'][i]['blockNum']
				hash =  data['event']['activity'][i]['hash']


		print("DATA: ", data)
		print("HASH: ", hash)


		message = client.messages.create(body=" \n\n TX MINED! \n\n From: " + from_address + " \n\n To: " + to_address + " \n\n @#:" + blockNum + " \n Check tx: https://rinkeby.etherscan.io/tx/" +hash ,from_='+19705361926', to='+919557040676')
		print(message.sid)


	return ("Ok")
	#return webhook(session), 200

def run():
	app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
