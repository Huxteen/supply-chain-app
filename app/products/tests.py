from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from products.models import Product

PRODUCT_URL = reverse('products:products-list')


# Create your tests here.
class publicProductApiTest(TestCase):
    """Test the Product api public"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving products"""
        res = self.client.get(PRODUCT_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class privateProductApiTest(TestCase):
    """Test the authorized Dataset API"""

    def setUp(self):
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@gmail.com',
            password='password123'
        )

        self.user = get_user_model().objects.create_user(
            'test@husteen.com',
            'testpass'
        )

        self.client = APIClient()
        self.client.force_authenticate(self.user)
        self.client.force_authenticate(self.admin_user)

    def test_retrieve_product(self):
        """"Test retrieve product"""
        Product.objects.create(name='MacBook M1', user_id=self.user,
                               price=99.99, quantity_in_stock=200)
        Product.objects.create(name='LogiTech Mouse', user_id=self.user,
                               price=299, quantity_in_stock=150)

        res = self.client.get(PRODUCT_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_product_successful(self):
        """Test only admin can create product successful"""
        admin_user = self.admin_user
        payload = {'name': 'MacBook M1', 'user_id': admin_user,
                   'price': 99.99, 'quantity_in_stock': 200}
        res = self.client.post(PRODUCT_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)
