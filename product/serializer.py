from rest_framework import serializers
from . models import Product , Review


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['name' , 'price' , 'stock' , 'created_at' , 'updated_at' , 'is_active']



class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['user' , 'product' , 'rating' , 'comment']