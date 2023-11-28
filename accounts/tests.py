from django.test import TestCase
from rest_framework.test import APIClient
from .models import CustomUser

class CustomUserTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    # create test
    def test_create_user(self):
        '''
        user create test
        '''
        print('===user create test===')
        response = self.client.post('/accounts/signup/', 
            {'email': 'test@test.com', 'password': 'testpw12', 'password2': 'testpw12', 'nickname': 'testuser'}, 
            format='json')
        print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 201)
        self.assertEqual(CustomUser.objects.count(), 1)
        self.assertEqual(CustomUser.objects.get(id=1).email, 'test@test.com')
        self.assertEqual(CustomUser.objects.get(id=1).nickname, 'testuser')
        self.assertTrue(CustomUser.objects.get(id=1).is_active)

    def test_login_user(self):
        '''
        user login test
        '''
        print('===user login test===')
        response = self.client.post('/accounts/signup/', 
            {'email': 'test@test.com', 'password': 'testpw12', 'password2': 'testpw12', 'nickname': 'testuser'}, 
            format='json')
        
        response = self.client.post('/accounts/login/',
            {'email': 'test@test.com', 'password':'testpw12'},
            format='json'
        )
        print(response.content.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.data['refresh_token'])
        self.assertTrue(response.data['access_token'])
