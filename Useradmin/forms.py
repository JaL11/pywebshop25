from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div
from django.contrib.auth.forms import AuthenticationForm


class MySignUpForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ("username", "first_name", "last_name", "email", "profile_picture")


class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['profile_picture']

class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")


