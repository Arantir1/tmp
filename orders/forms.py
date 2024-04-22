from django.forms import ModelForm, CharField, TextInput, PasswordInput
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms
from .models import Order, Book
from tinymce.widgets import TinyMCE


class TinyMCEWidget(TinyMCE):
    def use_required_attribute(self, *args):
        return False


class BookForm(forms.ModelForm):
    # description = forms.CharField(
    #     widget=TinyMCEWidget(attrs={"required": False, "cols": 30, "rows": 10})
    # )

    class Meta:
        model = Book
        fields = "__all__"


class RegisterUser(ModelForm):
    class Meta:
        model = User
        fields = ["username", "password", "first_name", "last_name", "email"]


# class LoginUser(ModelForm):
#     class Meta:
#         model = User
#         fields = ["username", "password"]


class LoginUser(AuthenticationForm):
    username = CharField(widget=TextInput())
    password = CharField(widget=PasswordInput())


class MakeOrder(ModelForm):
    class Meta:
        model = Order
        fields = ["address", "order_date", "price", "status", "client"]
