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
