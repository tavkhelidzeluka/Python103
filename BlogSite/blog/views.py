from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from blog.forms import PostCreateFrom, PostModifyFrom
from blog.models import Post
from django.contrib.auth.decorators import login_required


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {
        'post_list': Post.objects.order_by('-created_at').all()[:3],
        'post_form': PostCreateFrom()
    })

def post_list_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog.html', {
        'post_list': Post.objects.all()
    })


def post_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'post-details.html', {
        'post': get_object_or_404(Post, pk=pk)
    })


@login_required
def post_create_view(request: HttpRequest) -> HttpResponse:
    if request.method != 'POST':
        return redirect('blog:home')

    form = PostCreateFrom(request.POST, request.FILES)
    
    if form.is_valid():
        post = form.save(request.user, True)
        return redirect('blog:post-details', post.pk)
    # print(form.errors)
    return redirect('blog:home')


@login_required
def post_delete_view(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.user:
        return redirect('blog:home')
    
    post.delete()
    return redirect('blog:home')


@login_required
def post_modify_view(request: HttpRequest, pk: int) -> HttpResponse:
    post = get_object_or_404(Post, pk=pk)

    if request.user != post.user:
        return redirect('blog:home')
    form = PostModifyFrom(instance=post)
    print(request.method)
    if request.method == 'POST':
        form = PostModifyFrom(request.POST, request.FILES, instance=post)
        
        if form.is_valid():
            form.save(True)

            return redirect('blog:post-details', pk)
    
    return render(request, 'post-edit.html', {
        'post_form': form
    })

