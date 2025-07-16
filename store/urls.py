from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("artikel-suche/", views.item_search, name="artikel-suche"),
    path("pdf/", views.generate_pdf, name="pdf"),
    path('albums/<int:album_id>/rate/', views.rate_album, name='rate_album'),
    path('albums/toggle_rating/', views.toggle_rating, name='toggle_rating'),
    path("album-info/<int:album_id>/", views.get_album_info, name="album_info"), # type: ignore
    path("artist-info/<int:artist_id>/", views.get_artist_info, name="artist_info"),
    path("track-info/<int:track_id>/", views.get_track_info, name="track_info") # Uncomment if track info view is implemented
]
