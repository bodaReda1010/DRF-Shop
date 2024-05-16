from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [

    path('add_to_cart/<str:product_slug>/' , views.add_to_cart , name = 'add_to_cart'),
    path('decrease_quantity/<str:product_slug>/' , views.decrease_quantity , name = 'decrease_quantity'),
    path('delete_cart_item/<str:product_slug>/' , views.delete_cart_item , name = 'delete_cart_item'),
    path('get_user_cart_items/' , views.get_user_cart_items , name = 'get_user_cart_items'),

]