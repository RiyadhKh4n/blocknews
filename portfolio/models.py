from django.db import models


class Portfolio(models.Model):
    name = models.CharField(max_length=50, unique=True)
    coins = models.ManyToManyField(Coin, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    USDvalue = models.DecimalField(default='0.00')
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['USDvalue']

    def __str__(self):
        return self.title
