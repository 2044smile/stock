import asyncio
import os
import sys

from django.shortcuts import render
from django.http.response import HttpResponse
from telethon.sync import TelegramClient
from django_telethon.sessions import DjangoSession
from django_telethon.models import App, ClientSession
from telethon.errors import SessionPasswordNeededError


def index(request):
    return HttpResponse("Hello World")


def telethon(request):
    API_ID = os.getenv('TELETHON_API_ID')
    API_HASH = os.getenv('TELETHON_API_HASH')

    if request.method == "POST":
        print('Start')
        app, is_created = App.objects.update_or_create(
            api_id=API_ID,
            api_hash=API_HASH
        )
        print(app)
        cs = ClientSession.objects.get(
            name="default",
        )
        print(cs)
        target_user = "default"
        telegram_client = TelegramClient(DjangoSession(client_session=cs), app.api_id, app.api_hash)
        telegram_client.connect()

        if not telegram_client.is_user_authorized():
            phone = input('Enter your phone number: ')
            telegram_client.send_code_request(phone)
            code = input('Enter the code you received: ')
            try:
                telegram_client.sign_in(phone, code)
            except SessionPasswordNeededError:
                password = input('Enter your password: ')
                telegram_client.sign_in(password=password)

        async def send():
            try:
                await telegram_client.send_message(f'@{target_user}', 'Hello from django!')
            except ValueError:
                print(f'Sorry no {target_user} user was found')

        with telegram_client:
            telegram_client.loop.run_until_complete(send())
        return HttpResponse('addChannel')
