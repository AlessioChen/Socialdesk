from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import JsonResponse, HttpResponseNotFound
from datetime import timedelta

from .models import Post
from .forms import PostForm
import redis


# CONFIG FOR REDIS SERVER
SERVER_IP = '127.0.0.1'
SERVER_PORT = '6379'
PASSWORD = ''
DB = 0


@login_required
def home(request):
    
    
    error = False
    user_email = request.user.email

    # Create connection to the Redis DB
    client = redis.StrictRedis(host=SERVER_IP, 
                                port=SERVER_PORT, 
                                password=PASSWORD,
                                db=DB,
                                charset="utf-8", 
                                decode_responses=True)
  
    # Client last ip 
    last_ip = client.get(user_email)
    # Client current ip
    current_ip = request.META['REMOTE_ADDR']
    if current_ip != last_ip :
        client.set(user_email, current_ip)
        if current_ip != None: 
            error = True
  
    context = {
        'posts': Post.objects.all(),
        'error': error
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
            
            if 'hack' in post.content: 
                return HttpResponseNotFound('There is a no valid word in the post content!')
            
            # it writes the content on th Ropsten 
            post.write_on_chain()
            print('content written in Block successfuly')
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



def last_hour_posts(request):
    this_hour = timezone.now().replace(minute = 0, second =0, microsecond = 0)
    one_hour_later = this_hour + timedelta(hours=1)
    posts = Post.objects.filter(post_date__range=(this_hour, one_hour_later))

    data = { }
    for p in posts: 
        d = { 
            'title': p.title, 
            'content': p.content, 
            'post_date': p.post_date, 
            'author': p.author.username,
            'hash': post.hash,
            'transaction ID': post.txId,
        }
        data[p.id] = d 


    return JsonResponse(data, safe = False)


def word_count(request):
    context = { }
    
    context['show']=False
    if request.GET:
        word = request.GET['word']
        posts = Post.objects.all()

        count = 0 

        for p in posts: 
            count += int(p.content.count(word))
        
        context['count'] = count 
        context['word'] = word 

        

    
    return render(request, 'blog/word_count.html', context)