from django.http import HttpResponse
from django.shortcuts import render

from .models import Post
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def home(request):

    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


def post(request):

       return render(request, 'blog/new_post.html', {'title': 'About'})