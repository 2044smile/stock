from django.contrib import admin
from django.urls import path, include

from .views import StockListView

urlpatterns = [
    path('list/', StockListView.as_view()),
]
