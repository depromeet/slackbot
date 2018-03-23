# -*- coding: utf8 -*-

import os
import json
from datetime import datetime, timedelta
from slackclient import SlackClient


def hello(event, context):
    body = {
        "message": "디프만 슬랙 관리자 슬랙봇!",
        "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response


def archive_inactive_channels(event, context):
    oauth_token = os.environ['DPM_ADMIN_OAUTH_TOKEN']
    client = SlackClient(oauth_token)

    all_channels_id = [channel['id'] for channel in client.api_call(
        'channels.list', exclude_archived=True, exclude_members=True)['channels']]

    histories = [datetime.fromtimestamp(float(history['messages'][2]['ts']))
                 for history in [client.api_call('channels.history', channel=channel_id)
                                 for channel_id in all_channels_id]]

    now = datetime.now()
    one_month = timedelta(weeks=4)

    archived_count = 0

    total = len(all_channels_id)
    for i in range(total):
        if histories[i] <= now - one_month:
            client.api_call('channels.archive', channel=all_channels_id[i])
            archived_count += 1

    return {
        'statusCode': 200,
        'body': 'Successfully archived {} channels'.format(archived_count)
    }