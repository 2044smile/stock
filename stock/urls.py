from django.contrib import admin
from django.urls import path, include

from .views import StockListView, StockIndexView

urlpatterns = [
    path('', StockIndexView.as_view()),
    path('list/', StockListView.as_view()),
]
