from django.db import models
from rest_framework import fields, serializers
from .models import Prodcut

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    image = serializers.ImageField(max_length=None, allow_empty_file=False, allow_null=True, required=False)
    
    class Meta:
        model = Prodcut
        fields = ('id', 'name', 'description', 'price', 'stock', 'image', 'category')
