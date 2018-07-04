from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from .forms import UserLoginForm, UserRegistrationForm, SellerRegistrationForm, BuyerRegistrationForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.
def get_home(request):
    return render(request, "index.html")
    

def login(request):
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            u = login_form.cleaned_data['username_or_email']
            p = login_form.cleaned_data['password']
            user = authenticate(username=u, password=p)
    
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                login_form.add_error(None, "Your username or password are incorrect")
    else:
        login_form = UserLoginForm()

    return render(request, 'accounts/login.html', {'form': login_form})
    


def register_buyer(request):
    
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        buyer_form = BuyerRegistrationForm(request.POST, request.FILES)
        
        if user_form.is_valid() and buyer_form.is_valid():
            user = user_form.save()
            buyer = buyer_form.save(commit=False)
            buyer.user = user
            buyer.save()
            
            u = user_form.cleaned_data['username']
            p = user_form.cleaned_data['password1']
            user = authenticate(username=u, password=p)
            
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                user_form.add_error(None, "Can't log in now, try later.")
    else:
        user_form = UserRegistrationForm()
        buyer_form = BuyerRegistrationForm()

    return render(request, "accounts/register.html", {'user_form': user_form, 'user_type_form': buyer_form})
    
def register_seller(request):
    
    if request.method == "POST":
        user_form = UserRegistrationForm(request.POST)
        seller_form = SellerRegistrationForm(request.POST, request.FILES)
        
        if user_form.is_valid() and seller_form.is_valid():
            user = user_form.save()
            seller = seller_form.save(commit=False)
            seller.user = user
            seller.save()
            
            u = user_form.cleaned_data['username']
            p = user_form.cleaned_data['password1']
            user = authenticate(username=u, password=p)
            
            if user is not None:
                auth.login(request, user)
                return redirect("/")
            else:
                user_form.add_error(None, "Can't log in now, try later.")
    else:
        user_form = UserRegistrationForm()
        seller_form = SellerRegistrationForm()

    return render(request, "accounts/register.html", {'user_form': user_form, 'user_type_form': seller_form})
    
def logout(request):
    auth.logout(request)
    return redirect('/')    
    
@login_required(login_url="/accounts/login")
def profile(request):
    return render(request, "accounts/profile.html")
