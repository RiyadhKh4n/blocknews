from django.test import TestCase
from django.urls import resolve, reverse


class TestHandler404(TestCase):
    def test_404_page(self):
        response = self.client.get('/handler404')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, 'errors/404.html')
