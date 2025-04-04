# from rest_framework.test import APIClient, APITestCase
# from .models import Category
# from blog.models import CustomUser

# class CategoryAPITestCase(APITestCase):
#     def setUp(self):
#         self.user = CustomUser.objects.create_user(
#             username="testuser",
#             email = "test@example.com",
#             password="password123"
#             )
#         # Authenticate the client
#         self.client.login(
#             email = "test@example.com",
#             password="password123"
#             )
#         self.category = Category.objects.create(
#            name="Test One",
#            description = "This is test one Description"
#        )

#     def test_category_list(self):

#         data = 

  
# Create your tests here.
from django.test import TestCase
from .models import Category

class CategoryModelTestCase(TestCase):
    def setUp(self):
        # Create initial category for testing
        self.category = Category.objects.create(
            name="Test Category",
            description="This is a test category description."
        )

    def test_create_category(self):
        # Create a new category
        category = Category.objects.create(
            name="New Category",
            description="Description for new category."
        )
        self.assertEqual(Category.objects.count(), 2)  # Check the count of categories
        self.assertEqual(category.name, "New Category")  # Verify the name

    def test_read_category(self):
        # Retrieve the created category
        category = Category.objects.get(name="Test Category")
        self.assertEqual(category.description, "This is a test category description.")
        self.assertEqual(str(category), "Test Category")  # Test __str__ method

    def test_update_category(self):
        # Update the category's name
        self.category.name = "Updated Category"
        self.category.save()

        updated_category = Category.objects.get(id=self.category.id)
        self.assertEqual(updated_category.name, "Updated Category")

    def test_delete_category(self):
        # Delete the category
        self.category.delete()

        self.assertEqual(Category.objects.count(), 0)  # Ensure category is deleted