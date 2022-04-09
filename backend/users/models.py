from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    user_name = models.CharField(max_length=64)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField(default=2000)
    email = models.EmailField(max_length=64, unique=True, default=None)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)


    def __str__(self):
        return self.user_name