from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient, force_authenticate
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import Transaction

class TransactionTests(APITestCase):
    def setUp(self):
        self.noauth_client = APIClient()
        
        user = User.objects.create_user(username='testuser', password='testpassword')
        token = Token.objects.get(user=user)
        self.user_client = APIClient()
        self.user_client.force_authenticate(user=user, token=token)

        #self.admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin123')

    # def tearDown(self):
    #   pass

    def test_create_transaction_401(self):
        """
        Ensure only authenticated users can create Transactions
        """
        data = {}
        response = self.noauth_client.post('/api/transactions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_transaction(self):
        """
        Ensure we can create a new book.
        """
        data = {'date': '2025-02-15', 'vendor': 'Test Vendor', 'customer': 'Test Customer',
                'purchase_total': 10, 'snap':5, 'wicsenior':0, 'match_snap':5, 'match_wicsenior':0, 'cash_credit':0}
        response = self.user_client.post('/api/transactions/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_transaction(self):
        """
        Ensure we can get books.
        """
        response = self.user_client.get('/api/transactions/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)