from django.shortcuts import render

from .models import Stock


def index(request):
    stock_list = Stock.objects.all()
    return render(request, 'index.html', {'stock_list': stock_list})
