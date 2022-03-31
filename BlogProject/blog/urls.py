from django.urls import path
from blog.views import about_view, home_view, post_create_view, get_post_details, RegisterView, PostListView

from django.views.generic import TemplateView


urlpatterns = [
    # path('', home_view, name='home'),
    path('', PostListView.as_view(), name='home'),
    # path('about/', about_view, name='about'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),

    path('post/add/', post_create_view, name='post-create'),
    path('posts/<int:pk>/', get_post_details, name='post-details'),
    # path('register/', register_view)
    path('register/', RegisterView.as_view())

]
