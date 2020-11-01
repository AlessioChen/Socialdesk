from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone

# Create your views here.


@login_required
def home(request):

    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


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


def user_posts_count(request):
    posts = Post.objects.all()

    user_posts_count = {}
    for p in posts:
        if p.author not in user_posts_count:
            user_posts_count[p.author] = 1
        else:
            user_posts_count[p.author]+=1
    context = {
        'users_post_count': user_posts_count,
    }

 
    return render(request, 'blog/user_posts_count.html', context)
