from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, TemplateView, DetailView

from .models import Stock


class StockIndexView(TemplateView):
    template_name = 'index.html'
class StockListView(ListView):
    model = Stock
    paginate_by = 10
    ordering = ['-date']

class StockDetailView(DetailView):
    model = Stock
