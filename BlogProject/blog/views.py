from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

from blog.models import Post


# GET
def home_view(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    
    return render(request, 'home.html', {
        # 'number': 5,
        'posts': posts
    }) 


def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


