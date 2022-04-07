from asyncio.proactor_events import _ProactorSocketTransport
from django.urls import path
from blog.views import home_view, post_create_view, post_delete_view, post_detail_view, post_list_view, post_modify_view, create_comment_view

app_name = 'blog'
urlpatterns = [
    path('', home_view, name='home'),
    path('create/post/', post_create_view, name='post-create'),
    path('posts/', post_list_view, name='post-list'),
    path('posts/<int:pk>/', post_detail_view, name='post-details'),
    path('posts/<int:pk>/delete/', post_delete_view, name='post-delete'),
    path('posts/<int:pk>/modify/', post_modify_view, name='post-modify'),
    path('posts/add/comment/', create_comment_view, name='comment-create')
]
