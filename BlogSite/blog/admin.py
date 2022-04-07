from django.contrib import admin
from blog.models import Post, Comment, Tag

@admin.register(Tag)
class TagAdminModel(admin.ModelAdmin):
    filter_horizontal = ('posts', )

admin.site.register([Post, Comment])
