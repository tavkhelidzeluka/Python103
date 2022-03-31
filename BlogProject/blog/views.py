from django.shortcuts import redirect, render
from django.http import HttpRequest, HttpResponse
from django.urls import reverse, reverse_lazy
from blog.forms import PostCreateForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views import View
from django.views.generic import CreateView, ListView


from blog.models import Post


# GET
def home_view(request: HttpRequest) -> HttpResponse:
    posts = Post.objects.all()
    
    return render(request, 'home.html', {
        # 'number': 5,
        'posts': posts
    }) 

class PostListView(ListView):
    queryset = Post.objects.all()
    template_name = 'home.html'
    context_object_name = 'posts'

def about_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'about.html')


@login_required(redirect_field_name='home')
def post_create_view(request: HttpRequest) -> HttpResponse:
    print(request.user)
    # if not request.user.is_authenticated:
    #     return redirect(reverse('home'))


    if request.method == 'POST':
        print(request.POST)
        Post.objects.create(author=request.user, title=request.POST['title'], body=request.POST['body'])

    return render(request, 'post_create.html', {
        'form': PostCreateForm()
    })


def get_post_details(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)

    return render(request, 'post_details.html', {
        'post': post
    })


def register_view(request: HttpRequest) -> HttpResponse:

    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        print(form.data)
        if form.is_valid():
            form.save()

    return render(request, 'post_create.html', {
        'form': form
    })


# class RegisterView(View):
#     def get(self, request):
#         return render(request, 'post_create.html', {
#             'form': UserCreationForm()
#         })

#     def post(self, request):
#         form = UserCreationForm(request.POST)
#         print(form.data)
#         if form.is_valid():
#             form.save()

#         return render(request, 'post_create.html', {
#             'form': form()
#         }) 


class RegisterView(CreateView):
    model = User
    # fields = ['username', 'email', 'password']
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
