
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login


def home(request):
    return render(request, 'index.html')

def shop_view(request):
    return render(request, 'shop.html')

def cart_view(request):
    return render(request, 'cart.html')


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

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  # Assuming you're using Django's UserCreationForm or similar
            email = form.cleaned_data.get('email', '')  # Email is optional based on your form definition
            phonenumber = form.cleaned_data.get('phonenumber', '')  # Optional based on your form definition

            # Check if user already exists
            if not User.objects.filter(username=username).exists():
                user = User.objects.create(username=username, password=password)
                # Assuming you have a profile or similar model for extra fields like phonenumber
                user.phonenumber = phonenumber  # Adjust based on your user model
                user.save()

                # Log the user in and redirect to home
                login_user = authenticate(request, username=username, password=password)
                return redirect('home')  # Redirect to a success page.
            else:
                form.add_error(None, 'Username already exists')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

