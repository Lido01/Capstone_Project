from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Post, Category
from django.contrib.auth import get_user_model
from blog.models import CustomUser
User = get_user_model()

class PostAPITestCase(APITestCase):
    def setUp(self):
        
        self.user = CustomUser.objects.create_user(
            email="testuser@example.com",
            username="testuser",
            password="password123")
        self.category = Category.objects.create(
            name="Test Category")
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            user=self.user,
            category=self.category,
        )
        # Authenticate the test client
        self.client.login(
            email="testuser@example.com",
            password="password123"
            )
         # Authenticate the client
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_posts(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        data = {
            "user": self.user.id,
            "title": "New Post",
            "content": "This is a new post.",
            "category": self.category.id,
        }

        response = self.client.post(reverse('post_list'), data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_post(self):
        url = reverse('post_detail', args=[self.post.id])  # Assumes you named your detail endpoint 'post-detail'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_post(self):
        data = {
            "title": "Updated Post",
            "content": "Updated content.",
            "user": self.user.id,
            "category": self.category.id,
        }
        response = self.client.put(reverse('post_detail', args=[self.post.id]), data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_post(self):
        response = self.client.delete(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)