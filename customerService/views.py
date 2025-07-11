from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from store.models import Track, Album, Artist
from django.shortcuts import redirect
from datetime import timedelta

# Create your views here.


@method_decorator(login_required, name="dispatch")
class MyCustomerService(TemplateView):
    template_name = "customerService/csPortal.html"


class AddProductView(TemplateView):
    template_name = "customerService/addProduct.html"

class ModifyProductView(TemplateView):
    template_name = "customerService/modifyProduct.html"


def addArtist(request):
    if request.method == "POST":
        name = request.POST.get("name")
        genre = request.POST.get("genre")
        dateOfBirth = request.POST.get("dateOfBirth")
        country = request.POST.get("country")
        bio = request.POST.get("bio")

        Artist.objects.create(
            name=name,
            genre=genre,
            dateOfBirth=dateOfBirth,
            country=country,
            bio=bio
        )
        return redirect("addProduct")
    return render(request, "csPortal.html")

def addAlbum(request):
    if request.method == "POST":
        title = request.POST.get("title")
        artist_name = request.POST.get("artist")
        releaseDate = request.POST.get("releaseDate")
        price = request.POST.get("price")
        
        artist = Artist.objects.get(name=artist_name)

        Album.objects.create(
            title=title,
            artist=artist,
            releaseDate=releaseDate,
            price=price,
            
        )
        return redirect("addProduct")
    return render(request, "csPortal.html")


def addTrack(request):
    if request.method == "POST":
        title = request.POST.get("title")
        album_name = request.POST.get("album")
        duration_str = request.POST.get("duration")

        album = Album.objects.get(title=album_name)

        h, m, s = map(int, duration_str.split(':'))
        duration = timedelta(hours=h, minutes=m, seconds=s)

        Track.objects.create(title=title, album=album, duration=duration)

        return redirect("addProduct")
    return render(request, "csPortal.html")
