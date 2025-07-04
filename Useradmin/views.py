from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from .forms import MySignUpForm


# Create your views here.
class MySignUpView(generic.CreateView):
    form_class = MySignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class MyLoginView(LoginView):
    template = "registration/login.html"

   
