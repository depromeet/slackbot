import os
import requests


def parse_command(command):
    """
    @<USERID> 을 제외한 실제 명령어를 리턴해준디.
    :param command: 명령어. @<USERID> <텍스트> 형태로 나타난다.
    :return: @<USERID> 을 제외한 나머지 텍스트
    """
    actual_command = command[12:] if command[12] != ' ' else command[13:]
    return actual_command


def trigger_link(command):
    """
    command 를 받았을 때, request 를 보내야 하는 링크를 리턴해 줍니다.
    :param command:
    :return:
    """
    pass


def get_slack_api_response(url, **kwargs):
    """
    slack api 를 호출하여 응답을 리턴합니다.
    :param url: api 호출 url
    :return:
    """
    token = os.environ['DPM_ADMIN_BOT_TOKEN']

    print(url)
    print(kwargs)


if __name__ == '__main__':
    get_slack_api_response('url.com', token='token', channel='channel')
