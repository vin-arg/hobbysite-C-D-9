from django.shortcuts import render, redirect
from django.contrib.auth import login
from .models import Profile
from .forms import RegisterForm

def home_page(request):
    return render(request, 'home.html')

def profile(request):
    return render(request, "profile.html")

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, name=user.username, email=user.email)
            login(request, user)
            return redirect('home_page')   
    return render(request, 'registration/register.html', {'regform': form})