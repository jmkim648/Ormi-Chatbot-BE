from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser

class CustomUserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    # create test
    def test_create_user(self):
        '''user create test'''
        print('===user create test===')
        url = reverse('signup')
        response = self.client.post(url, 
            {'email': 'test@test.com', 'password': 'testtest1', 'password2': 'testtest1', 'nickname': 'testuser'}, 
            format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get(id=1).email, 'test@test.com')
        self.assertEqual(CustomUser.objects.get(id=1).nickname, 'testuser')
        self.assertTrue(CustomUser.objects.get(id=1).is_active)

    def test_login_user(self):
        '''user login test'''
        print('===user login test===')
        url = reverse('signup')
        response = self.client.post(url, 
            {'email': 'test@test.com', 'password': 'testtest1', 'password2': 'testtest1', 'nickname': 'testuser'}, 
            format='json')
        
        url = reverse('login')
        response = self.client.post(url,
            {'email': 'test@test.com', 'password':'testtest1'},
            format='json'
        )
        user = self.client.login(email='test@test.com', password='testtest1')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['refresh'])
        self.assertTrue(response.data['access'])
        self.assertTrue(user)
