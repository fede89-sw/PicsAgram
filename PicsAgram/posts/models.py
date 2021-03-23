from django.conf import settings
from django.db import models

# Create your models here.


class Post(models.Model):
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=240, null=True, blank=True)
    author = models.ForeignKey( settings.AUTH_USER_MODEL,
                                on_delete=models.CASCADE,
                                related_name="posts")
    voters = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                    related_name="votes")

    def __str__(self):
        return self.description


class Answer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    content = models.TextField()
    post = models.ForeignKey( Post,
                              on_delete=models.CASCADE,
                              related_name="answers")
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username