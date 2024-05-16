from django.contrib import admin
from django.urls import path , include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/' , include('category.urls' , namespace = 'category')),
    path('api/' , include('product.urls' , namespace = 'product')),
    path('api/' , include('accounts.urls' , namespace = 'accounts')),
    path('api/' , include('cart.urls' , namespace = 'cart')),
    path('api/' , include('order.urls' , namespace = 'order')),
    path('api-token-auth/' , obtain_auth_token),
]

