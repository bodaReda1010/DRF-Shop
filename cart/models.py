from django.db import models
import uuid
from django.contrib.auth.models import User
from product.models import Product



class Cart_Item(models.Model):
    id = models.UUIDField(primary_key = True , default = uuid.uuid4 , editable = False)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    quantity = models.IntegerField()
    size = models.CharField(max_length=50)
    color = models.CharField(max_length=50)


    class Meta:
        verbose_name = ("Cart_Item")
        verbose_name_plural = ("Cart_Items")

    def __str__(self):
        return f'{self.product} {self.user}'
    
    def sub_total(self):
        return self.product.price * self.quantity
    
    @property
    def total(self):
        total = 0
        items = Cart_Item.objects.filter(user = self.user)
        for item in items:
            total += item.sub_total()
        return total




