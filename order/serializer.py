from rest_framework import serializers
from . models import *


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('id' , 'user' , 'email' , 'first_name' , 'last_name' , 'phone' , 'address1' , 'address2' , 'city')

class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Product
        fields = ('id' , 'user' , 'order' , 'product' , 'quantity' , 'product_price')

class OrderCompleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_Complete
        fields = ('id' , 'user' , 'order' , 'products' , 'total_price' , 'created_at')