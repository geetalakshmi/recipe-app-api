from django.test import TestCase
from django.contrib.auth import get_user_model
# from core.models import User, UserManager


class modelTests(TestCase):

    def test_create_user_with_email_successful(self):
        '''test creating a new user with email is successful'''
        email = 'lakshmi.geeta@gmail.com'
        password = 'Sybase123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''test the email for the new user is normalized'''
        email = 'lakshmi.geeta@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email,
            'tet123'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        '''test creating user with no email raises error'''
        with self.assertRaises(ValueError):
            '''anything that run here should raise the value error \
            else this test fails'''
            get_user_model().objects.create_user(
                None,
                'test123'
            )

    def test_create_new_superuser(self):
        '''test creating a new super user'''
        user = get_user_model().objects.create_superuser(
            'test@gmail.com',
            'test123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
