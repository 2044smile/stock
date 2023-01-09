from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, TemplateView

from .models import Stock


class StockIndexView(TemplateView):
    template_name = 'base.html'
class StockListView(ListView):
    model = Stock
    paginate_by = 10
    ordering = ['-date']

    def get_queryset(self):
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
