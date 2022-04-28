from django.test import TestCase
from .forms import PortfolioForm, AddAsset, UpdateAsset


class TestPortfolioForm(TestCase):

    def test_portfolio_name_is_required(self):
        form = PortfolioForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_field_are_explicit_in_form_metaclass(self):
        form = PortfolioForm()
        self.assertEqual(form.Meta.fields, ['name'])


class TestAddAssetForm(TestCase):

    def test_portfolio_name_is_required(self):
        form = AddAsset({'quantity': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors.keys())
        self.assertEqual(form.errors['quantity'][0], 'This field is required.')

    def test_field_are_explicit_in_form_metaclass(self):
        form = AddAsset()
        self.assertEqual(form.Meta.fields, ['quantity'])


class TestUpdateAssetForm(TestCase):

    def test_portfolio_name_is_required(self):
        form = UpdateAsset({'quantity': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('quantity', form.errors.keys())
        self.assertEqual(form.errors['quantity'][0], 'This field is required.')

    def test_field_are_explicit_in_form_metaclass(self):
        form = UpdateAsset()
        self.assertEqual(form.Meta.fields, ['quantity'])
