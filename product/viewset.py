from .models import Product
from .serializer import ProductSerializers
from rest_framework import viewsets,mixins

class ProductViewset(viewsets.ModelViewSet):
    """
    A viewset that provides default `create()`, `retrieve()`, `update()`,
    `partial_update()`, `destroy()` and `list()` actions.
    """
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
    
class ProductListRestrieveViewset(viewsets.GenericViewSet,mixins.ListModelMixin,mixins.RetrieveModelMixin
                        ):
        
    queryset = Product.objects.all()
    serializer_class = ProductSerializers