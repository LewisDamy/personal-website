import unittest
from django.test import Client

class SimpleTest(unittest.TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_page(self):
        response = self.client.get('/home/')
        self.assertEqual(response.status_code, 200)

    def test_about_page(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)

    def test_projects_page(self):
        response = self.client.get('/projects/')
        self.assertEqual(response.status_code, 200)

    def test_hobbies_page(self):
        response = self.client.get('/hobbies/')
        self.assertEqual(response.status_code, 200)
