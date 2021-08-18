import uuid

from django.db import models

# from user.models import MyUser
from utilization.utils import code_item_generator
# from buyer.models import Cart
from django.conf import settings



# Create your models here.

def uid():
  return uuid.uuid4()

class Product(models.Model):

    id                          = models.UUIDField(primary_key=True, default=uid(), unique=True)
    code                        = models.CharField(max_length=255, unique=True, default=code_item_generator(), blank=True)
    name                        = models.CharField(max_length=255, blank=True)
    description                 = models.TextField()
    amount                      = models.IntegerField(default=0)
    price                       = models.IntegerField(default=0)
    is_active                   = models.BooleanField(default=True)
    number_sold                 = models.IntegerField(default=0)
    number_seen                 = models.IntegerField(default=0)
    number_bought               = models.IntegerField(default=0)
    created_at                  = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at                  = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    deleted_at                  = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    user                        = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart                        = models.ForeignKey('buyer.Cart', on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return "<this is {}".format(self.name)

    def __repr__(self):
        return "<this is {}".format(self.name)

class ProductPicture(models.Model):

    id                          = models.UUIDField(primary_key=True, default=uid(), unique=True)
    filename                    = models.CharField(max_length=255, blank=False)
    image                       = models.ImageField(upload_to='images/', blank=True)
    is_active                   = models.BooleanField(default=True)
    created_at                  = models.DateTimeField(auto_now_add=True, null=True)
    product                     = models.ForeignKey(Product, on_delete=models.CASCADE)
    deleted_at                  = models.DateTimeField(auto_now_add=False, null=True)

    class Meta:
        ordering = ['created_at']

    def __str__(self):
        return "<this picture {} is belong to {}>".format(self.filename, self.product.name)

    def __repr__(self):
        return "<this picture {} is belong to {}>".format(self.filename, self.product.name)
