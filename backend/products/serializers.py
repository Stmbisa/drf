from rest_framework import serializers
from rest_framework.reverse import reverse
from products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True) # SerializerMethodField works anywhere 
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField( # HyperlinkedIdentityField only works on model serializer
        view_name='product-detail',
        lookup_field='pk'
        )
    email = serializers.EmailField(write_only=True) # write_only=True allows to add fields to not on the model
    class Meta:
        model= Product
        fields = [
            'url',
            'edit_url',
            'email',
            'pk',
            'title', 
            'content',
            'price',
            'sale_price', 
            'my_discount']
        
    def create(self, validated_data):
        # return Product.objects.create(**validated_data)
        # email = validated_data.pop('email') # these methods can be shifted to the view itself if def create
        obj= super().create(validated_data)
        # print(email,obj)
        return obj
    
     
    def update(self, instance, validated_data):
        # email = validated_data.pop('email')
        # instance.title = validated_data.get('title')
        # return super().update(instance, validated_data)
        return instance 
    
    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request') #self.request
        if request is None:
            return None 
        return reverse("product-edit",kwargs={"pk":obj.pk},  request=request)

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
    