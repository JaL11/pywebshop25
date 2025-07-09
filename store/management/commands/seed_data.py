from django.core.management.base import BaseCommand
from store.models import Artist, Album, Track
from datetime import timedelta
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Seed database with initial artists, albums, and tracks'

    def handle(self, *args, **kwargs):
        if Artist.objects.exists():
            self.stdout.write("Data already seeded. Skipping.")
            return

        # artists
        kendrick = Artist.objects.create(name="Kendrick Lamar", genre="hiphop", dateOfBirth="1987-06-17", country="USA", bio="Pulitzer-winning rapper.")
        adele = Artist.objects.create(name="Adele", genre="pop", dateOfBirth="1988-05-05", country="UK", bio="Known for emotional ballads.")
        bjork = Artist.objects.create(name="Björk", genre="electronic", dateOfBirth="1965-11-21", country="Iceland", bio="Experimental Icelandic singer blending genres.")
        taylor = Artist.objects.create(name="Taylor Swift", genre="pop", dateOfBirth="1989-12-13", country="USA", bio="Pop and country crossover megastar.")
        miles = Artist.objects.create(name="Miles Davis", genre="jazz", dateOfBirth="1926-05-26", country="USA", bio="Jazz legend and trumpet innovator.")
        daftpunk = Artist.objects.create(name="Daft Punk", genre="electronic", dateOfBirth="1993-01-01", country="France", bio="French electronic duo known for robot personas.")
        bob = Artist.objects.create(name="Bob Dylan", genre="folk", dateOfBirth="1941-05-24", country="USA", bio="Singer-songwriter and Nobel Prize winner.")
        shakira = Artist.objects.create(name="Shakira", genre="pop", dateOfBirth="1977-02-02", country="Colombia", bio="Global pop icon blending Latin and Arabic influences.")
        bowie = Artist.objects.create(name="David Bowie", genre="rock", dateOfBirth="1947-01-08", country="UK", bio="Visionary artist known for reinvention.")
        eminem = Artist.objects.create(name="Eminem", genre="hiphop", dateOfBirth="1972-10-17", country="USA", bio="Controversial and skilled rap lyricist.")

        # albums
        damn = Album.objects.create(title="DAMN.", artist=kendrick, releaseDate="2017-04-14", price=12.99)
        twentyone = Album.objects.create(title="21", artist=adele, releaseDate="2011-01-24", price=11.49)
        homogenic = Album.objects.create(title="Homogenic", artist=bjork, releaseDate="1997-09-22", price=11.99)
        folklore = Album.objects.create(title="Folklore", artist=taylor, releaseDate="2020-07-24", price=13.49)
        kind_of_blue = Album.objects.create(title="Kind of Blue", artist=miles, releaseDate="1959-08-17", price=10.00)
        random_access = Album.objects.create(title="Random Access Memories", artist=daftpunk, releaseDate="2013-05-17", price=12.00)
        blonde_on_blonde = Album.objects.create(title="Blonde on Blonde", artist=bob, releaseDate="1966-05-16", price=9.99)
        laundry_service = Album.objects.create(title="Laundry Service", artist=shakira, releaseDate="2001-11-13", price=10.99)
        ziggy = Album.objects.create(title="Ziggy Stardust", artist=bowie, releaseDate="1972-06-16", price=11.99)
        marshall = Album.objects.create(title="The Marshall Mathers LP", artist=eminem, releaseDate="2000-05-23", price=11.49)

        # tracks
        Track.objects.create(title="DNA.", album=damn, duration=timedelta(minutes=3, seconds=6))
        Track.objects.create(title="HUMBLE.", album=damn, duration=timedelta(minutes=2, seconds=57))
        Track.objects.create(title="Rolling in the Deep", album=twentyone, duration=timedelta(minutes=3, seconds=48))
        Track.objects.create(title="Someone Like You", album=twentyone, duration=timedelta(minutes=4, seconds=45))
        Track.objects.create(title="Jóga", album=homogenic, duration=timedelta(minutes=5, seconds=5))
        Track.objects.create(title="Bachelorette", album=homogenic, duration=timedelta(minutes=5, seconds=18))
        Track.objects.create(title="Cardigan", album=folklore, duration=timedelta(minutes=4, seconds=0))
        Track.objects.create(title="Exile", album=folklore, duration=timedelta(minutes=4, seconds=45))
        Track.objects.create(title="So What", album=kind_of_blue, duration=timedelta(minutes=9, seconds=22))
        Track.objects.create(title="Freddie Freeloader", album=kind_of_blue, duration=timedelta(minutes=9, seconds=46))
        Track.objects.create(title="Get Lucky", album=random_access, duration=timedelta(minutes=6, seconds=7))
        Track.objects.create(title="Instant Crush", album=random_access, duration=timedelta(minutes=5, seconds=37))
        Track.objects.create(title="Visions of Johanna", album=blonde_on_blonde, duration=timedelta(minutes=7, seconds=30))
        Track.objects.create(title="Just Like a Woman", album=blonde_on_blonde, duration=timedelta(minutes=4, seconds=52))
        Track.objects.create(title="Whenever, Wherever", album=laundry_service, duration=timedelta(minutes=3, seconds=17))
        Track.objects.create(title="Underneath Your Clothes", album=laundry_service, duration=timedelta(minutes=3, seconds=45))
        Track.objects.create(title="Starman", album=ziggy, duration=timedelta(minutes=4, seconds=16))
        Track.objects.create(title="Ziggy Stardust", album=ziggy, duration=timedelta(minutes=3, seconds=13))
        Track.objects.create(title="Stan", album=marshall, duration=timedelta(minutes=6, seconds=44))
        Track.objects.create(title="The Real Slim Shady", album=marshall, duration=timedelta(minutes=4, seconds=44))

        self.stdout.write(self.style.SUCCESS("Seeded artists, albums, and tracks."))
        
        # create default superuser
        User = get_user_model()
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                password="admin123",
                email="admin@example.com"
            )
            self.stdout.write(self.style.SUCCESS("Created default superuser."))
