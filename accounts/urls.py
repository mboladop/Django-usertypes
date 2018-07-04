from django.urls import path
from .views import login, get_home, register, profile, logout

urlpatterns = [
    path('login/', login, name='login'),
    path('register/', register, name= 'register'),
    path('logout/', logout, name= 'logout'),
    path('profile/', profile, name= 'profile'),
    path('', get_home, name = 'home'),
]
