from django.db import models
from django.db.models.deletion import SET_NULL
from api.category.models import Category


class Prodcut(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=250)
    price = models.IntegerField()
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True, blank=True)
    image = models.ImageField(upload_to='images/products/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name
