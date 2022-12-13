import os
import sys
sys.path.append('.')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from telethon.sync import TelegramClient


API_ID = os.getenv('TELETHON_API_ID')
API_HASH = os.getenv('TELETHON_API_HASH')
channel_list = ['corevalue', 'FastStockNews']
# channel_username1 = 'corevalue'  # 가치투자클럽
# channel_username2 = 'FastStockNews'  # 주식 급등일보, 급동테마 대장주 탐색기

with TelegramClient('Tim', API_ID, API_HASH) as client:
    # client.send_message('me', "Hello, myself!")
    for cl in channel_list:
        print(cl)
        channel_entity = client.get_entity(cl)
        print(channel_entity)
        for message in client.get_messages(cl, limit=10):
            print(message.message)
# from telethon.sync import TelegramClient
# from django_telethon.sessions import DjangoSession
# from django_telethon.models import App, ClientSession
# from telethon.errors import SessionPasswordNeededError

# # Use your own values from my.telegram.org
# API_ID = os.getenv('TELETHON_API_ID')
# API_HASH = os.getenv('TELETHON_API_HASH')

# app, is_created = App.objects.update_or_create(
#     api_id=API_ID,
#     api_hash=API_HASH
# )
# cs = ClientSession.objects.get(
#     name="default",
# )
# telegram_client = TelegramClient(DjangoSession(client_session=cs), app.api_id, app.api_hash)
# telegram_client.connect()

# if not telegram_client.is_user_authorized():
#     phone = input('Enter your phone number: ')
#     telegram_client.send_code_request(phone)
#     code = input('Enter the code you received: ')
#     try:
#         telegram_client.sign_in(phone, code)
#     except SessionPasswordNeededError:
#         password = input('Enter your password: ')
#         telegram_client.sign_in(password=password)