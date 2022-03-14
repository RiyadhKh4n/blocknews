from django import forms
from .models import Portfolio, Asset


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['name', 'USDvalue', 'user', 'slug']