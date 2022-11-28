import uuid

from django.db import models
from utilization.utils import code_item_generator
from django.conf import settings
from seller.models import Shop
from utilization.utils import code_item_generator


# Create your models here.
# def gen_uid():
#   return uuid.uuid4()

# class Product(models.Model):
#     """
#     Poduct database model.
#     one shop can have many product to added
#     """

#     shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
#     id = models.UUIDField(primary_key=True, default=gen_uid(), unique=True)
#     code = models.CharField(max_length=255, unique=True, default=code_item_generator(), blank=True)
#     name = models.CharField(max_length=255, blank=True)
#     description = models.TextField(blank=True, null=True)
#     upload = models.FileField(upload_to='uploads/')
#     category = models.CharField(max_length=300, null=True, blank=True)
#     stock = models.IntegerField(default=0)
#     price = models.IntegerField(default=0)
#     size = models.CharField(max_length=150, null=True, blank=True)
#     color = models.CharField(max_length=150, null=True, blank=True)
#     is_dangerous = models.BooleanField(default=True)
#     number_view = models.IntegerField(default=0)
#     created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
#     updated_at = models.DateTimeField(auto_now_add=False, null=True, blank=True)
#     # cart = models.ForeignKey('buyer.Cart', on_delete=models.CASCADE, null=True)

#     class Meta:
#         ordering = ['name']

#     def __str__(self):
#         return "<this is {}".format(self.name)

#     def __repr__(self):
#         return "<this is {}".format(self.name)

