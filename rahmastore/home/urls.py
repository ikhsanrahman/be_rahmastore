
from django.urls import path, include
from .views import HomeViewSet
from rest_framework import routers


# router = routers.DefaultRouter()
# router.register('', HomeViewSet, basename='home')
# router.register('cancel-product/<str:buyer_uuid>/<str:product_uuid>', BuyerCancelProductView, basename='buyer-cancel-buy-product')

urlpatterns = [
    path('homepage', HomeViewSet.as_view()),
    
]


