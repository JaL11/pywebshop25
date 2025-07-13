from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("artikel-suche/", views.item_search, name="artikel-suche"),
    path("pdf/", views.generate_pdf, name="pdf"),
    path('albums/<int:album_id>/rate/', views.rate_album, name='rate_album'),
]
