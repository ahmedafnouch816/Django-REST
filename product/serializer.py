from rest_framework import serializers

from product.models import Product

class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True )
    class Meta:
        model = Product
        fields =  ('pk','name', 'prix' , 'content' ,'my_discount')
        #extra_kwargs = {'content': {'required': False, 'allow_blank': True}}
    
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        
        return obj.get_discount