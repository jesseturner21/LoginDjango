
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from .models import User
from django.contrib import messages


def home(request):
    return render(request, "index.html")

def home(request):
    return render(request, "base.html")


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(username=username, password=password)
               
                return redirect('home')  # Assuming you have a URL named 'home'
            except User.DoesNotExist:
                form.add_error(None, 'Username or password is incorrect')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

