from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, TemplateView

from .models import Stock


class StockIndexView(TemplateView):
    template_name = 'base.html'
class StockListView(ListView):
    model = Stock
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset()
