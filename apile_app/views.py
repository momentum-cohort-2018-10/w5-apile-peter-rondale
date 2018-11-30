import csv, io
from django.shortcuts import redirect
from django.shortcuts import render
from apile_app.models import Post, Comment, Vote
from apile_app.forms import PostForm, CommentForm
from django.contrib.auth.views import login_required
# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
    })

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', slug)
    else:
        form = CommentForm()
    return render(request, 'post_detail.html', {
        'post': post,
        'form': CommentForm(),
        'comments': post.comment_set.all()
    })

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
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

@login_required
def switch_vote(request):
    pass

def post_vote(request):
    post = Post.objects.get(slug=slug) #retrieves the post by slug
    post.vote.add(request.user) #will know that the logged in user liked the post
    return redirect('home') #redirects user to homepage
