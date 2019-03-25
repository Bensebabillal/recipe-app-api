from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_succesful(self):
        """test creating a new user with an email is succeful"""
        email = 'benseba@gmail.com'
        password = 'test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,  email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email(self):
        """Test the email for a new user is normalizer"""
        email = 'test@HOTMAIL.FR'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creationg user with no email raise error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'teste123')

    def test_crate_new_superuser(self):
        """test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'benseba@gmail.com',
            'teste123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
