from django.contrib import admin

from blog.models import Post

@admin.register(Post)
class PostAdminModel(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['title', 'author']

    
# admin.site.register(Post)
