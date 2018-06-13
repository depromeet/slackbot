from src.cron.packt_free_ebook.utils import get_today_free_ebook
from src.utils.http import LambdaResponse, ExceptionHandler
from src.utils.logging import Logger
from src.utils.slack import SlackMessageWriter


@LambdaResponse
@SlackMessageWriter
@ExceptionHandler
@Logger
def handler(event, context):
    ebook = get_today_free_ebook()
    slack_params = {
        'channel': '개발',
        'text': ebook,
        'unfurl_links': True,
        'unfurl_media': True,
        'username': '개발책 읽어주는 여자'
    }

    return slack_params
