import os
import json
import logging
import requests
from urllib.parse import parse_qs


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
    else:
        logger.info(api_response)
        requested_user_name = api_response['user']['real_name']
        with open('manito.json', encoding='utf8') as file:
            manito_list = json.load(file)
            try:
                manito = manito_list[requested_user_id]
                response = '\n{} 님의 마니또는 {} 님 입니다!'.format(
                    requested_user_name, manito)
                return {
                    'statusCode': 200,
                    'body': response
                }
            except KeyError:
                return {
                    'statusCode': 200,
                    'body': '뭔가 문제가 생겼습니다. 만든놈 @gyukebox 잘못이니 물어보세요.'
                }
