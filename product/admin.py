from django.contrib import admin
from . models import Product , Review
# Register your models here.


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name' , 'category' ,'price' , 'stock' , 'created_at' , 'updated_at' , 'is_active']
    


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product' , 'rating' , 'comment']