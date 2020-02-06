from models import Buyer, Cart, HistoryBuyer
from rest_framework import serializers


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyer
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class HistoryBuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryBuyer
        fields = '__all__'