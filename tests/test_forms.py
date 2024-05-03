from django.test import TestCase

from orders.forms import RegisterUser


class RegisterUserFormTest(TestCase):

    def test_register_form_valid(self):
        form = RegisterUser(
            data={
                "username": "user",
                "password": "S0meD1ff@pass",
                "first_name": "Ketty",
                "last_name": "Perry",
                "email": "katty.perry@email.com",
            }
        )
        self.assertTrue(form.is_valid())

    def test_register_form_valid(self):
        form = RegisterUser(
            data={
                "username": "user",
                "password": "S0meD1ff@pass",
                "first_name": "Ketty",
                "last_name": "Perry",
                "email": "not_email",
            }
        )
        self.assertFalse(form.is_valid())