import os, time
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

import asyncio

from telethon.sync import TelegramClient
from django_telethon.sessions import DjangoSession
from django_telethon.models import App, ClientSession
from telethon.errors import SessionPasswordNeededError

from stock.models import Channel, Stock
from apscheduler.schedulers.background import BackgroundScheduler
from django.core.exceptions import ObjectDoesNotExist


def get_telethon():
    API_ID = os.getenv('TELETHON_API_ID')
    API_HASH = os.getenv('TELETHON_API_HASH')

    channel_list = [os.getenv('channel_one'), os.getenv('channel_two')]
    success_news_link = []
    fail_news_link = []

    # if request.method == "POST":
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
                # await telegram_client.download_media(message.media, "save path")

                for message in await telegram_client.get_messages(channel, limit=20):
                    print()
                    print(message)
                    print()
                    try:
                        if message.media.webpage:
                            print('True')

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
                            success_news_link.append(message.media.webpage.url)
                            print(success_news_link)
                    except AttributeError:
                        print('There are many difficult problems')
                        # print('False')
                        # """
                        # ?????????????????? ??? ?????? ????????? ?????? ????????? ?????? ??????

                        # Ex by msg_list)
                        # 12??? 15??? ??????????????????\n  [0]
                        # https://cafe.naver.com/stockhunters/99194\n Posts that are only open to members [1]
                        # 12??? 15??? 52??? ????????? ??? ????????????\n  [2]
                        # https://cafe.naver.com/stockhunters/99195' You can see it even if you are not a member  [3]
                        # """
                        # msg_list = message.message.split('\n')
                        # if len(msg_list) != 3:
                        #     print(msg_list)
                        #     break

                        # title = msg_list[0]
                        # description = msg_list[2]
                        # url = msg_list[3]

                        # Stock.objects.update_or_create(
                        #     channel=obj,
                        #     title=title,
                        #     description=description,
                        #     site_name="????????? ?????????",
                        #     url=url,  # Naver Cafe must sign up in the case of 'msg_list[1]'
                        #     date=message.date
                        # )
                        # fail_news_link.append(message.message)
                        # print(fail_news_link)
        except ValueError:
            print(f'Sorry no {target_user} user was found')

    with telegram_client:
        telegram_client.loop.run_until_complete(send())
    return success_news_link


if __name__ == '__main__':
    sched = BackgroundScheduler(timezone="Asia/Seoul")
    sched.start()

    # while True:
        # @sched.scheduled_job('cron', hour='15', minute='8')
        # def job_am():
        #     print('15,8')
    get_telethon()
