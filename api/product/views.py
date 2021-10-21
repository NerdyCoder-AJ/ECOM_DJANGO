from rest_framework import viewsets
from .serilizers import ProductSerializer
from .models import Prodcut

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Prodcut.objects.filter(is_active=True).order_by('id')
    serializer_class = ProductSerializer
