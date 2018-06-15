import os
import requests
from src import ENV


URL = 'https://slack.com/api/chat.postMessage'

SLACK_BOT_TOKEN = os.environ['DPM_ADMIN_BOT_TOKEN']


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
            if ENV != 'production':
                params['channel'] = 'lab'

            params['token'] = SLACK_BOT_TOKEN
            slack_api_response = requests.post(URL, data=params).json()
            del params['token']

        response = {**params, **slack_api_response}
        return response
