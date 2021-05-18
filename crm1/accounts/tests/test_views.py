import json

from accounts.models import Customer, Order, Product, Tag
from django.test import Client, TestCase
from django.urls import reverse


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.home_url = reverse('home')
        self.products_url = reverse('products')
        self.customers_url = reverse('customer', kwargs={'pk_test': '1'})

    def test_home_GET(self):
        response = self.client.get(self.home_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/dashboard.html')

    def test_products_GET(self):
        response = self.client.get(self.products_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/products.html')

    def test_customers_GET(self):
        response = self.client.get(self.customers_url)

        self.assertEquals(response.status_code, 201)
        self.assertTemplateUsed(response, 'accounts/customers.html')
