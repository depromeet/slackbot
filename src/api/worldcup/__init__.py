from src.utils.http import LambdaResponse, ExceptionHandler
from src.utils.logging import Logger
from src.utils.slack import SlackMessageWriter
from src.api.worldcup.utils import generate_slack_message, fetch_worldcup_data
from src import ASSETS_URL, BRANCH


ICON_DIR = 'assets/images/football.png'

ICON_URL = '{}/{}/{}'.format(ASSETS_URL, BRANCH, ICON_DIR)


@LambdaResponse
@ExceptionHandler
@Logger
@SlackMessageWriter
def handler(event, context):
    world_cup_data = fetch_worldcup_data()
    slack_message = generate_slack_message(world_cup_data)
    slack_params = {
        'channel': 'general',
        'text': slack_message,
        'username': '축잘알',
        'icon_emoji': ':soccer:'
    }
    return slack_params
