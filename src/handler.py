import json
import logging


def root_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel('INFO')
    logger.info('Got request: \n{}'.format(event))

    response = {
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*',
        },
        'statusCode': 200
    }

    try:
        response['body'] = json.dumps({
            'response_type': 'in_channel',
            'text': '호오, 저를 부르셨군요? {}'.format(event['body'])
        })
    except Exception as err:
        logger.setLevel('ERROR')
        logger.exception(err, exc_info=True)
        response['body'] = json.dumps({
            'response_type': 'ephemeral',
            'text': '뭔가 잘못됬습니다. 만든놈 @gyukebox 의 잘못이니 그에게 물어보세요.'
        })

    logger.setLevel('INFO')
    logger.info('Will respond with: \n{}'.format(response))

    return response


def display_commands(event, context):
    logger = logging.getLogger()
    logger.setLevel('INFO')
    logger.info('Got event: {}'.format(event))

    response = {
        'statusCode': 200,
        'body': 'https://github.com/depromeet/slackbot-management/docs 에서 확인하세요!'
    }
    logger.info('Will respond with: \n{}'.format(response))

    return response
