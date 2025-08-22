from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required, user_passes_test
from .decorators import librarian_required, student_required
from .models import User


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # By default har user student hoga
            user.is_staff = False
            user.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "signup.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")
    

def logout_view(request):
    logout(request)
    return redirect("login")



def librarian_required(view_func):
    return user_passes_test(lambda u: u.is_staff)(view_func)

@login_required
def dashboard(request):
    if request.user.is_staff:
        return redirect("librarian_dashboard")
    else:
        return redirect("student_dashboard")
    

@librarian_required
def librarian_dashboard(request):
    return render(request, 'lb_dashboard.html')

@student_required
def student_dashboard(request):
    return render(request, 'st_dashboard.html')

def accounts(request):
    return render(request, 'accounts.html')
