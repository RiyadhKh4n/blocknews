from django.contrib import admin
from portfolio.models import Portfolio, Asset


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('user', 'name', 'created_on')
    list_display = ('name', 'user', 'created_on', 'USDvalue')
    search_fields = ['name', 'user']


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('portfolio_user', 'coinID', 'portfolioID', 'PnL', 'quantity', 'added_to_portfolio')
    search_fields = ['coinID', 'portfolioID']
    list_filter = ('coinID', 'portfolioID', 'PnL', 'added_to_portfolio')

    def portfolio_user(self, instance):
        return instance.portfolioID.user
