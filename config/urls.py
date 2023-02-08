from django.contrib import admin
from django.urls import path, include

from django_telethon.urls import django_telethon_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('account/', include("account.urls")),
    path('stock/', include("stock.urls")),

    path('telegram/', django_telethon_urls()),
]
