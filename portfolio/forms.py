from django import forms
from .models import Portfolio, Asset


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        exclude = ['user', 'slug', 'USDvalue']
        fields = ['name']


class AddAsset(forms.ModelForm):
    class Meta:
        model = Asset
        exclude = ['portfolioID']
        fields = ['coinID', 'quantity', 'AveragePrice', 'USDSpent', 'USDEarned', 'CurrentInvestment', 'PnL']
