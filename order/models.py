from django.db import models
import uuid
from django.contrib.auth.models import User
from cart.models import Cart_Item
from product.models import Product
# Create your models here.


class Order(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50)
    address2 = models.CharField(max_length=50 , null = True , blank = True)
    city = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Order")
        verbose_name_plural = ("Orders")

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    @property
    def full_address(self):
        return f'{self.address1} {self.address2}'

    def __str__(self):
        return f'{self.user.email} {self.full_name}'




class Order_Product(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField()
    product_price = models.FloatField()
    order_notes = models.CharField(max_length=350)
    ordered = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Order_Product")
        verbose_name_plural = ("Order_Products")

    @property
    def total(self):
        total = 0
        items = Order_Product.objects.filter(user = self.user)
        for item in items:
            total += item.sub_total
        return total
    
    @property
    def sub_total(self):
        return self.product.price * self.quantity

    def __str__(self):
        return f'{self.order.full_name} {self.product}'
    



class Order_Complete(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    order = models.ForeignKey(Order , on_delete=models.CASCADE)
    products = models.TextField()
    total_price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = ("Order_Complete")
        verbose_name_plural = ("Orders_Complete")

    @property
    def total(self):
        total = 0
        items = Cart_Item.objects.filter(user = self.user)
        for item in items:
            total += item.sub_total()
        return total

    def __str__(self):
        return f'{self.order.full_name}'

