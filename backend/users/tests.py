from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase, force_authenticate
from .views import UserModelViewSet
from .models import User
from mixer.backend.django import mixer
# from django.contrib.auth.models import User


class TestUserApi(TestCase):

    def test_get_list_1(self):
        factory = APIRequestFactory()
        user = User.objects.create_superuser(
            'admin',
            email='superuser@gb.local',
            password='admin12345'
        )
        User.objects.create(
            user_name='Petr',
            first_name='Петр',
            last_name='Петров',
            birthday_year=1980,
            email='petr80@gb.local'
        )
        request = factory.get('/api/users')
        force_authenticate(request, user)
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_list_2(self):
        client = APIClient()
        User.objects.create(
            user_name='Petr',
            first_name='Петр',
            last_name='Петров',
            birthday_year=1980,
            email='petr80@gb.local'
        )
        response = client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestUserClientApi(APITestCase):

    def setUp(self) -> None:
        self.admin = User.objects.create_superuser(
            'admin',
            email='superuser@gb.local',
            password='admin12345'
        )
        # self.user = mixer.blend(User)
        self.user = User.objects.create(
            user_name='Petr',
            first_name='Петр',
            last_name='Петров',
            birthday_year=1980,
            email='petr80@gb.local'
        )

    def test_get_list_3(self):
        self.client.login(
            username='admin',
            password='admin12345'
        )
        self.client.logout()
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
