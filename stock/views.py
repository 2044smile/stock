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
