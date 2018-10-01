import json
from pprint import pprint


def webhook(session):
    action = session['action']

    if action == 'event1':
        print('Получен запрос по событию event1')
        session['variable1'] = "значение1"

    elif action == 'event2':
        print('Получен запрос по событию event2')
        session['variable2'] = "значение2"

    elif action == 'event3':
        print('Получен запрос по событию event2')
        session['variable3'] = "значение3"

    else:
        print('Unknown action. Session data:')
        pprint(session)
        action = session['action']

        session['text'] = f'Вебхук получил запрос, но не смог обработать событие ' \
                          f'{action}. Вы можете добавить обработку этого события в webhook.'

        # Получить значение переменной text в Aimylogic можно в текстовом блоке через переменную $text

    return json.dumps(session)
