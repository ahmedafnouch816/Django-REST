    
from rest_framework import serializers
from product.models import Product
from rest_framework.validators import UniqueValidator


#ef validate_product_name(value):
#   qs = Product.objects.filter(name__iexact=value)
#   if qs.exists():
#       raise serializers.ValidationError(f"le produit {value} esiste deja dans db ")
#   return value
#      
       
       
validators_unique_product_name = UniqueValidator(queryset=Product.objects.all())
 