from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APIClient
from .models import ChatPost, ChatMessage

User = get_user_model()


class ChatTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        url = reverse('accounts:signup')
        data = {'email': 'testuser@test.com', 'password': 'testpw212', 'password2': 'testpw212', 'nickname': 'testuser'}
        self.client.post(url, data, format='json')
        
        data = {'email': 'testuser@test.com', 'password': 'testpw212'}
        response = self.client.post('/accounts/login/', data)
        print(response.content.decode('utf-8'))
        self.access_token = response.data['access_token']

    def test_create_chat_post(self):
        '''
        create chat test
        '''
        print('===chat create test===')
        url = reverse('chat:chat_list')
        data = {'language': 'Python', 'convention': 'PEP8', 'user': 1}
        response = self.client.post(url, data, HTTP_AUTHORIZATION=f'Bearer {self.access_token}', format='json')

        print(response.content.decode('utf-8'))

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(ChatPost.objects.count(), 1)
        self.assertEqual(ChatPost.objects.get().language, 'Python')