import os
import requests


def test_send_message_handler():
    bot_token = os.environ['DPM_ADMIN_BOT_TOKEN']
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    body = {
        'token': bot_token,
        'channel': '#lab',
        'text': '메시지 보내기 테스트'
    }

    slack_api_response = requests.post('https://slack.com/api/chat.postMessage', data=body, headers=headers)

    response = {
        'statusCode': 200 if slack_api_response.json()['ok'] is True else 500,
        'body': slack_api_response.text
    }
    return response
