from .models import MyUser
from buyer.models import Cart
from buyer.models import HistoryBuyer
from rest_framework import serializers

class UserLoginSerializer(serializers.ModelSerializer):
	class Meta:
		model = MyUser
		fields = ['email', 'password']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class HistoryBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryBuyer
        fields = '__all__'