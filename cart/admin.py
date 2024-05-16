from django.contrib import admin
from . models import Cart_Item



@admin.register(Cart_Item)
class Cart_ItemAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product' , 'quantity' , 'size' , 'color']
    

