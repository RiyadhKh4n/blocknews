from django import forms
from .models import Portfolio, Asset


class PortfolioForm(forms.ModelForm):
    # user = forms.CharField(initial={'user': 'User'})

    class Meta:
        model = Portfolio
        exclude = ['user', 'slug', 'USDvalue']
        fields = ['name']

class AddAsset(forms.ModelForm):
    class Meta:
        models = Asset
        fields = ['CoinID', 'quantity', 'AveragePrice', 'USDSpent', 'USDEarned', 'CurrentInvestment', 'PnL']



        
