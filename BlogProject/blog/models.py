from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# DRY Principle - Don't Repeat Yourself

# ORM - Object Relational Mapper
class Post(models.Model):
    # Relations 
    # One to Many
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=255)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True) 

    def __str__(self) -> str:
        return f'{self.title} - {self.author}'
