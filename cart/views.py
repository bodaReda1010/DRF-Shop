from rest_framework.decorators import api_view , permission_classes , authentication_classes
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from . models import Cart_Item
from . serializer import CartItemSerializer
from product.models import Product


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def add_to_cart(request , product_slug = None):
    product = Product.objects.get(slug = product_slug)
    quantity = int(request.data['quantity'])
    color = request.data['color']
    size = request.data['size']
    user = request.user

    try:
        cart_item = Cart_Item.objects.get(product=product , color=color , size=size , user=user)
        cart_item.quantity += quantity
        cart_item.save()
        serializer = CartItemSerializer(cart_item)
        json = {
            'Message':'Cart Item Has Updated Successfully',
            'data':serializer.data
        }
        return Response(json , status=status.HTTP_200_OK)
    except:
        cart_item = Cart_Item.objects.create(
            product  =   product,
            quantity =   quantity,
            color    =   color,
            size     =   size,
            user     =   user
        )
        serializer = CartItemSerializer(cart_item)
        json = {
            'Message':'Cart Item Has Created Successfully',
            'data':serializer.data
        }
        return Response(json , status=status.HTTP_201_CREATED)



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def decrease_quantity(request , product_slug = None):
    product = Product.objects.get(slug=product_slug)
    quantity = int(request.data['quantity'])
    color = request.data['color']
    size = request.data['size']
    user = request.user

    try:
        cart_item = Cart_Item.objects.get(product=product , color=color , size=size , user=user)
        cart_item.quantity -= quantity
        if cart_item.quantity >= 1:
            cart_item.save()
            serializer = CartItemSerializer(cart_item)
            json = {
                    'Message':'Cart Item Has Updated Successfully',
                    'data':serializer.data
            }
            return Response(json , status=status.HTTP_200_OK)
        elif cart_item.quantity == 0:
            cart_item.delete()
            return Response({'Message':f'This Cart Item Has Been Deleted Because The Quantity Of Product {product} Is Equal TO Zero.'})
        return Response({'ERROR!!!':f'The Quantity Of Product {product} Must Be More Than One'} , status = status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'ERROR!!!':"Data Doesn't Exist"} , status=status.HTTP_400_BAD_REQUEST)
    



@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def delete_cart_item(request , product_slug = None):
    product = Product.objects.get(slug=product_slug)
    quantity = int(request.data['quantity'])
    color = request.data['color']
    size = request.data['size']
    user = request.user

    try:
        cart_item = Cart_Item.objects.get(quantity=quantity , color=color , size=size , user=user , product=product)
        cart_item.delete()
        return Response({'Message': 'Cart Item Has Been Deleted'} , status = status.HTTP_204_NO_CONTENT)
    except:
        return Response({'ERROR!!!':"Data Doesn't Exist"} , status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_user_cart_items(request):
    user = request.user
    cart_items = Cart_Item.objects.filter(user=user)
    serializer = CartItemSerializer(cart_items , many = True)
    response = {
        'Message':f'Cart Items Of {user}',
        'data':serializer.data
    }
    return Response(response , status = status.HTTP_200_OK)


