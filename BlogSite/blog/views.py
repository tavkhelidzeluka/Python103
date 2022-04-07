from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from blog.forms import CommentCreateForm, PostCreateFrom, PostModifyFrom
from blog.models import Post, Comment
from django.contrib.auth.decorators import login_required


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'index.html', {
        'post_list': Post.get_recent_posts(),
        'post_form': PostCreateFrom()
    })

def post_list_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'blog.html', {
        'post_list': Post.objects.all()
    })


def post_detail_view(request: HttpRequest, pk: int) -> HttpResponse:
    return render(request, 'post-details.html', {
        'post': get_object_or_404(Post, pk=pk),
        'comments': Comment.objects.filter(post__pk=pk),
        'comment_form': CommentCreateForm()
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


@login_required
def create_comment_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        return redirect('blog:home')

    form = CommentCreateForm(request.POST)
    post_pk = request.POST.get('post')
    get_object_or_404(Post, pk=post_pk)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()
        print()
        return redirect('blog:post-details', post_pk)
    print(form.errors)
    return render(request, 'post-details.html', {
        'post': get_object_or_404(Post, pk=post_pk),
        'comments': Comment.objects.filter(post__pk=post_pk),
        'comment_form': form
    })

