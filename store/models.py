from django.db import models
from django.conf import settings

# Create your models here.
class Artist(models.Model):
    name = models.CharField(max_length=100)
    genre = models.CharField(max_length=50)
    dateOfBirth = models.DateField()
    country = models.CharField(max_length=50, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.name

class Album(models.Model):
    title = models.CharField(max_length=100)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    releaseDate = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    cover = models.ImageField(upload_to="album_covers", blank=True, null=True)
    ratings_enabled = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} by {self.artist.name}"

    def average_rating(self):
        return self.ratings.aggregate(models.Avg("value"))["value__avg"] or 0 # type: ignore[attr-defined]

class Track(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duration = models.DurationField()
    price = models.DecimalField(default=0.99, max_digits=2, decimal_places=2)

    def __str__(self):
        return f"{self.title} ({self.album.title})"

    # returns the average rating of the album
    # def average_rating_album(self):
    #     return self.album.average_rating()

    # def average_rating(self):
    #     return self.ratings.aggregate(models.Avg("value"))["value__avg"] or 0 # type: ignore[attr-defined]



class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name="ratings")
    value = models.PositiveSmallIntegerField()
    is_active = models.BooleanField(default=True)


    class Meta:
        unique_together = ("user", "album")  # prevent multiple ratings per album/user

    def __str__(self):
        return f"{self.album.title}: {self.value}⭐ by {self.user.username}"