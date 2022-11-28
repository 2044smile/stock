import os

from telethon import TelegramClient, events, sync


api_id = os.getenv('TELETHON_API_ID')
api_hash = os.getenv('TELETHON_API_HASH')
channel_username1 = 'corevalue'  # 가치투자클럽
channel_username2 = 'FastStockNews'  # 주식 급등일보, 급동테마 대장주 탐색기

with TelegramClient('Tim', api_id, api_hash) as client:
    # client.send_message('me', "Hello, myself!")
    channel_entity = client.get_entity(channel_username1)
    print(channel_entity)

    for message in client.get_messages(channel_username1, limit=10):
        print(message.message)
