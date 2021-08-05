# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask import request
from webhook import webhook
from twilio.rest import Client
import json, time
import requests
from websocket import create_connection
import os
import pickle

from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACe63c4c0358c719f1359e6e30a14dd6c9'
auth_token = 'fc160c7435aee7167038fe0e941dd0d9'
client = Client(account_sid, auth_token)


app = Flask(__name__)
app.debug = True
queue = []

@app.route('/', methods=['POST', 'GET'])

def request_handler():

	if request.method == 'POST':
		data = (request.json)

		print(data)
		print("")

		if len(data['activity'])==1:
			timestamp = data['timestamp']
			from_address = data['activity'][0]['fromAddress']
			to_address = data['activity'][0]['toAddress']
			blockNum =  data['activity'][0]['blockNum']
			hash =  data['activity'][0]['hash']


		else:
			for i in range(len(data['activity'])):
				timestamp = data['timestamp']
				from_address = data['activity'][i]['fromAddress']
				to_address = data['activity'][i]['toAddress']
				blockNum =  data['activity'][i]['blockNum']
				hash =  data['activity'][i]['hash']

		with open("data.p", "wb") as f:
		    data = pickle.load(f)

		print("DATA: ", data)
		print("HASH: ", hash)


		if hash in data:
			data.remove(hash)
			pickle.dump(data,f)

			message = client.messages.create(body=" \n TRANSACTION MINED! \n From: " + from_address + " \n To: " + to_address + " \n @#:" + blockNum + " \n CHECK HERE- https://rinkeby.etherscan.io/tx/" +hash ,from_='+14435267244', to='+14158130071')
			print(message.sid)


	return ("Ok")
	#return webhook(session), 200

def run():
	app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
	port = int(os.environ.get("PORT", 5000))
	app.run(host='0.0.0.0', port=port)
