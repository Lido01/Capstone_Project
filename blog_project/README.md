# Blog Capstone Project


## Project Description

This Blog Project that I have built is a comprehensive showcase of the skills that I have learned and gained so far in backend web development. It features a robust backend that allows users to interact seamlessly with the server, enabling them to perform various actions such as creating, reading, updating, and deleting blog posts. 

The application is built using Django and Django REST Framework. Users can register and authenticate securely, with role-based access control implemented to manage permissions effectively.

In addition to these core functionalities, the project incorporates some advanced features that is like search functionality, to quickly find relevant posts, and category for better content organization. The API endpoints are designed to be RESTful, promoting easy integration with various frontend frameworks or mobile applications.

This project not only demonstrates my technical proficiency but also reflects my understanding of best practices in software development, including code organization, version control, and responsive design principles. Overall, it serves as a solid foundation for future enhancements and potential expansion into a fully-featured blogging platform.

## Features

- User Authentication 
    - User registration
    - User login
    - User logout

- Blog Posts
  - Create new posts
  - Read all posts
  - Update existing posts
  - Delete posts

-  Comments
  - Create comments on posts
  - Read comments for each post
  - Update comments
  - Delete comments by comment author

- Categories
  - Create categories for organizing posts
  - Read all categories
  - Update existing categories
  - Delete categories

## What I used Software

    - Python
    - Django
    - Django REST Framework
    - SQLite 
    - Postman (for testing the API)
    - Local Chrome browser(http://127.0.0.1:8000/)

## Installation
1. Clone the repository: https://github.com/Lido01/Capstone_Project.git

## API Endpoints
        ### User Authentication

            - Register : POST /blog/register/
            - Login  : POST /blog/login/
            - Logout  : POST /blog/logout/

        ### Blog Posts

            - Create Post : POST /blog/posts/
            - Read All Posts : GET /blog/posts/
            - Read Single Post : GET /blog/posts/{id}/
            - Update Post : PUT /blog/posts/{id}/
            - Delete Post  : DELETE /blog/posts/{id}/

        ### Comments

            - Create Comment : POST /blog/comments/
            - Read Comments  : GET /blog/comments/
            - Update Comment : PUT /blog/comments/{comment_id}/
            - Delete Comment : DELETE /blog/comments/{comment_id}/

        ### Categories

            - Create Category : POST /api/categories/
            - Read All Categories : GET /api/categories/
            - Update Category : PUT /api/categories/{id}/
            - Delete Category : DELETE /api/categories/{id}/

## Contributing

If you'd like to contribute to this project, please fork the repository and create a pull request with your changes.

## Acknowledgments
- ALX  Africa
