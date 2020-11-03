from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from .models import Post
from .forms import PostForm


# Create your views here.


@login_required
def home(request):

    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.post_date = timezone.now()

            post.save()
            return redirect('blog-home')
    else:
        form = PostForm()

        context = {
            'form': form
        }

    return render(request, 'blog/new_post.html', context)

@login_required
def user_posts_count(request):
    posts = Post.objects.all()

    posts_count = {}
    for post in posts:
        if post.author not in posts_count:
            posts_count[post.author] = 1
        else:
            posts_count[post.author] += 1
    context = {
        'users_post_count': posts_count,
    }

    return render(request, 'blog/user_posts_count.html', context)

