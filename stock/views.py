from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView

from .models import Stock


class IndexListView(ListView):
    model = Stock
    paginate_by = 10
    template_name = 'index.html'
