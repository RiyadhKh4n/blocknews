from django import forms
from .models import Portfolio, Asset


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name']


class AddAsset(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['quantity']


class UpdateAsset(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['quantity', 'price']
