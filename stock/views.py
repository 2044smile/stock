import asyncio
import os

from django.http.response import HttpResponse
from telethon.sync import TelegramClient
from django_telethon.sessions import DjangoSession
from django_telethon.models import App, ClientSession
from telethon.errors import SessionPasswordNeededError

from stock.models import Channel, Stock


def index(request):
    return HttpResponse("Hello World")


def telethon(request):
    API_ID = os.getenv('TELETHON_API_ID')
    API_HASH = os.getenv('TELETHON_API_HASH')

    channel_list = [os.getenv('channel_one'), os.getenv('channel_two')]
    news_link = []

    if request.method == "POST":
        app, is_created = App.objects.update_or_create(
            api_id=API_ID,
            api_hash=API_HASH
        )
        cs = ClientSession.objects.get(
            name="default",
        )
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        target_user = "default"
        telegram_client = TelegramClient(DjangoSession(client_session=cs), app.api_id, app.api_hash, loop=loop)
        telegram_client.connect()

        if not telegram_client.is_user_authorized():
            # phone = input('Enter your phone number: ')
            phone = os.getenv('TELETHON_PHONE')
            telegram_client.send_code_request(phone)
            # code = input('Enter the code you received: ')
            code = os.getenv('TELETHON_CODE')
            try:
                telegram_client.sign_in(phone, code)
            except SessionPasswordNeededError:
                password = input('Enter your password: ')
                telegram_client.sign_in(password=password)

        async def send():
            try:
                # await telegram_client.send_message(f'@{target_user}', 'Hello from django!')
                for channel in channel_list:
                    obj = Channel.objects.get(name=channel)
                    await telegram_client.get_entity(channel)
                    for message in await telegram_client.get_messages(channel, limit=10):
                        if message.media.webpage:
                            title = message.media.webpage.title
                            description = message.media.webpage.description
                            site_name = message.media.webpage.site_name
                            url = message.media.webpage.url
                            Stock.objects.update_or_create(
                                channel=obj,
                                title=title,
                                description=description,
                                site_name=site_name,
                                url=url,
                                date=message.date
                            )
                            news_link.append(message.message)
                        elif message.media == None:
                            """
                            시간외특징주 와 같이 링크나 추가 설명이 없을 경우

                            Ex)
                            12월 15일 시간외특징주\n
                            https://cafe.naver.com/stockhunters/99194\n Posts that are only open to members
                            12월 15일 52주 신고가 및 급등락주\n
                            https://cafe.naver.com/stockhunters/99195' You can see it even if you are not a member
                            """
                            pass
            except ValueError:
                print(f'Sorry no {target_user} user was found')

        with telegram_client:
            telegram_client.loop.run_until_complete(send())
        return HttpResponse(news_link)
