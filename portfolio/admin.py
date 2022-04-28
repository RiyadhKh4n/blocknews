from django.contrib import admin
from portfolio.models import Portfolio, Asset


@admin.register(Portfolio)
class PortfolioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ('user', 'name', 'created_on')
    list_display = ('name', 'user', 'created_on')
    search_fields = ['name', 'user']


@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('ticker', 'portfolio_user', 'portfolio_name', 'pnl',
                    'quantity', 'added_to_portfolio')
    search_fields = ['portfolio_name']
    list_filter = ('portfolio_name', 'pnl', 'added_to_portfolio')

    def portfolio_user(self, instance):
        return instance.portfolio_name.user
