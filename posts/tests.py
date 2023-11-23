from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTest(APITestCase):
    def setUp(self):
        User.objects.create_user(username='tester', password='pw')
    
    def test_list_posts(self):
        tester = User.objects.get(username='tester')
        Post.objects.create(owner=tester, title='test title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_logged_in_create_posts(self):
        self.client.login(username='tester', password='pw')
        response = self.client.post('/posts/', {'title': 'test title'})
        count = Post.objects.count()
        self.assertEqual(count, 1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def test_logged_out_create_posts(self):
        response = self.client.post('/posts/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)