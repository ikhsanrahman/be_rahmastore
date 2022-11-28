from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import *
from django.contrib.auth.models import User


class HomeUserView(viewsets.ViewSet):
    def list(self, request):
        return Response("welcome")

# class UserRegisterView(viewsets.ViewSet):
#     def create(self, request):
#         responses = {}
#         data = request.data
#         serializer = UserRegisterSerializer(data=data, many=True)

#         user = User.objects.filter(email=data['email'])

#         if not user and serializer.is_valid():
#             new_user = User(email=data['email'], username=data['username'], password=data['password'])
#             new_user.generate_password_hash(data['password'])
#             new_user.created_at = TIME
#             new_user.save()
#             responses['msg'] = "User Created Succesfully"
#             return Response(responses)

#         return Response("user is already existed")

# class UserLogoutView(viewsets.ViewSet):
#     @user_token_required
#     def list(self, request, user_uuid):
#         token = request.headers.get('Authorization')
#         responses = {}
#         user = User.objects.get(id=user_uuid, is_login=True)
#         blacklisted = BlacklistToken.objects.filter(token=token)
#         if user and not blacklisted:
#             new_blacklisted = BlacklistToken(token=token)
#             new_blacklisted.blacklisted_on = TIME
#             new_blacklisted.save()
#             user.is_login = False
#             user.logout_at = TIME
#             user.save()
            
#             responses['msg'] = "User is already logout"
#             return Response(responses)

#         return Response("user is not valid")


# class UserLoginView(viewsets.ViewSet):
#     def create(self, request):
#         responses = {}
#         data = request.data
#         user = User.objects.get(is_login=False, email=data['email'])
#         # serializer = UserLoginSerializer(data)
        
#         if user and user.check_password_hash(data['password']):
#             user.is_login = True
#             user.login_at = TIME

#             auth_token = user.encode_auth_token(str(user.id))

#             responses['token'] = auth_token.decode()
#             responses['user_uuid'] = user.id
#             user.save()
#             return Response(responses)

#         return Response("user is not valid")

#     # def retrieve(self, request, pk=None):
#     #     queryset = User.objects.all()
#     #     user = get_object_or_404(queryset, pk=pk)
#     #     serializer = UserSerializer(user)
#     #     return Response(serializer.data)

# class GetOneProductView(viewsets.ViewSet):
#     @user_token_required
#     def retrieve(self, request, user_uuid):
#         data = request.data
#         product = Product.objects.filter(code=data['code'] )
#         user = User.objects.filter(id=user_uuid)
#         serializer = ListProductSerializer(product)
#         if product and user and serializer.is_valid():
#             return Response(serializer.data)
#         return Response("user doesn't has authorization")

# class ActivateProductView(viewsets.ViewSet):
#     @user_token_required
#     def list(self, request, user_uuid, product_uuid):
        
#         product = Product.objects.get(id=product_uuid, is_active=False, user_id=user_uuid)

#         if product:
#             product.is_active = True
#             product.save()
#             return Response("product has been activated")
#         return Response("some thing not authorized")

# class UnactivateProductView(viewsets.ViewSet):
#     @user_token_required
#     def list(self, request, user_uuid, product_uuid):
#         # user = User.objects.filter(id=user_uuid)
#         product = Product.objects.get(id=product_uuid, is_active=True, user=user_uuid)
#         # serializer = ListProductSerializer(data=product)
#         if product :
#             product.is_active = False
#             product.save()
#             return Response("product has been unactivated")
#         return Response("some thing not authorized")

# class AddProductView(viewsets.ViewSet):
#     @user_token_required
#     def create(self, request, user_uuid):
#         responses = {}

#         data = request.data
#         serializer = ProductSerializer(data=data, many=True)
#         user = User.objects.get(id=user_uuid)
#         product = Product.objects.filter(name=data['name'])
        
#         if not product and serializer.is_valid() and user:
#             new_product = Product(name=data['name'], description=data['description'], amount=data['amount'],
#                 price=data['price'], user=user)
#             productPicture = ProductPicture(filename=data['file'].name, image=data['file'], product=new_product)
#             productPicture.save()
#             new_product.save()
#             responses['product_uuid'] = new_product.id
#             responses['msg'] = "product added successfully"
#             return Response(responses)
#         responses['msg'] = "can not add product. product name is same"
#         return  Response(responses)

# class UpdateProductView(viewsets.ViewSet):
#     @user_token_required
#     def update(self, request, user_uuid=None, product_uuid=None):
#         responses = {}
#         data = request.data
#         serializer = UpdateProductSerializer(data=data, many=True)
#         user = User.objects.filter(id=user_uuid)
#         product = Product.objects.get(id=product_uuid)
#         if user and serializer.is_valid() and product:
#             product.name = data['name']
#             product.price = data['price']
#             product.amount = data['amount']
#             product.description = data['description']
#             product.save()
#             responses['msg'] = "update product has been succeed"
#             return Response(responses)
#         return Response("update product is not valid")
