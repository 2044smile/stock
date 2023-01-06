from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView

from .models import Stock


class StockListView(ListView):
    model = Stock
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset()
