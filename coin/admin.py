from django.contrib import admin
from coin.models import Coin

@admin.register(Coin)
class PortfolioAdmin(admin.ModelAdmin):
    list_filter = ('user', 'ticker')
    list_display = ('user', 'ticker')
    search_fields = ['ticker']
