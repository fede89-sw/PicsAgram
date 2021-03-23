from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):

    biography = models.CharField(max_length=240, null=True, blank=True)
    profile_picture = models.ImageField(null=True, blank=True)
    theme = models.CharField(max_length=100)
    
