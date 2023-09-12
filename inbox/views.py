from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm, LoginForm

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            return redirect('welcome', email=email)
    else:
        form = UserRegisterForm()
    return render(request, 'inbox/register.html', {'form': form})

def welcome(request, email):
    return render(request, 'inbox/welcome.html', {'email': email})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'inbox/login.html', {'form': form})

def resetPassword(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'inbox/reset-password.html', {'form': form})

def index(request):
    return render(request, 'inbox/index.html')

def report(request):
    return render(request, 'inbox/report.html')