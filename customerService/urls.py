from django.urls import path
from . import views

urlpatterns = [
    path("dashboard/", views.MyCustomerService.as_view(), name="customerService"),
    path("addProduct/", views.AddProductView.as_view(), name="addProduct"),
    path("modifyProduct", views.ModifyProductView.as_view(), name="modifyProduct"),
    path('add-artist/', views.addArtist, name='add_artist'),
    path('add-album/', views.addAlbum, name='add_album'),
    path('add-track/', views.addTrack, name='add_track'),
    
]