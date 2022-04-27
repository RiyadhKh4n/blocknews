from django import forms
from .models import Portfolio, Asset


class PortfolioForm(forms.ModelForm):
    """
    Form that allows user to create a portflio
    """
    class Meta:
        model = Portfolio
        fields = ['name']


class AddAsset(forms.ModelForm):
    """
    Form that allows user to add a new asset to a portfolio
    """
    class Meta:
        model = Asset
        fields = ['quantity']


class UpdateAsset(forms.ModelForm):
    """
    Form that allows the user to update the quantity of their asset
    """
    class Meta:
        model = Asset
        # fields = ['quantity', 'price']
        fields = ['quantity']
