from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from utilization.decorator import buyer_token_required

# Create your views here.

# class BuyerRegisterView(viewsets.ViewSet):
# 	def create(self, request):
# 		responses = {}
# 		data = request.data
# 		serializer = BuyerRegisterSerializer(data, many=True)

# 		buyer = Buyer.objects.get(email=data['email'])

# 		if serializer.is_valid() and not buyer:
# 			new_buyer = Buyer(fullname=data['fullname'], password=data['password'], email=data['email'], gender=data['gender'],
# 				address_line1=data['address_line1'], address_line2=data['address_line2'], house_no=data['house_no'], 
# 				phone_number=data['phone_number'], postal_code=data['postal_code'], city=data['city'], province=data['province'],
# 				country=data['country'])
# 			new_buyer.save()
# 			responses['msg'] = "new buyer has been added"
# 			return Response(responses)
# 		return Response("can not create account, try again")

# class BuyerLoginView(viewsets.ViewSet):
# 	def list(self, request):
# 		responses = {}
# 		data = request.data
# 		serializer = BuyerLoginSerializer(data)
# 		buyer = Buyer.objects.filter(email=data['email'], is_login=False)

# 		if serializer.is_valid() and buyer.check_password_hash(data['password']):
# 			buyer.time_login = TIME
# 			auth_token = buyer.encode_auth_token(buyer.buyer_uuid)
# 			responses['token'] = auth_token.decode()
# 			return Response(responses)

# 		return Response("can not login, try again")

# class BuyerResetPasswordView(viewsets.ViewSet):
# 	def partial_retrieve(self, request):
# 		responses = {}
# 		data = request.data
# 		buyer = Buyer.objects.filter(email=data['email'])
# 		serializer = BuyerResetPassword
# 		if buyer and serializer.is_valid():
# 			buyer.password = data['password']
# 			buyer.generate_password_hash(data['password'])
# 			buyer.save()
# 			responses['msg'] = "reset password succeed"
# 			return Response(responses)
# 		return Response("can not reset password, try again")

# class BuyerUpdateProfileView(viewsets.ViewSet):
# 	@buyer_token_required
# 	def update(self, request, buyer_uuid):
# 		responses = {}
# 		data = request.data
# 		serializer = BuyerUpdateProfileSerializer(data)
# 		buyer = Buyer.objects.filter(buyer_uuid=buyer_uuid, is_login=True)
# 		if buyer and serializer.is_valid():
# 			buyer.fullname = data['fullname']
# 			buyer.gender = data['gender']
# 			buyer.address_line1 = data['address_line1']
# 			buyer.address_line2 = data['address_line2']
# 			buyer.house_no = data['house_no']
# 			buyer.phone_number = data['phone_number']
# 			buyer.postal_code = data['postal_code']
# 			buyer.city = data['city']
# 			buyer.province = data['province']
# 			buyer.country = data['country']
# 			buyer.save()
# 			responses['msg'] = "update profile succeed"
# 			return Response(responses)
# 		return Response("can not update profile, check again")

# class BuyerLogoutView(viewsets.ViewSet):
# 	@buyer_token_required
# 	def list(self, request, buyer_uuid):
# 		responses = {}
# 		data = request.data
# 		buyer = Buyer.objects.filter(buyer_uuid=buyer_uuid, is_login=True)
# 		token = BlacklistToken.objects.filter(token=data['token'])
# 		if buyer and not token:
# 			buyer.is_login = False
# 			buyer.time_logout = TIME
# 			new_blacklisted = BlacklistToken(token=data['token'])
# 			buyer.save()
# 			new_blacklisted.save()
# 			responses['msg'] = "buyer is already logout"
# 			return Response(responses)
# 		return Response("user is not valid")

# class BuyerSearchProductView(viewsets.ViewSet):
# 	def get(self, request, buyer_uuid):
# 		responses = {}
# 		data = request.data
# 		buyer = Buyer.objects.filter(buyer_uuid=buyer_uuid, is_login=True)



