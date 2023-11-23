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


class PostDetailViewTest(APITestCase):
    def setUp(self):
        sub1 = User.objects.create_user(username='subject1', password='pw')
        sub2 = User.objects.create_user(username='subject2', password='pw')
        Post.objects.create(
            owner=sub1, title='sub1 title', content='sub1 content'
        )
        Post.objects.create(
            owner=sub2, title='sub2 title', content='sub2 content'
        )

    def test_get_post_with_valid_id(self):
        response = self.client.get('/posts/1')
        self.assertEqual(response.data['title'], 'sub1 title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_get_post_with_invalid_id(self):
        response = self.client.get('/posts/369')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
    
    def test_user_update_owned_post(self):
        self.client.login(username='subject1', password='pw')
        response = self.client.put('/posts/1', {'title': 'sub1 updated title'})
        post = Post.objects.filter(pk=1).first()
        self.assertEqual(post.title, 'sub1 updated title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_user_update_not_owned_post(self):
        self.client.login(username='subject1', password='pw')
        response = self.client.put('/posts/2', {'title': 'sub2 updated title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        
