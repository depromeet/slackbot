import os
import json
import logging
import requests


def send_off_work_reminder(event, context):
    logger = logging.getLogger()
    logger.setLevel('INFO')
    logger.info('Got request: {}'.format(event))

    bot_token = os.environ['DPM_ADMIN_BOT_TOKEN']
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    body = {
        'token': bot_token,
        'channel': '#general',
        'text': '삐빅. 퇴근시간입니다.'
    }

    slack_api_response = requests.post(
        'https://slack.com/api/chat.postMessage', data=body, headers=headers).json()
    response = {
        'body': json.dumps(slack_api_response)
    }

    if slack_api_response['ok'] is True:
        response['statusCode'] = 200
        logger.info('Got Slack API Response: {}'.format(slack_api_response))
    else:
        response['statusCode'] = 500
        logger.error('Error on Slack API Response: {}'.format(
            slack_api_response))

    return response
