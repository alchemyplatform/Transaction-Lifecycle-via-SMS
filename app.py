# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask import request
from webhook import webhook

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['POST', 'GET'])

queue = []
def request_handler():

    if request.method == 'POST':
        data = (request.json)

        print(data)
        print("")

        try:
            if (data['local'] == 'true'):
                queue.append(data['hash'])
                print("QUEUE UPDATED")
                print(queue)

        except:

            for i in range(len(data['activity']))
                if data['activity'][i]['hash'] in queue:
                    timestamp = data['timestamp']
                    from_address = data['activity'][i]['fromAddress']
                    to_address = data['activity'][i]['toAddress']
                    blockNum =  data['activity'][i]['blockNum']
                    queue.remove(data['activity'][i]['hash'])
                    print("FOUND")

    return ("Ok")
    #return webhook(session), 200

def run():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
