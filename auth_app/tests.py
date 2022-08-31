from rest_framework.test import APITestCase
from rest_framework import status


class ViewsTest(APITestCase):
    def test_register(self):
        url = 'http://127.0.0.1:8000/auth/register/'
        data = {'username': 'sample', 'password': 'samp_le12=3', 'password2': 'samp_le12=3'}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
