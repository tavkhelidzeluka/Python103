from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render

from users.forms import UserLoginForm
from django.contrib.auth import authenticate
from users.models import User
from django.contrib.auth import login as auth_login, logout as auth_logout


def login_view(request: HttpRequest) -> HttpResponse:
    if request.user.is_authenticated:
        return redirect('blog:home')

    form = UserLoginForm()

    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                auth_login(request, user)
                return redirect('blog:home')
            
            form.add_error('password', 'Check Password')

    return render(request, 'auth/login.html', {
        'form': form
    })


def logout_view(request: HttpRequest) -> HttpResponse:
    auth_logout(request)
    return redirect('blog:home')
