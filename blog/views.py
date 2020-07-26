from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

posts  =[
    {
        'author': 'Alessio', 
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'today'
    },

     {
        'author': 'Luca', 
        'title': 'Blog Post 2',
        'content': 'Seconde post content',
        'date_posted': 'yesterday'
    },
]

def home(request):
    context = {
        'posts': posts, 
        'title': 'ciccio bello'
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
