from django.contrib import admin
from django.urls import path, include

from .views import StockListView, StockIndexView, StockDetailView

urlpatterns = [
    path('', StockIndexView.as_view(), name='index'),
    path('list/', StockListView.as_view(), name='stock_list'),
    path('detail/<int:pk>/', StockDetailView.as_view(), name='stock_detail'),
]
