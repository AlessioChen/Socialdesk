from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    #GET we disply the form 
    #POST we save the data

    context = { }

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            username  = form.cleaned_data.get("username")
            messages.success(request, f"Account created for {username}!")

            return redirect('blog-home') #redirect to the home page if success
            
    else: 
        form = UserCreationForm()
        context = {
            'form': form
        }
    
    return render(request, 'users/register.html', context)