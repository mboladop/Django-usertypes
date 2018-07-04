from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Buyer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'buyer')
    numbervalue = models.IntegerField(default=0, null=False)
    stringvalue = models.CharField(max_length=50, default= 'unknown', null= False, blank= False)
    
    
    def __str__(self):
        return self.user.username
        
        
class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'seller')
    verified = models.BooleanField(default=False)
    joined = models.DateField(auto_now_add=True)
    
    
    def __str__(self):
        return self.user.username