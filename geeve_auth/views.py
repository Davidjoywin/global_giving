from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

from .forms import UserCreation

def register_user(request):
    new_user = UserCreation()
    if request.method == 'POST':
        new_user = UserCreation(request.POST)
        if new_user.is_valid():
            new_user.save()
            user=authenticate(request, username=request.POST.get("username"), password=request.POST.get("password1"))
            # user=authenticate(request, username=new_user.data.get("username"), password=new_user.data.get("password1"))
            login(request, user)
            return redirect("geeve:home")
        
        messages.error(request, "Used Username or invalid Password!")
        return redirect("auth:signup")

    context = {
        "new_user_form": new_user
    }

    if request.user.is_authenticated:
        return redirect("geeve:home")
    return render(request, "auth/sign_up.html", context)

def login_user(request):
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")

        user=authenticate(request, username=username, password=password)
        login(request, user)

        return redirect("geeve:home")

    if request.user.is_authenticated:
        return redirect("geeve:home")
    return render(request, "auth/login.html")

def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("geeve:home")
    else:
        return redirect("geeve:home")
