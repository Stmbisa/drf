from rest_framework import serializers
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model= Product
        fields = ['title', 'content','price','sale_price', 'my_discount']

    def get_my_discount(self, obj):
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product): # this is same as as if not hasattr(obj, 'id'): 
            return None
        # obj here is the object you can query anything like obj.id or any field
        return obj.get_discount()
        # try:
        #     return obj.get_discount()
        # except:
        #     return None 
    