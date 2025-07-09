from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("artikel-suche/", views.item_search, name="artikel-suche")
]
