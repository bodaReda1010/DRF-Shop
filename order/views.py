from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from . models import Order , Order_Complete  , Order_Product
from cart.models import Cart_Item
from product.models import Product
from . serializer import OrderSerializer , OrderProductSerializer , OrderCompleteSerializer



@api_view(['POST' , 'GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def make_order(request , address2 = None):
    user = request.user
    email = user.email
    if request.method == 'GET':
        orders = Order.objects.all()
        serializer = OrderSerializer(orders)
        response = {
            'Message':f'The Orders Of User {user}:',
            'data':serializer.data
        }
        return Response(response , status = status.HTTP_200_OK)
    elif request.method == 'POST':
        first_name = request.data['first_name']
        last_name = request.data['last_name']
        phone = request.data['phone']
        address1 = request.data['address1']
        address2 = request.data.get('address2' , '')
        city = request.data['city']
        try:
            order = Order.objects.get(user = user)
            order.first_name = first_name
            order.last_name = last_name
            order.phone = phone
            order.address1 = address1
            order.email = email
            if address2:
                order.address2 = address2
            order.city = city
            order.save()
            serializer = OrderSerializer(order)
            response = {
            'Message':'Order Has Been Updated',
            'data':serializer.data
            }
            return Response(response , status = status.HTTP_200_OK)
        except:
            order = Order.objects.create(
                user        = user,
                email       = email,
                first_name  = first_name,
                last_name   = last_name,
                phone       = phone,
                address1    = address1,
                address2    = address2,
                city        = city,
            )
            serializer = OrderSerializer(order)
            response = {
            'Message':'Order Has Been Created',
            'data':serializer.data
            }
            return Response(response , status = status.HTTP_201_CREATED)
        




@api_view(['POST' , 'GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def place_order(request):
    user = request.user
    if request.method == 'GET':
        orders = Order_Product.objects.all()
        serializer = OrderSerializer(orders)
        response = {
            'Message':f'The Orders Had Been Ordered From User {user}',
            'data':serializer.data
        }
        return Response(response , status = status.HTTP_200_OK)
    elif request.method == 'POST':
        order = Order.objects.get(user = user)
        items = Cart_Item.objects.filter(user=user)
        for item in items:
            order_product = Order_Product()
            order_product.order_id = order.id
            order_product.user = user
            order_product.product = item.product
            order_product.quantity = item.quantity
            order_product.product_price = item.product.price
            order_product.order_notes = f'The Size Is {item.size} And Color IS {item.color}'
            order_product.ordered = True
            order_product.save()
            product = Product.objects.get(id=item.product_id)
            product.stock -= item.quantity
            if product.stock < 0:
                return Response({'Message':'Please Order Fewer Quantity Of This Product'})
            product.save()

        Cart_Item.objects.filter(user=user).delete()
        data = {
            'Message':'Place Order Success'
        }
        return Response(data , status = status.HTTP_202_ACCEPTED)



@api_view(['POST' , 'GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def order_complete(request):
    user = request.user
    if request.method == 'GET':
        completed_orders = Order_Complete.objects.all()
        serializer = OrderCompleteSerializer(completed_orders)
        response = {
            'Message':f'The Orders Have Been Completed Done With User {user}',
            'Data':serializer.data
        }
        return Response(response , status = status.HTTP_200_OK)
    elif request.method == 'POST':
        products = []
        order = Order.objects.get(user=user)
        order_products = Order_Product.objects.filter(user=user)

        for product in order_products:
            product_name = product.product.name
            quantity = product.quantity
            price = product.product_price
            subtotal = product.sub_total
            products.append({
                'product':product_name,
                'quantity':quantity,
                'price':price,
                'subtotal':subtotal,
            })
        order_product = Order_Product.objects.get(user=user , product__name = products[0]['product'])
        orders = Order_Complete.objects.create(
            user         =          user,
            order        =          order,
            products     =          products,
            total_price  =          order_product.total
        )
        serializer = OrderCompleteSerializer(orders)
        data = {
            'Message':'Order Completed Successfully',
            'Data':serializer.data
        }
        return Response(data , status = status.HTTP_200_OK)