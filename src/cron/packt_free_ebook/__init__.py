from src.cron.packt_free_ebook.utils import get_today_free_ebook
from src.utils.http import LambdaResponse, ExceptionHandler
from src.utils.logging import Logger
from src.utils.slack import SlackMessageWriter
from src import ASSETS_URL, BRANCH

ICON_DIR = 'assets/images/girl.png'

ICON_URL = '{}/{}/{}'.format(ASSETS_URL, BRANCH, ICON_DIR)


@LambdaResponse
@ExceptionHandler
@Logger
@SlackMessageWriter
def handler(event, context):
    ebook = get_today_free_ebook()
    slack_params = {
        'channel': '개발',
        'text': ebook,
        'unfurl_links': True,
        'unfurl_media': True,
        'username': '개발책 읽어주는 여자',
        'icon_url': ICON_URL
    }

    return slack_params
