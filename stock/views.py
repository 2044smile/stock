from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView, TemplateView, DetailView

from .models import Stock, PresidentFact


class StockIndexView(TemplateView):
    template_name = 'index.html'
class StockListView(ListView):
    model = Stock
    paginate_by = 7  # why not on the 10th?

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-date')
        return ordering

class PresidentListView(ListView):
    model = PresidentFact
    paginate_by = 10

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-date')
        return ordering

class StockFavoriteIndexView(TemplateView):
    template_name = 'stock_favorite.html'