from django.shortcuts import render
from .models import Artist, Album, Track

def home(request):
    artists = Artist.objects.all()
    albums = Album.objects.all()
    tracks = Track.objects.all()
    
    context = {
        'artists': artists,
        'albums': albums,
        'tracks': tracks
    }
    
    return render(request, 'store/home.html', context)