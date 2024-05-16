from django.contrib import admin
from . models import Order , Order_Complete , Order_Product
# Register your models here.



@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['user' , 'email' , 'first_name' , 'last_name' , 'phone' , 'city']


@admin.register(Order_Product)
class Order_ProductAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product' , 'order' , 'quantity' , 'product_price' , 'created_at' , 'updated_at']


@admin.register(Order_Complete)
class Order_CompleteAdmin(admin.ModelAdmin):
    list_display = ['user' , 'order' , 'products' , 'total_price' , 'created_at' , 'updated_at']
    

