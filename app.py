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
        more = '<a href="https://github.com/Denire/python-webhook" ' \
               'target="_blank">Подробнее</a> '

        return f'<p>Укажите этот URL в настройках вашего бота на {href}</p>' \
               f'{more}', 200

    session = request.json

    return webhook(session), 200

def run():
    print('test restart. One more restart')
    print(' * Вы можете использовать ngrok, чтобы дать возможность серверу Aimylogic увидеть ваш вебхук.'
          '\n * ./ngrok http 5000 || ngrok.exe http 5000 (windows)'
          '\n * Вы увидите временный URL для вашего вебхука в консоли. Скопируйте его и вставьте в настройках вашего '
          'бота на aimylogic.com в поле "Вебхук для тестов". После этого, когда вы будете тестировать вашего бота в '
          'тестовом виджете, все запросы будут приходить к серверу на вашей машине.')
    app.run(host='0.0.0.0', port=5000)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
