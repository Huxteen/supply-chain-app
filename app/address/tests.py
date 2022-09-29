from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status
from address.models import Address

ADDRESS_URL = reverse('address:address-list')


# Create your tests here.
class publicAddressApiTest(TestCase):
    """Test the Address api public"""

    def setUp(self):
        self.client = APIClient()

    def test_login_required(self):
        """Test that login is required for retrieving address"""
        res = self.client.get(ADDRESS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class privateAddressApiTest(TestCase):
    """Test the authorized Address API"""

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@husteen.com',
            'testpass'
        )

        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_address(self):
        """Test retrieve address"""
        user = self.user

        Address.objects.create(
            company_name='Shop Rite',
            contact_name='Andrew Smith',
            contact_title='mr',
            address='2 Broad Street',
            city='London',
            postal_code='23401',
            phone='07034252738',
            fax='23456',
            user_id=user,
        )

        Address.objects.create(
            company_name='HP',
            contact_name='John Doe',
            contact_title='mr',
            address='2 Layout Street',
            city='London',
            postal_code='23401',
            phone='0905624261',
            fax='876123',
            user_id=user,
        )

        res = self.client.get(ADDRESS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_address_successful(self):
        """Test user can create address successful"""
        user = self.user
        payload = {
            'company_name': 'HP',
            'contact_name': 'John Doe',
            'contact_title': 'mr',
            'address': '2 Layout Street',
            'city': 'London',
            'postal_code': '23401',
            'phone': '0905624261',
            'fax': '876123',
            'user_id': user,
        }
        res = self.client.post(ADDRESS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