class BuyerSeeProductView(viewsets.ViewSet):
	@buyer_token_required
	def retrieve(self, request, buyer_uuid, product_uuid):
		data = request.data
		buyer = Buyer.objects.filter(buyer_uuid=buyer_uuid)
		product = Product.objects.filter(product_uuid=product_uuid, code=data['code'])
		serializer = ListProductSerializer(product)

		if buyer and product and serializer.is_valid():
			product.number_seen = product.number_seen + 1
			product.save()
			return Response("Product was seen")
		return Response("not valid authorization")


class BuyerPutInCartView(viewsets.ViewSet):
	@buyer_token_required
	def create(self, request, buyer_uuid, product_uuid):
		responses = {}
		data = request.data
		buyer = Buyer.objects.filter(buyer_uuid=buyer_uuid, is_login=True)
		product = Product.objects.filter(product_uuid=product_uuid)

		if not buyer.cart:
			new_cart = Cart(buyer=buyer)
			new_cart.save()

		if buyer and buyer.cart and product:
			product.cart = buyer.cart
			product.save()


#buyer add number of item inside cart, can buy more that 1
class BuyerAddProductView(viewsets.ViewSet):
	@buyer_token_required
	def create(self, request, buyer_uuid, product_uuid):
		responses = {}
		buyer = Buyer.objects.filter(buyer_uuid=buyer_uuid, is_login=True)
		product = Product.objects.filter(product_uuid=product_uuid)

		if buyer and product:
			product.number_bought = number_bought + 1
			product.save()
			responses['msg'] = "The bought product is being added"
			return Response(responses)
		return Response("there is no authorization, try again")

#buyer substract number of item inside cart, can buy more that 1
class BuyerSubstractProductView(viewsets.ViewSet):
	@buyer_token_required
	def create(self, request, buyer_uuid, product_uuid):
		responses = {}
		buyer = Buyer.objects.filter(buyer_uuid=buyer_uuid, is_login=True)
		product = Product.objects.filter(product_uuid=product_uuid)

		if buyer and product:
			product.number_bought = number_bought - 1
			product.save()
			responses['msg'] = "The bought product is being substracted"
			return Response(responses)
		return Response("there is no authorization, try again")

#buyer can cancel item inside cart, can buy more that 1
class BuyerCancelInCartView(viewsets.ViewSet):
	@buyer_token_required
	def destroy(self, request, buyer_uuid, product_uuid):
		responses = {}
		buyer = Buyer.objects.filter(buyer_uuid=buyer_uuid, is_login=True)
		product = Product.objects.filter(product_uuid=product_uuid)
		cancel_item = cart.objects.filter(product=product)

		if buyer and product:
			cancel_item.delete()
			responses['msg'] = "item canceled successfully"
			return Response(responses)
		return Response("there is no authorization")

#buyer buy products
class BuyerBuyProductView(viewsets.ViewSet):
	@buyer_token_required
	def get(self, request, buyer_uuid):
		responses = {}
		data = request.data #collection of product_uuid and code
		buyer = Buyer.objects.filter(buyer_uuid=buyer_uuid)
		product = Product.objects.filter(product_uuid=product_uuid)

# class BuyerCancelProductView(viewsets.ViewSet):
# 	def delete(self, request,)


# class Buyer:

# 	def register(self):
# 		pass

# 	def login(self):
# 		pass

# 	def updateProfile(self):
# 		pass

# 	def resetPassword(self):
# 		pass

# 	def chooseProduct(self):
# 		pass

# 	def searchProduct(self):
# 		pass

# 	def seeProduct(self):
# 		pass

# 	def PutProdInCart(self):
# 		pass

# 	def updateProdInCart(self):
# 		pass

# 	def buyProduct(self):
# 		pass

# 	def cancelBuyingProduct(self):
# 		pass

# 	def reviewProductBought(self):
# 		pass

# 	- can add amount of item

