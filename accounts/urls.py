from django.urls import path
from .views import login, get_home, register

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name= 'register'),
    path('', get_home, name = 'home'),
]
