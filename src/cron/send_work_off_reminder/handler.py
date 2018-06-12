from src.utils.http import LambdaResponse, ExceptionHandler
from src.utils.logging import Logger
from src.utils.slack import SlackMessageWriter


@LambdaResponse
@SlackMessageWriter
@ExceptionHandler
@Logger
def handler(event, context):
    return {
        'channel': 'lab',
        'text': '삐빅. 퇴근시간입니다.'
    }
