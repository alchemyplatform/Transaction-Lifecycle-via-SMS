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
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACe63c4c0358c719f1359e6e30a14dd6c9'
auth_token = 'fc160c7435aee7167038fe0e941dd0d9'
client = Client(account_sid, auth_token)


for i in range(3):
	try:
		ws = create_connection("wss://eth-rinkeby.alchemyapi.io/v2/Sj6KIf5jVp8VG7PC02ydEaMNhRu7VPy0")
		print("Connection made")
	except Exception as error:
		print('Connection Error: ' + repr(error))
		time.sleep(3)
	else:
		break

ws.send(json.dumps({"jsonrpc":"2.0","method":"eth_subscribe","params":["alchemy_filteredNewFullPendingTransactions", {"address": "0xcF3A24407aae7c87bd800c47928C5F20Cd4764D2"}],"id":1}))
print("JSON eth_subscribe sent")

while True:
    try:
        result = ws.recv()
        result = json.loads(result)
        from_address = (result["params"]["result"]["from"])
        to_address = (result["params"]["result"]["to"])

        try:
            hash = (result["params"]["result"]["hash"])
        except:
            hash = None

		print("from:", from_address)
		print("to:", to_address)
		print("hash: ", string(hash))

		message = client.messages \
		                .create(
		                     body="\n PENDING TRANSACTION! \n From: " + from_address + " \n To: " + to_address + "\n  @tx:" + hash,
		                     from_='+14435267244',
		                     to='+14158130071'
		                 )
		print(message.sid)

				# data to be sent to api
		#data = {'local':'true','hash':hash}

		#API_ENDPOINT= "https://fathomless-journey-71013.herokuapp.com/"

		# sending post request and saving response as response object
		#r = requests.post(url = API_ENDPOINT, data = data)


	except KeyError as error:
		print("Check JSON params for parsing")

	except Exception as error:
		print('JSON Error: ' + repr(error))
		time.sleep(1)

ws.close()
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

        message = client.messages.create(body=" \n TRANSACTION MINED! \n From: " + from_address + " \n To: " + to_address + " \n @#:" + blockNum + " \n CHECK HERE- https://rinkeby.etherscan.io/tx/" +hash ,from_='+14435267244', to='+14158130071')
        print(message.sid)

    return ("Ok")
    #return webhook(session), 200

def run():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
