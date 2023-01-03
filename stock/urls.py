from django.contrib import admin
from django.urls import path, include

from .views import IndexListView

urlpatterns = [
    path('', IndexListView.as_view()),
]
