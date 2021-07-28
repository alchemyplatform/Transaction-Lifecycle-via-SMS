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
    data = request.json
    print(data)

    #return webhook(session), 200
