from rest_framework import serializers
from . models import Cart_Item

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_Item
        fields = ('user' , 'product' , 'quantity' , 'size' , 'color')


        