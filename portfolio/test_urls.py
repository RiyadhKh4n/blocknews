from django.test import TestCase
from django.urls import reverse, resolve
from .models import Portfolio
from .views import get_portfolio_list, edit_portfolio, delete_portfolio, create_portfolio, get_asset_list, add_asset, update_asset


class TestPortfolioUrls(TestCase):
    def test_getPortfolioList_url_is_resolved(self):
        url = reverse('get_portfolio_list')
        self.assertEquals(resolve(url).func, get_portfolio_list)

    # def test_editPortfolio_url_is_resolved(self):
    #     portfolio = Portfolio.objects.create(name='Django')
    #     url = reverse(f'edit_portfolio/{portfolio.id}')
    #     self.assertEquals(resolve(url).func, edit_portfolio)

    # def test_createPortfolio_url_is_resolved(self):
    #     url = reverse('create_portfolio')
    #     self.assertEquals(resolve(url).func, create_portfolio)