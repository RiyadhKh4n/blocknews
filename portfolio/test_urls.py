from django.test import TestCase
from django.urls import reverse, resolve
from .models import Portfolio
from .views import get_portfolio_list, edit_portfolio, delete_portfolio, create_portfolio, get_asset, get_asset_list, add_asset, update_asset  # noqa


class TestPortfolioUrls(TestCase):
    def test_getPortfolioList_url_is_resolved(self):
        url = reverse('get_portfolio_list')
        self.assertEquals(resolve(url).func, get_portfolio_list)

    def test_editPortfolio_url_is_resolved(self):
        url = reverse('edit_portfolio', args=[1])
        self.assertEqual(resolve(url).func, edit_portfolio)

    def test_deletePortfolio_url_is_resolved(self):
        url = reverse('delete_portfolio', args=[1])
        self.assertEqual(resolve(url).func, delete_portfolio)

    def test_createPortfolio_url_is_resolved(self):
        url = reverse('create_portfolio_url')
        self.assertEquals(resolve(url).func, create_portfolio)

    def test_viewPortfolio_url_is_resloved(self):
        url = reverse('get_asset_list', args=[1])
        self.assertEquals(resolve(url).func, get_asset_list)

    def test_get_url_is_resolved(self):
        url = reverse('get_asset', args=[1])
        self.assertEquals(resolve(url).func, get_asset)

    def test_add_url_is_resolved(self):
        url = reverse('add_asset_form', args=[1, 'ADA', '10.00'])
        self.assertAlmostEquals(resolve(url).func, add_asset)

    def test_update_url_is_resolved(self):
        url = reverse('update_asset', args=[1, 'sell', 'ADA', '0.89'])
        self.assertAlmostEquals(resolve(url).func, update_asset)
