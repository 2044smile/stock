from django.contrib import admin
from django.urls import path, include

from django_telethon.urls import django_telethon_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('stock/', include("stock.urls")),
    path('accounts/', include("accounts.urls")),

    path('telegram/', django_telethon_urls()),
]
