import os
import json


def find_manito(userid):
    """
    userid 의 슬랙 아이디를 가진 사람의 마니또를 찾아줍니다
    :param userid: 슬랙 유저 아이디
    :return: 마니또 이름
    """
    path = os.path.dirname(__file__)
    with open(path + '/manito.json', encoding='utf8') as file:
        manito_list = json.load(file)
        return manito_list[userid]


def parse_extra_commands(query_string):
    try:
        return query_string['text']
    except KeyError:
        return None
