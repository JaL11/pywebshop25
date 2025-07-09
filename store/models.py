from django.db import models

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

    def __str__(self):
        return f"{self.title} by {self.artist.name}"

class Track(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    duration = models.DurationField()

    def __str__(self):
        return f"{self.title} ({self.album.title})"