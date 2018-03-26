import logging


def root_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel('INFO')
    logger.info('Got event: {}'.format(event))

    response = {
        'statusCode': 200,
        'body': 'https://github.com/depromeet/slackbot-management/wiki 에서 확인하세요!'
    }

    return response
