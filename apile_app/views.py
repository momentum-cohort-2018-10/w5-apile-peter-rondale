import csv, io
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.http import require_POST
from apile_app.models import Post, Comment, Vote
from apile_app.forms import PostForm, CommentForm
from django.db.models import Count
from django.contrib.auth.views import login_required
from django.views.decorators.http import require_POST
from django.contrib import messages
# Create your views here.

def index(request):
    posts = Post.objects.all()
    posts = posts.annotate(num_of_votes=Count('votes'))
    voted_posts = []
    if request.user.is_authenticated:
        voted_posts = request.user.voted_posts.all()
    return render(request, 'index.html', {
        'posts': posts,
        'voted_posts': voted_posts,
    })

def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    comments = post.comments.all()
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
        'comments': comments,
        'slug': slug,
    })

@login_required
@require_POST
def post_delete(request, slug):
    post = Post.objects.get(slug=slug)
    if request.user == post.author:
        post.delete()
    return redirect('home')

@login_required
@require_POST
def comment_delete(request, slug, description):
    comment = Comment.objects.get(description=description)
    if request.user == comment.author:
        comment.delete()
    return redirect('home')



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
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_comment.html', {'form': form})



@require_POST                   #Have to submit form to access
@login_required
def switch_vote(request, post_id):
    post = Post.objects.get(pk=post_id)
    if post in request.user.voted_posts.all():
        post.votes.filter(author=request.user).delete()
        message = "I don't like this post!"
    else:
        post.votes.create(author=request.user)
        message = "I like this post!"

    messages.add_message(request, messages.SUCCESS, message)
    return redirect(to='home')