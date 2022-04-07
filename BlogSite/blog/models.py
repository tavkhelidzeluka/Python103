from calendar import c
import re
from django.db import models
from django.urls import reverse
from users.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    thumbnail = models.ImageField(upload_to='blog/post_thumbnail/')
    category = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:post-details', kwargs={'pk': self.pk})
    
    @staticmethod
    def get_recent_posts():
        return Post.objects.order_by('-created_at').all()[:3]


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

class Tag(models.Model):
    title = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)


