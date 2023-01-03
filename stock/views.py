from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.generic import ListView

from .models import Stock


class IndexListView(ListView):
    paginate_by = 10
    model = Stock
    