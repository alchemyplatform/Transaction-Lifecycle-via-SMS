import json, time
import requests
from websocket import create_connection
import os
from twilio.rest import Client
import pickle

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = '<TWILIO SID>'
auth_token = '<TWILIO AUTH TOKEN>'
client = Client(account_sid, auth_token)
ALCHEMY_KEY = '<ALCHEMY KEY>'

for i in range(3):
	try:
		ws = create_connection("wss://eth-rinkeby.alchemyapi.io/v2/"+ALCHEMY_KEY)
		print("Connection made")
	except Exception as error:
		print('Connection Error: ' + repr(error))
		time.sleep(3)
	else:
		break

ws.send(json.dumps({"jsonrpc":"2.0","method":"eth_subscribe","params":["alchemy_filteredNewFullPendingTransactions", {"address": "0xccD3dd576e715b0E060169e16C39Cd7E6eEdeF51"}],"id":1}))
print("JSON eth_subscribe sent")

while True:
	try:
		result = ws.recv()
		result = json.loads(result)
		from_address = (result["params"]["result"]["from"])
		to_address = (result["params"]["result"]["to"])
		hash = (result["params"]["result"]["hash"])
		blockHash = (result["params"]["result"]["blockNumber"])

		#data = pickle.load( open( "data.p", "rb" ) )
		#data.add(hash)
		#pickle.dump(data, open( "data.p", "wb" ) )

		print("from:", from_address)
		print("to:", to_address)
		print("hash: ", hash)
		print("blockHash: ", blockHash)

		print("Send Twilio SMS for pending transaction!")
		message = client.messages \
						.create(
							 body="\n \n PENDING TX! \n\n From: " + from_address + " \n\n To: " + to_address + "\n\n  @tx:" + hash,
							 from_='+14435267244',
							 to='+14158130071'
						 )

		print(message.sid)

		#data = pickle.load( open( "data.p", "rb" ) )
		#print(data)


	except KeyError as error:
		print("Check JSON params for parsing")

	except Exception as error:
		print('JSON Error: ' + repr(error))
		time.sleep(1)

ws.close()
