from rest_framework import serializers

from product.models import Product
from rest_framework.reverse import reverse
from .validators import validators_unique_product_name

class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True )
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    name = serializers.CharField(validators=[validators_unique_product_name])

    
    class Meta:
        model = Product
        fields =  ('email','url','pk','name', 'prix' , 'content' ,'my_discount')
    
    
    def validate_name(self, value):
        request = self.context.get('request')
        if request is not None:
            user = request.user
            qs = Product.objects.filter(user=user, name__iexact=value)
        qs = Product.objects.filter(name__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"le produit {value} esiste deja dans db ")
        return value
            

    def create(self, validated_data): 
        print(validated_data)
        email = validated_data.pop('email')
        print(email)
        print(validated_data)
        #return Product.objects.create(**validated_data)
        obj = super().create(validated_data)
        return obj  
    
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        return super().update(instance, validated_data)
    
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        
        return obj.get_discount