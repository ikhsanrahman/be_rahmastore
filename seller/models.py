from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Shop(models.Model):
    """
    Shop Model for database.
    user only have one shop to open
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="user has one shop only")
    shop_name = models.CharField(null=True, blank=True)
    upload = models.FileField(upload_to='uploads/shop/')
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True) 
    phone_number = models.CharField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True, auto_now=True)
