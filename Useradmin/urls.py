from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", views.MyLoginView.as_view() ,name="login"),
    path('signup/', views.MySignUpView.as_view(), name='signup'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

