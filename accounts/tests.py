from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

class CustomUserTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            email='test@test.com',
            password='password',
            nickname='testuser'
        )
        self.manager_user = get_user_model().objects.create_user(
            email='manager@test.com',
            password='password',
            nickname='manager',
            is_manager=True
        )
        self.client.login(email='test@test.com', password='password')
        # self.client.login(email='manager@test.com', password='password')

    # create test
    def test_create_user(self):
        '''user create test'''
        print('===user create===')
        self.assertEqual(self.user.email, 'test@test.com')
        self.assertEqual(self.user.nickname, 'testuser')
        self.assertTrue(self.user.is_active)

    # profile 페이지 DRF 구현 시 수정 필요
    def test_profile_view(self):
        '''user profile test'''
        print('===user profile===')
        url = reverse('profile')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.user.nickname)