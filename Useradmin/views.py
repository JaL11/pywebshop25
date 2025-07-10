from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views import generic
from .forms import MySignUpForm
from django.views.generic.base import TemplateView
from .forms import ProfilePictureForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


# Create your views here.
class MySignUpView(generic.CreateView):
    form_class = MySignUpForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class MyLoginView(LoginView):
    template = "registration/login.html"


class MyHomeView(TemplateView):
    template_name = "home.html"


@login_required
def upload_profile_picture(request):
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')  # Zurück zur Homepage
    else:
        form = ProfilePictureForm(instance=request.user)
    return render(request, 'upload_profile_picture.html', {'form': form})


   
