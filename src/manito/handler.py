import os
import json
import logging
import requests
from urllib.parse import parse_qs

from src.manito.utils import find_manito, parse_extra_commands


def slash_command_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel('INFO')
    logger.info('Got request: \n{}'.format(event))

    response = {
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
        'statusCode': 200,
        'body': {
            'response_type': 'ephemeral'
        }
    }

    parsed_qs = parse_qs(event['body'])
    extra_text = parse_extra_commands(parsed_qs)
    requested_user_id = parsed_qs['user_id'][0]

    if extra_text is None:
        token = os.environ['DPM_ADMIN_BOT_TOKEN']
        params = {
            'token': token,
            'user': requested_user_id,
        }

        api_response = requests.get(
            'https://slack.com/api/users.info', params=params).json()

        if api_response['ok'] is False:
            logger.setLevel('ERROR')
            logger.error('Slack API Responded with: {}'.format(api_response))
            response['body']['text'] = '뭔가 문제가 생겼습니다. 만든놈 @gyukebox 의 잘못이니 그에게 물어보세요.'
        else:
            logger.info('Slack API Responded with: \n{}'.format(api_response))
            requested_user_name = api_response['user']['real_name']
            try:
                manito = find_manito(requested_user_id)
                response['body']['text'] = '{} 님의 마니또는 {} 님 입니다!'.format(
                    requested_user_name, manito)
            except (FileNotFoundError, KeyError) as err:
                logger.setLevel('ERROR')
                logger.exception(err, exc_info=True)
                response['body']['text'] = '뭔가 문제가 생겼습니다. 만든놈 @gyukebox 의 잘못이니 그에게 물어보세요.'

    elif extra_text[0] == '미션':
        response['body'] = {
            'response_type': 'in_channel',
            'text': '이번주 마니또 미션: 마니또에게 (어떤 형태로든)인사하기!'
        }

    else:
        response['body']['text'] = '해당 명령어는 아직 준비되지 않았습니다. 만든놈 @gyukebox 의 게으름을 욕하세요.'

    logger.setLevel('INFO')
    logger.info('Will respond with: \n{}'.format(response))

    response['body'] = json.dumps(response['body'])
    return response
