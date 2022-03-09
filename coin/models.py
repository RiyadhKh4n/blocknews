from django.db import models
from django.contrib.auth.models import User


class Coin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    portfolio_name = models.ManyToManyField(Portfolio, on_delete=models.CASCADE)  # noqa
    ticker = models.CharField(max_length=5)
    quantity = models.DecimalField()
    AveragePrice = models.DecimalField()
    USDSpent = models.DecimalField()
    USDEarned = models.DecimalField()
    CurrentInvestment = models.DecimalField()
    added_to_portfolio = models.DateTimeField(auto_now_Add=True)

    class Meta:
        ordering = ['added_to_portfolio']

    def __str__(self):
        return self.title