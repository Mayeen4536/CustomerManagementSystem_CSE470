
from accounts.views import (createCustomer, createOrder, customers,
                            deleteOrder, home, products, updateOrder)
from django.test import SimpleTestCase
from django.urls import resolve, reverse


class TestUrls(SimpleTestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, home)


    def test_products_url(self):
        url = reverse('products')
        self.assertEquals(resolve(url).func, products)

    def test_cutomer_url(self):
        url = reverse('customer', kwargs={'pk_test':'1'})
        self.assertEquals(resolve(url).func, customers)

    def test_createOrder_url(self):
        url = reverse('create_order')
        self.assertEquals(resolve(url).func, createOrder)

    def test_updateOrder_url(self):
        url = reverse('update_order', kwargs={'pk':'1'})
        self.assertEquals(resolve(url).func, updateOrder)

    def test_deleteOrder_url(self):
        url = reverse('delete_order', kwargs={'pk':'1'})
        self.assertEquals(resolve(url).func, deleteOrder)

    def test_createCustomer_url(self):
        url = reverse('create_customer')
        self.assertEquals(resolve(url).func, createCustomer)
