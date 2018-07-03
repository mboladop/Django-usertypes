from django.shortcuts import render
from .forms import UserLoginForm, UserRegistrationForm
# Create your views here.
def get_home(request):
    return render(request,"index.html")
    
def login(request):
    form = UserLoginForm()
    return render(request, "accounts/login.html", {'form': form})
    
def register(request):
    form = UserRegistrationForm()
    return render(request, "accounts/register.html", {'form': form})