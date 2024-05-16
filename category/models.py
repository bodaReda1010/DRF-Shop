from django.db import models
from django.utils.text import slugify
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique = True , null = True , blank = True)
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)

    def save(self , *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category , self).save(*args, **kwargs)
        
    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name
