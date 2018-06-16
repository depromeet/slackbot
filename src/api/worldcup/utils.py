import datetime
import requests

TEAMS = {
    'RUS': '러시아',
    'KSA': '사우디아라비아',
    'URU': '우루과이',
    'EGY': '이집트',
    'POR': '포르투갈',
    'ESP': '스페인',
    'IRN': '이란',
    'MAR': '모로코',
    'FRA': '프랑스',
    'AUS': '호주',
    'PER': '페루',
    'DEN': '덴마크',
    'ARG': '아르헨티나',
    'ISL': '아이슬란드',
    'CRO': '크로아티아',
    'NGA': '나이지리아',
    'BRA': '브라질',
    'SUI': '스위스',
    'CRC': '코스타리카',
    'SRB': '세르비아',
    'GER': '독일',
    'MEX': '멕시코',
    'SWE': '스웨덴',
    'KOR': '대한민국',
    'BEL': '벨기에',
    'PAN': '파나마',
    'TUN': '튀니지',
    'ENG': '잉글랜드',
    'POL': '폴란드',
    'SEN': '세네갈',
    'COL': '콜롬비아',
    'JPN': '일본',
}

KST_UTC_DIFFERENCE = 9

TODAY = datetime.date.today()


def calculate_korean_datetime(local_date, local_time, difference):
    year, month, date = local_date.split('-')
    year, month, date = int(year), int(month), int(date)

    hour, minute, _ = local_time.split(':')
    hour, minute = int(hour) + difference, int(minute)

    if hour >= 24:
        hour -= 24
        date += 1
    if date == 31:
        month += 1
        date = 1

    return datetime.datetime(year, month, date, hour, minute)


def generate_match_data(match, matchtime):
    return {
        'datetime': str(matchtime),
        'status': match['status'],
        'home': {
            'team': TEAMS[match['home_team']['code']],
            'score': match['home_team']['goals']
        },
        'away': {
            'team': TEAMS[match['away_team']['code']],
            'score': match['away_team']['goals']
        }
    }


def fetch_worldcup_data():
    URL = 'http://worldcup.sfg.io/matches'
    response = requests.get(URL).json()
    matches = [match for match in response]

    yesterday_matches = []
    today_matches = []
    tomorrow_matches = []

    for match in matches:
        local_date, local_time = match['datetime'].split('T')
        local_time = local_time.split('.')[0]

        matchtime_in_korean = calculate_korean_datetime(
            local_date,
            local_time,
            KST_UTC_DIFFERENCE
        )

        date_difference = (matchtime_in_korean.date() - TODAY).days

        if date_difference == 0:
            today_matches.append(
                generate_match_data(
                    match,
                    matchtime_in_korean
                )
            )
        elif date_difference == -1:
            yesterday_matches.append(
                generate_match_data(
                    match,
                    matchtime_in_korean
                )
            )
        elif date_difference == 1:
            tomorrow_matches.append(
                generate_match_data(
                    match,
                    matchtime_in_korean
                )
            )

    return {
        'yesterday': yesterday_matches,
        'today': today_matches,
        'tomorrow': tomorrow_matches
    }


def generate_match_result(match):
    sentence = '> '
    home = match['home']
    away = match['away']
    finished = match['status'] == 'completed'

    if not finished:
        time = match['datetime'].split(' ')[1][:5]
        sentence += '{} vs {} ({})'.format(home['team'], away['team'], time)
    else:
        if home['score'] > away['score']:
            sentence += '*{} {}* : {} {}'.format(
                home['team'],
                home['score'],
                away['score'],
                away['team']
            )
        elif home['score'] < away['score']:
            sentence += '{} {} : *{} {}*'.format(
                home['team'],
                home['score'],
                away['score'],
                away['team']
            )
        else:
            sentence += '{} {} : {} {}'.format(
                home['team'],
                home['score'],
                away['score'],
                away['team']
            )
    return sentence


def generate_slack_message(data):
    sentence = ':soccer: 오늘의 월드컵 정보 :soccer: \n\n'
    yesterday_result = [
        generate_match_result(match) for match in data['yesterday']
    ]
    today_result = [
        generate_match_result(match) for match in data['today']
    ]
    tomorrow_result = [
        generate_match_result(match) for match in data['tomorrow']
    ]

    sentence += '*어제의 경기* \n'
    yesterday_sentence = ''
    for result in yesterday_result:
        yesterday_sentence += (result + '\n')
    sentence += yesterday_sentence

    sentence += '\n*오늘의 경기* \n'
    today_sentence = ''
    for result in today_result:
        today_sentence += (result + '\n')
    sentence += today_sentence

    sentence += '\n*내일의 경기* \n'
    tomorrow_sentence = ''
    for result in tomorrow_result:
        tomorrow_sentence += (result + '\n')
    sentence += tomorrow_sentence

    return sentence
