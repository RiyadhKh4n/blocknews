from django import forms
from .models import Portfolio, Asset


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name', 'USDvalue', 'user', 'slug']
        # fields = ['name']


class AddAsset(forms.ModelForm):
    class Meta:
        models = Asset
        fields = ['CoinID', 'quantity', 'AveragePrice', 'USDSpent', 'USDEarned', 'CurrentInvestment', 'PnL']