from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, RegisterForm
from .models import User
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate, login

# View for homepage
def home(request):
    return render(request, 'index.html')

# View for shop page
def shop_view(request):
    return render(request, 'shop.html')

# View for cart page
def cart_view(request):
    return render(request, 'cart.html')

# View for user login
def login_view(request):
    # If request is POST, create login form
    if request.method == 'POST':
        form = LoginForm(request.POST)
        # If form is valid, extract the username and password
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            # Try to get username or password from database
            try:
                user = User.objects.get(username=username, password=password)
               
                return redirect('home')  
            # Error is username or password is not found
            except User.DoesNotExist:
                form.add_error(None, 'Username or password is incorrect')
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {'form': form})

# View for user registration
def register_view(request):
    # If request is POST, create registration form
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        # If form is valid, extract the information
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']  
            email = form.cleaned_data.get('email', '') 
            phonenumber = form.cleaned_data.get('phonenumber', '') 

            # Check if user already exists
            if not User.objects.filter(username=username).exists():
                user = User.objects.create(username=username, password=password)
                user.phonenumber = phonenumber 
                user.save()
                login_user = authenticate(request, username=username, password=password)
                return redirect('home')
            else:
                form.add_error(None, 'Username already exists')
    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})

