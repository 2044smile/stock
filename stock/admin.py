from stock.models import Channel, Stock

from django.contrib import admin

@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['channel_id', 'name']

@admin.register(Stock)
class StockAdmin(admin.ModelAdmin):
    list_display = ['channel', 'site_name', 'title', 'date']
