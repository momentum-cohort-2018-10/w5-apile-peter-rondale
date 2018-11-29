import csv, io
from django.shortcuts import redirect
from django.shortcuts import render
from apile_app.models import Post
from apile_app.forms import PostForm
from django.contrib.auth.views import login_required
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
    })

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'post_detail.html', {
        'post': post,
    })

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.slug = slug
            # post.date_added = datetime.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_create.html', {'form': form})

def comment_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # post.slug = slug
            # post.date_added = datetime.now()
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_comment.html', {'form': form})