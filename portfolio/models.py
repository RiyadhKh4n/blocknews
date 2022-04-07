from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    name = models.CharField(max_length=10, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    usd_value = models.DecimalField(blank=True, max_digits=10, decimal_places=3, default='0.00')

    class Meta:
        ordering = ['-usd_value']

    def __str__(self):
        return self.name


class Asset(models.Model):
    portfolio_name = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=6)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=3, default=0.00)
    average_price = models.DecimalField(max_digits=10, decimal_places=3)
    usd_spent = models.DecimalField(max_digits=10, decimal_places=3)
    current_holdings = models.DecimalField(max_digits=10, decimal_places=2)
    usd_earned = models.DecimalField(max_digits=10, decimal_places=3)
    added_to_portfolio = models.DateTimeField(auto_now_add=True)
    pnl = models.DecimalField(max_digits=10, decimal_places=3, default='0.00')

    class Meta:
        ordering = ['added_to_portfolio']

    def __repr__(self):
        return self.ticker
