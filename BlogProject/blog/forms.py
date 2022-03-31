from django import forms
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password

# class PostCreateForm(forms.Form):
#     title = forms.CharField(max_length=255)
#     body = forms.CharField(widget=forms.Textarea)

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Post
        # fields = ['title', 'body']
        exclude = ['author']



class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
    
    def save(self, commit: bool = ...):
        user: User = super().save(commit=False)

        user.password = make_password(user.password)
        if commit:
            user.save()
        return user
