from rest_framework.test import APIClient, APITestCase
from .models import Category
from blog.models import CustomUser
from django.urls import reverse
from rest_framework import status

class CategoryAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username="testuser",
            email = "test@example.com",
            password="password123"
            )
        # Authenticate the client
        self.client.login(
            email = "test@example.com",
            password="password123"
            )
        self.category = Category.objects.create(
           name="Test One",
           description = "This is test one Description"
       )

    def test_category_list(self):
        response = self.client.get(reverse('category_list_create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_category(self):
        data = {
            "name": "Tech Category",
            "description" : "This is tech Description"
        }

        response = self.client.get(reverse('category_list_create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], data['name'])

        data = {
            "name": "Updated Category",
            "description": "Updated Description"
            }
        response = self.client.post(reverse('category_list_create'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_get_category_list(self):
        """Test retrieving the list of categories"""
        response = self.client.get(reverse('category_list_create'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), Category.objects.count())

    def test_get_category_detail(self):
        """Test retrieving a specific category by ID"""
        response = self.client.get(reverse('category_detail', kwargs={'pk': self.category.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], self.category.name)

    def test_update_category(self):
        """Test updating an existing category"""
        data = {
            "name": "Updated Category",
            "description": "Updated Description"
            }
        response = self.client.put(reverse('category_detail', kwargs={'pk': self.category.id}), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], data['name'])

    def test_delete_category(self):
        """Test deleting a category"""
        response = self.client.delete(reverse('category_detail', kwargs={'pk': self.category.id}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Category.objects.count(), 0)
