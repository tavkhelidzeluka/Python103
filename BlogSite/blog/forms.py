from this import d
from django import forms
from users.models import User

from blog.models import Comment, Post


class PostCreateFrom(forms.ModelForm):
    
    def save(self, user: User, commit: bool = False):
        post = super().save(False)

        post.user = user

        if commit:
            post.save()

        return post

    class Meta:
        model = Post
        exclude = ['user']


class PostModifyFrom(forms.ModelForm):

    class Meta:
        model = Post
        exclude = ['user']


class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'body']
        
        widgets = {
            'post': forms.HiddenInput()
        }
