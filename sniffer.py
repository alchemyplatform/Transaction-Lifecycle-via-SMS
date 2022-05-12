import json, time
import requests
from websocket import create_connection
import os
from twilio.rest import Client
import pickle

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC6ad5ff1f49211e3f0a635dbea3a664f2'
auth_token = 'cb30e22c26adba34605f96dc66e8a381'
client = Client(account_sid, auth_token)
ALCHEMY_KEY = 'aPT9cd5pETtsGl6vbCpWYsCJrAWhzX1k'

for i in range(3):
	try:
		ws = create_connection("wss://eth-rinkeby.alchemyapi.io/v2/"+ALCHEMY_KEY)
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
		hash = (result["params"]["result"]["hash"])
		blockHash = (result["params"]["result"]["blockNumber"])

		#data = pickle.load( open( "data.p", "rb" ) )
		#data.add(hash)
		#pickle.dump(data, open( "data.p", "wb" ) )

		print("from:", from_address)
		print("to:", to_address)
		print("hash: ", hash)
		print("blockHash: ", blockHash)

		message = client.messages \
						.create(
							 body="\n \n PENDING TX! \n\n From: " + from_address + " \n\n To: " + to_address + "\n\n  @tx:" + hash,
							 from_='+19705361926',
							 to='+919557040676'
						 )
		print("Checking for pending txns!!!!!!!")
		print(message.sid)

		#data = pickle.load( open( "data.p", "rb" ) )
		#print(data)


	except KeyError as error:
		print("Check JSON params for parsing")

	except Exception as error:
		print('JSON Error: ' + repr(error))
		time.sleep(1)

ws.close()
