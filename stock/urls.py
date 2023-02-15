from django.contrib import admin
from django.urls import path, include

from .views import StockListView, StockIndexView, PresidentListView, StockFavoriteIndexView

urlpatterns = [
    path('index/', StockIndexView.as_view(), name='index'),
    path('telegram/list/', StockListView.as_view(), name='stock_list'),

    path('president/newsroom/fact/list/', PresidentListView.as_view(), name='presidentfact_list'),

    path('favorite/', StockFavoriteIndexView.as_view(), name='stock_favorite')
]
