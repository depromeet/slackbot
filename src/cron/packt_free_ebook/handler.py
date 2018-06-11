import os
import logging
import requests


def handler(event, context):
    logger = logging.getLogger()
    logger.setLevel('INFO')
    logger.info('Got request : \n{}'.format(event))

    response = {
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    # TODO get to packtpub
    url = ''

    # TODO scrape ebook title(asynchronus way if possible)
    ebook_title = ''

    logger.info('오늘의 무료책 제목 : {}\n'.format(ebook_title))

    token = os.environ['DPM_ADMIN_BOT_TOKEN']
    params = {
        'token': token,
        'channel': '개발',
        'text': '(베타) 오늘의 무료책 : {}\n{}'.format(ebook_title, url)
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
