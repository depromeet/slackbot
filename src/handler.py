import json
import logging
import os

import requests
from src.utils import parse_command


def root_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel('INFO')
    logger.info(event)
    response = {'statusCode': 200}

    if event['httpMethod'] == 'POST':
        body = json.loads(event['body'], encoding='utf8')['event']
        logger.info(body)

        # TODO parse command and set appropriate request url
        command = parse_command(body['text'])

        bot_token = os.environ['DPM_ADMIN_BOT_TOKEN']
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        body = {
            'token': bot_token,
            'channel': body['channel'],
            'text': '오호, 저를 부르셨군요? 입력하신 명령어 : {}'.format(command)
        }

        api_response = requests.post(
            'https://slack.com/api/chat.postMessage', data=body, headers=headers).json()
        if api_response['ok'] is True:
            logger.info('Slack API Response: \n{}'.format(
                json.dumps(api_response, ensure_ascii=False)))
        else:
            logger.setLevel('ERROR')
            logger.error('Error on Slack API Response: \n{}'.format(
                json.dumps(api_response, ensure_ascii=False)))

        # temp
        response['body'] = json.dumps({
            'ok': True,
            'message': 'Successfully responded!'
        })
    else:
        response['body'] = '디프만 슬랙에 봇이 언급되면 불리는 api 입니다. 이 메시지는 api 를 GET 요청으로 호출했을 때 나타납니다.'

    logger.setLevel('INFO')
    logger.info('Will respond with: \n{} \n'.format(response))
    return response


def display_commands(event, context):
    logger = logging.getLogger()
    logger.setLevel('INFO')
    logger.info('Got event: {}'.format(event))

    response = {
        'statusCode': 200,
        'body': 'https://github.com/depromeet/slackbot-management/wiki 에서 확인하세요!'
    }

    return response
