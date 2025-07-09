from django.shortcuts import render
from .models import Artist, Album, Track
from django.views.generic.base import TemplateView

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


def item_search(request):
    query = request.GET.get("q","")
    artists = Artist.objects.filter(name__icontains=query) if query else []
    albums = Album.objects.filter(title__icontains=query) if query else []
    tracks = Track.objects.filter(title__icontains=query) if query else []

    context = {
        'query': query,
        'artists': artists,
        'albums': albums,
        'tracks': tracks,
    }
    return render(request, 'store/artikel_suche.html', context)