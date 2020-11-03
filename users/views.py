from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from blog.views import Post 


def register(request):
    #GET we disply the form 
    #POST we save the data

    context = { }

    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid(): 
            username  = form.cleaned_data.get("username")
            messages.success(request, f"Your account has benne created! You are now able to log in") #flash message
            form.save() #saves the data in the DB
            return redirect('login') #redirect to the home page if success
            
    else: 
        form = UserRegisterForm()
      
    context = {
        'form': form,
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')



def user_detail(request, pk):
    user = get_object_or_404(User, pk=pk)
    posts = Post.objects.filter(author = user)

    context = {
        'user': user, 
        'posts': posts,
    }
    return render(request, 'users/user_detail.html', context)