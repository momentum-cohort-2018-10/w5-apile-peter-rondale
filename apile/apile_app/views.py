import csv, io
from django.shortcuts import render
from apile_app.models import Post
from django.template.defaultfilters import slugify

# Create your views here.

def index(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {
        'posts': posts,
    })

def create_post(request):
    form_class = PostForm
    if request.method == 'POST':
        form = form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.slug = slugify(post.name)
            post.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = form_class()

    return render(request, 'posts/create_post.html', {
        'form': form,
    })