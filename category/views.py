from rest_framework import viewsets , status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from . models import Category
from product.models import Product
from . serializer import CategorySerializer
from product.serializer import ProductSerializer




class Category_Viewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # http://127.0.0.1:8000/api/category/category_slug/filter_by_category/
    @action(detail=True , methods=['GET'])
    def filter_by_category(self , request , category_slug = None):
        category = Category.objects.get(slug=category_slug)
        products = Product.objects.filter(category = category , is_active=True)
        serializer = ProductSerializer(products , many = True)
        json = {
            'Message':f'The Products Of Category {category} is {len(products)}',
            'Data':serializer.data
        }
        return Response(json , status=status.HTTP_200_OK)

