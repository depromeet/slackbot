import os
import requests


TOKEN = os.environ['DPM_ADMIN_BOT_TOKEN']

URL = 'https://slack.com/api/chat.postMessage'


class SlackMessageWriter:
    """
    Decorator class for cron handlers.
    Writes to slack with parameters returned by the handler.
    """

    def __init__(self, handler):
        self.handler = handler

    def __call__(self, event, context):
        params = self.handler(event, context)

        if 'channel' in params and 'text' in params:
            params['token'] = TOKEN
            requests.post(URL, data=params)
            del params['token']

        return params
