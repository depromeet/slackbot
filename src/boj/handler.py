import os
import logging
import random
import requests


def boj_problem_fetcher(event, context):
    logger = logging.getLogger()
    logger.setLevel('INFO')
    logger.info('Got request: \n{}\n'.format(event))

    response = {
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    min_problem_number = 1000
    max_problem_number = 15688
    random_problem_number = random.randint(min_problem_number, max_problem_number)
    url = 'https://www.acmicpc.net/problem/{}'.format(random_problem_number)

    logger.info('{} 에서 문제를 가져왔습니다. \n'.format(url))

    token = os.environ['DPM_ADMIN_BOT_TOKEN']
    params = {
        'token': token,
        'channel': 'algo',
        'text': '(베타) 오늘의 문제 : {}'.format(url)
    }

    api_response = requests.post('https://slack.com/api/chat.postMessage', data=params).json()

    if api_response['ok'] is True:
        response['statusCode'] = 200
        response['body'] = params['text']
    else:
        response['statusCode'] = 400
        response['body'] = api_response['error']

    logger.info('다음과 같이 응답합니다 : \n{}'.format(response))

    return response
