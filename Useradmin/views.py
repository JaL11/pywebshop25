from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from .forms import MySignUpForm
from django.views.generic.base import TemplateView



# Create your views here.
class MySignUpView(generic.CreateView):
    form_class = MySignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class MyLoginView(LoginView):
    template = "registration/login.html"



class MyHomeView(TemplateView):
    template_name = "home.html"

class ArtikelSucheView(TemplateView):
    template_name = "artikel_suche.html"

   
