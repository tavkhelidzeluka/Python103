from django.urls import path
from blog.views import about_view, home_view


urlpatterns = [
    path('', home_view),
    path('about/', about_view)
]
