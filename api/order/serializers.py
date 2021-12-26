from django.db.models import fields
from rest_framework import serializers
from .models import Order

class OrderSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('user', 'product_names', 'total_products')
        #TODO: add product and quantity