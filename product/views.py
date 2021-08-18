from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from config.config import Config

from .serializer import *
from user.models import MyUser
from product.models import Product



TIME = Config().time()

# Create your views here.

class DisplayProductView(viewsets.ViewSet):
	def list(self, request):
		responses = {}
		products = Product.objects.all()			
		serializer = ListProductSerializer(products, many=True)
		return Response(serializer.data)

#list by user or admin
class ListProductView(viewsets.ViewSet):
	def list(self, request, user_uuid=None):
		responses = {}
		products = Product.objects.all()
		user = MyUser.objects.filter(user_uuid=user_uuid)
		if user:			
			serializer = ListProductSerializer(products, many=True)
			return Response(serializer.data)
		return Response("can not retrieve products")


# search by admin using code
class searchProduct(viewsets.ViewSet):
	def get(self, request, buyer_uuid):
		data = request.data
		buyer = Buyer.objects.filter(buyer_uuid=buyer_uuid)
		product = Product.objects.filter(product_uuid=product_uuid)
		serializer = Product.objects.filter()

