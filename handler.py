# -*- coding: utf8 -*-

import os
import json
from datetime import datetime, timedelta
from slackclient import SlackClient


def archive_inactive_channels(event, context):
    oauth_token = os.environ['DPM_ADMIN_OAUTH_TOKEN']
    client = SlackClient(oauth_token)

    all_channels_id = [channel['id'] for channel in client.api_call(
        'channels.list', exclude_archived=True, exclude_members=True)['channels']]

    histories = [datetime.fromtimestamp(float(history['messages'][0]['ts']))
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


def send_off_work_reminder(event, context):
    oauth_token = os.environ['DPM_ADMIN_BOT_TOKEN']
    client = SlackClient(oauth_token)

    response = client.api_call('chat.postMessage', channel='#lab', text='테스트 메시지 from remote')

    if response['ok'] is True:
        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    else:
        return {
            'statusCode': 500,
            'body': response['error']
        }
