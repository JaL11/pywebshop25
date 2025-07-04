from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    USER_TYPES = [
        ("SU", "superuser"),
        ("CS", "customer service"),
        ("CU", "customer")
    ]


