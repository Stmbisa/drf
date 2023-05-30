from rest_framework import serializers
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer
from products.models import Product
# from .validators import validate_title
from . import validators


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField( # HyperlinkedIdentityField only works on model serializer
        view_name='product-detail',
        lookup_field='pk',
        read_only=True

        )
    title = serializers.CharField(required=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True) #you need to declare things that you would like to have as read only 
    related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
    my_user_data = serializers.SerializerMethodField(read_only=True)
    my_discount = serializers.SerializerMethodField(read_only=True) # SerializerMethodField works anywhere 
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField( # HyperlinkedIdentityField only works on model serializer
        view_name='product-detail',
        lookup_field='pk'
        )
    # email = serializers.EmailField(write_only=True) # write_only=True allows to add fields to not on the model
    title = serializers.CharField(validators= [validators.validate_title_no_hello, validators.unique_product_title])
    # name = serializers.CharField(source ='title', read_only=True )
    # email = serializers.EmailField(source ='user.email', read_only=True ) # if we had user attached to the product
    class Meta:
        model= Product
        fields = [
            'owner', # to avoid users trying to save products as others you should remove this field
            'url',
            'edit_url', 
            # 'email', 
            'pk',
            'title',
            # 'name', 
            'content',
            'price',
            'sale_price', 
            'my_discount',
            'my_user_data',
            'related_products'
            ]

    # def validate_title(self, value): # replaced by custom validators in validators.py 
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     # This is would be the best concept to customise the validation to a specific user
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product  name")
    #     return value 
    def get_my_user_data(self, obj):
        return {
            'username':obj.user.username 
        }
        
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
        request = self.context.get('request') #self.request on views yet here its self.context.get('request')
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
    