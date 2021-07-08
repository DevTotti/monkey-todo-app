from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker

class TestSetup(APITestCase):

    def setUp(self):
        self.fake = Faker()

        self.register_url = reverse('register')
        self.login_url = reverse('login')

        self.email = self.fake.email()
        self.password = self.fake.password()

        self.user_data = {
            "email": self.email,
            "password": self.password,
            "password2": self.password
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown()

