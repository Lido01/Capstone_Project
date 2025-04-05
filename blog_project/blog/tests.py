from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.urls import reverse
from .models import CustomUser

class UserTests(APITestCase):

    def test_create_user(self):
        data = {"username": "abebe", 
                "email": "abebe@gmail.com",
                "password": "password"}
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class AuthAPItest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = CustomUser.objects.create_user(
            email = 'testuser@example.com',
            password = 'testpass',
            username = 'testuser',
        )
    def test_registration(self):
        data = {
            'email' : 'newuser@gmail.com',
            'password' : 'newpass122',
            'username' : 'newuser123',
        }
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.filter(email='newuser@gmail.com').count(), 1)
    
    def test_invalid_credentials(self):
        data = {
            "email": "abc",
            "password": "abc123",
            "username": "abc",
        }
        response = self.client.post(reverse("register"), data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
  

    def test_user_login(self):
        data = {
            "email": "newuser@gmail.com",
            "password": "newuser123",
        }
        response = self.client.post(reverse("login", data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('access', response.data)
        self.assertIn('refresh', response.data)


    def test_invalid_user_login(self):
        data = {
            'email': 'abcabc11@example.com',
            'password': 'aaabbb123',
            'username' : 'abcdef'
        }
        response = self.client.post(reverse('login'), data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertIn("No active account found with the given credentials", response.data['detail'])

