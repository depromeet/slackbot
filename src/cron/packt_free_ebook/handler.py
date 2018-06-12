import os
import logging
import requests
from src.cron.packt_free_ebook.utils import get_today_free_ebook


def handler(event, context):
    logger = logging.getLogger()
    logger.setLevel('INFO')

    response = {}

    token = os.environ['DPM_ADMIN_BOT_TOKEN']
    params = {
        'token': token,
        'channel': '개발',
        'text': get_today_free_ebook(),
        'unfurl_links': True,
        'unfurl_media': True,
        'username': '개발책 읽어주는 여자',
    }

    slack_api_response = requests.post(
        'https://slack.com/api/chat.postMessage',
        data=params
    )
    slack_api_response = slack_api_response.json()

    if slack_api_response['ok'] is True:
        response['statusCode'] = 200,
        response['body'] = params['text']
    else:
        response['statusCode'] = 400
        response['body'] = slack_api_response['error']

    logger.info('다음과 같이 응답합니다 : \n{}'.format(response))

    return response
