from django.db import models
from django.contrib.auth.models import User


class Portfolio(models.Model):
    """
    Class that defines the Portfolio Model
    """
    name = models.CharField(max_length=9, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Asset(models.Model):
    """
    Class that defines the Asset Model
    """
    portfolio_name = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    ticker = models.CharField(max_length=6)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    price = models.DecimalField(max_digits=10, decimal_places=3)
    average_price = models.JSONField(blank=True, null=True)
    usd_spent = models.DecimalField(max_digits=10, decimal_places=3)
    usd_earned = models.DecimalField(max_digits=10, decimal_places=3)
    added_to_portfolio = models.DateTimeField(auto_now_add=True)
    pnl = models.DecimalField(max_digits=10, decimal_places=3, default='0.00')

    class Meta:
        ordering = ['-ticker']

    def __repr__(self):
        return self.ticker
