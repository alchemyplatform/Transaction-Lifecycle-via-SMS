# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask import request
from webhook import webhook

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['POST', 'GET'])
def request_handler():
    if request.method == 'POST':
        print(requst.json)

    //return webhook(session), 200

def run():
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
