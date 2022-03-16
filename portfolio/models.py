from django.db import models
from django.contrib.auth.models import User
from coin.models import Coin


class Portfolio(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    USDvalue = models.DecimalField(blank=True, max_digits=10, decimal_places=3, default='0.00')

    class Meta:
        ordering = ['-USDvalue']

    def __str__(self):
        return self.name


class Asset(models.Model):
    portfolio_name = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    coinID = models.ForeignKey(Coin, on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    AveragePrice = models.DecimalField(max_digits=10, decimal_places=3)
    USDSpent = models.DecimalField(max_digits=10, decimal_places=3)
    USDEarned = models.DecimalField(max_digits=10, decimal_places=3)
    CurrentInvestment = models.DecimalField(max_digits=10, decimal_places=3)
    added_to_portfolio = models.DateTimeField(auto_now_add=True)
    PnL = models.DecimalField(max_digits=10, decimal_places=3, default='0.00')

    class Meta:
        ordering = ['added_to_portfolio']

    def __str__(self):
        return self.coinID.ticker


