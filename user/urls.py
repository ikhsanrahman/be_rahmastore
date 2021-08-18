
from django.urls import path, include
from .views import *
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('home', HomeUserView.as_view({'get': 'list'})),
    path('register', UserRegisterView.as_view({'post': 'create'})),
    path('login', UserLoginView.as_view({'post': 'create'})),
    path('logout/<str:user_uuid>', UserLogoutView.as_view({'get': 'list'})),
    path('add-product/<str:user_uuid>', AddProductView.as_view({'post': 'create'})),
    path('update-product/<str:user_uuid>/<str:product_uuid>', UpdateProductView.as_view({'put': 'update'})),
    path('activate-product/<str:user_uuid>/<str:product_uuid>', ActivateProductView.as_view({'get': 'list'})),
    path('unactivate-product/<str:user_uuid>/<str:product_uuid>', UnactivateProductView.as_view({'get': 'list'})),
    # path('home', HomeUserView.as_view({'get': 'list'})),
    # path('home', HomeUserView.as_view({'get': 'list'})),


    
]
