from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status

# Test GET odjects people
class PeopleTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_people(self):
        # Examples of GET request verification people
        response = self.client.get('/pop_people/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Test GET odjects people/id
class PeopleTestCase_id(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_people(self):
        # Examples of GET request verification people
        response = self.client.get('/pop_people/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Test GET odjects movies
class MoviesTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_people(self):
        # Examples of GET request verification people
        response = self.client.get('/pop_movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Test GET odjects movies/id
class MoviesTestCase_id(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_movies(self):
        # Examples of GET request verification movies
        response = self.client.get('/pop_movies/1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Test Search
class SearchTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_search(self):
        # Examples of GET request verification search
        response = self.client.get('/search/search_people')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# Test Notification
class Notification_test(TestCase):
    def setUp(self):
        self.client = APIClient()

    # Examples of Post request verification Notification
    def test_Notification(self):
        data = {'name': 'John', 'email': 'john@mail.com', 'subject': 'Hello', 'notification': 'Hello, world!'}
        response = self.client.post('/about/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

#Test Registration
class Regislration_Test(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_registration(self):
        url = reverse('registration')
        data = {
                    "name": "Test",
                    "email": "smolllll192@gmail.com",
                    "password": "111111",
                    "phone": "0960000000"
                }
        response = self.client.post(url, data, format='json')
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'Test')
        self.assertEqual(User.objects.first().email, 'smolllll192@gmail.com')
        self.assertTrue(User.objects.first().check_password('111111'))

# Test Login and Logout
class Login_Test(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='Test', password='password')

    def test_login(self):
        self.client = APIClient()
        url = reverse('login')
        data = {
            'name': 'Test',
            'password': 'password'
        }
        response = self.client.post(url, data, format='json', HTTP_AUTHORIZATION='Basic dGVzdDpwYXNzd29yZA==')

        self.assertEqual(response.status_code, status.HTTP_302_FOUND)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.first().username, 'Test')

    def test_logout(self):
        self.client.force_authenticate(user=self.user)
        url = reverse('logout')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
