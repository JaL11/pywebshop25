from django.contrib.auth.forms import UserCreationForm
from .models import MyUser
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div


class MySignUpForm(UserCreationForm):

    class Meta:
        model = MyUser
        fields = ("username", "first_name", "last_name", "email", "profile_picture")

    

class ProfilePictureForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['profile_picture']


class LoginForm(forms.Form):
    sername = forms.CharField(label="Username")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Div(
                Field(
                    "username", css_class="w-full px-4 py-2 border rounded bg-red-500 text-black"),
                Field(
                    "password", css_class="w-full px-4 py-2 border rounded bg-white text-black"),
                Submit(
                    "submit", "Login", css_class="mt-4 bg-violet-600 text-white px-4 py-2 rounded hover:bg-violet-700"),
                css_class="bg-red-500"
            )
        )
