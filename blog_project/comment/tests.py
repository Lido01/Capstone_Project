from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from post.models import Post
from .models import Comment
from category.models import Category
from blog.models import CustomUser

User = get_user_model()
class CommentAPITestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            username = "testuser",
            email = "test@example.com",
            password = "password123"
            )
        # Authenticate the user
        self.client.login(
            email="test@example.com",
            password="password123"
            )
        # Create a test category
        self.category = Category.objects.create(
            name="Test Category"
            )
        # Create a test post
        self.post = Post.objects.create(
            title="Test Post",
            content="This is a test post.",
            user=self.user,
            category=self.category
        )
        # Create a test comment
        self.comment = Comment.objects.create(
            content="This is a test comment.",
            post=self.post,
            user=self.user
        )
         # Authenticate the client
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_comments(self):
        response = self.client.get(reverse('comment_list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # def test_create_comment(self):
    #     data = {
    #         "content": "This is another comment.",
    #         "post": self.post.id,  # Passing the post ID
    #         "user": self.user.id   # Passing the user ID
    #     }
    #     response = self.client.post(reverse('list_comment'), data)
    #     self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_retrieve_comment(self):
        url = reverse('comment_detail', args=[self.comment.id])  # Assumes you named the detail endpoint 'comment-detail'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_comment(self):
        data = {
            "content": "Updated comment content.",
            "post": self.post.id,
            "user": self.user.id
        }
        url = reverse('comment_detail', args=[self.comment.id])
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_comment(self):
        url = reverse('comment_detail', args=[self.comment.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)