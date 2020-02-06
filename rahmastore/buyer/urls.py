
from django.urls import path, include
from .views import *
from rest_framework import routers


urlpatterns = [
    path('register', BuyerRegisterView.as_view({'post':'create'})),
	path('login', BuyerLoginView.as_view({'get':'list'})),
	path('reset-credential', BuyerResetPasswordView.as_view({'patch':'partial_retrieve'})),
	path('update-profile/<str:buyer_uuid>', BuyerUpdateProfileView.as_view({'put':'update'})),
	path('logout/<str:buyer_uuid>', BuyerLogoutView.as_view({'get':'list'})),
	path('see-product/<str:buyer_uuid>/<str:product_uuid>', BuyerSeeProductView.as_view({'get':'retrieve'})),
	path('buy-product/<str:buyer_uuid>', BuyerBuyProductView),
	path('put-product-in-cart/<str:buyer_uuid>/<str:product_uuid>', BuyerPutInCartView),
	path('cancel-product-in-cart/<str:buyer_uuid>/<str:product_uuid>', BuyerCancelInCartView),
	# router.register('cancel-product/<str:buyer_uuid>/<str:product_uuid>', BuyerCancelProductView, basename='buyer-cancel-buy-product')

]
