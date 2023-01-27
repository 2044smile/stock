from django.contrib import admin
from django.urls import path, include

from .views import StockListView, StockIndexView

urlpatterns = [
    path('telegram/', StockIndexView.as_view(), name='index'),
    path('telegram/list/', StockListView.as_view(), name='stock_list'),

    # path('president/newsroom/'),
    # path('president/newsroom/list/'),
]
