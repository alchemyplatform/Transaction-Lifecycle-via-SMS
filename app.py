# -*- coding: utf-8 -*-
import os
from flask import Flask
from flask import request
from webhook import webhook

app = Flask(__name__)
app.debug = True


@app.route('/', methods=['POST', 'GET'])
def request_handler():
    if request.method == 'GET':
        href = '<a href="http://aimylogic.com" ' \
               'target="_blank">aimylogic.com</a> '
        more = '<a href="https://github.com/aimylogic/python-webhook" ' \
               'target="_blank">More</a> '

        return f'<p>Copy this URL and paste it in your bot settings.' \
               f'{more}', 200

    session = request.json

    return webhook(session), 200

def run():
    print(' * Use ngrok to tunnel your localhost to Aimylogic.'
          '\n * ./ngrok http 5000 || ngrok.exe http 5000 (windows)'
          '\n * This will generate temporary URL in terminal.  Copy it and paste into the field named "Webhook for tests" in your bot\'s settings. '
          'All requests to your webhook will go to your local machine while you test your bot scenario via a test widget on Aimylogic.')
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
