from django.contrib import admin
from django.urls import path, include

from django_telethon.urls import django_telethon_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('accounts/', include("dj_rest_auth.urls")),
    path('accounts/', include("allauth.urls")),
    # path('accounts/', include("accounts.urls")),
    path('stock/', include("stock.urls")),

    path('telegram/', django_telethon_urls()),
]
