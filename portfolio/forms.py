from django import forms
from .models import Portfolio, Asset


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        exclude = ['user', 'slug', 'usd_value']
        fields = ['name']


class AddAsset(forms.ModelForm):
    class Meta:
        model = Asset
        # exclude = ['portfolio_name', 'pnl', 'usd_earned', 'usd_spent', 'current_investment']
        fields = ['quantity', 'average_price']


class UpdateAsset(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['quantity', 'average_price']
