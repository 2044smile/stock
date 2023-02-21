from accounts.models import User

from django.contrib import admin


@admin.register(User)
class AccountsAdmin(admin.ModelAdmin):
    list_display = ['email']
    # list_display = ['email', 'kakao_nickname', 'stock_code_1', 'stock_code_2', 'stock_code_3', 'is_active']
