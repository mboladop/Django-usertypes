from django.urls import path
from .views import *

urlpatterns = [
    path('login/', login, name='login'),
    path('register/buyer', register_buyer, name= 'register_buyer'),
    path('register/seller', register_seller, name= 'register_seller'),
    path('logout/', logout, name= 'logout'),
    path('profile/', profile, name= 'profile'),
    path('', get_home, name = 'home'),
]
