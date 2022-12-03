from django.contrib import admin
from django.urls import path, include

from .views import index, telethon

urlpatterns = [
    path('', index),
    path('telethon/', telethon)
]
