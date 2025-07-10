from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django import forms

class MySignUpForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = {"username", "first_name", "last_name", "email", "profile_picture"}

    

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['profile_picture']