from rest_framework import serializers

from product.models import Product
from rest_framework.reverse import reverse


class ProductSerializers(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True )
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk')
    
    
    class Meta:
        model = Product
        fields =  ('url','pk','name', 'prix' , 'content' ,'my_discount')
        #extra_kwargs = {'content': {'required': False, 'allow_blank': True}}

    
    #def get_url(self, obj):
    #    request = self.context.get('request')
    #    if request is None:
    #        return None 
    #    return reverse("product-detail" , kwargs={'pk':obj.pk}, request=request)
        
    
    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        
        return obj.get_discount