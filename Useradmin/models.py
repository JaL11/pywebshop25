from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    USER_TYPES = [
        ("SU", "superuser"),
        ("CS", "customer service"),
        ("CU", "customer")
    ]

    type = models.CharField(max_length=2,
                            choices=USER_TYPES,
							default='CU',
                            )
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)

