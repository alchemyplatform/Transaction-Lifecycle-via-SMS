import json
from pprint import pprint


def webhook(session):
    action = session['action']

    if action == 'event1':
        print('Received request from event1 action')
        session['variable1'] = "value1"

    elif action == 'event2':
        print('Received request from event2 action')
        session['variable2'] = "value2"

    elif action == 'event3':
        print('Received request from event3 action')
        session['variable3'] = "value3"

    else:
        print('Unknown action. Session data:')
        pprint(session)
        action = session['action']

        session['text'] = f'Webhook recieved a request, but couldn\'t handle the action' \
                          f'{action}.'

    return json.dumps(session)
