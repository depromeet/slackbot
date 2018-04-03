import os
import logging
import requests
from urllib.parse import parse_qs
from src.manito.utills import find_users_manito


def slash_command_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel('INFO')

    parsed_qs = parse_qs(event['body'])
    requested_user_id = parsed_qs['user_id'][0]
    token = os.environ['DPM_ADMIN_BOT_TOKEN']

    params = {
        'token': token,
        'user': requested_user_id,
    }

    api_response = requests.get(
        'https://slack.com/api/users.info', params=params).json()

    if api_response['ok'] is False:
        logger.setLevel('ERROR')
        logger.error(api_response)
        return {
            'statusCode': 200,
            'body': '뭔가 문제가 생겼습니다. 만든놈 @gyukebox 의 잘못이니 물어보세요.'
        }

    logger.info(api_response)
    requested_user_name = api_response['user']['real_name']
    manito = find_users_manito(userid=requested_user_id)
    if manito is None:
        return {
            'statusCode': 200,
            'body': '뭔가 문제가 생겼습니다. 만든놈 @gyukebox 의 잘못이니 물어보세요.'
        }
    else:
        return {
            'statusCode': 200,
            'body': '{} 님의 마니또는 {} 님 입니다!'.format(requested_user_name, manito)
        }
