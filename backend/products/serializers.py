from rest_framework import serializers
from rest_framework.reverse import reverse
from api.serializers import UserPublicSerializer
from products.models import Product
from . import validators


class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField( # HyperlinkedIdentityField only works on model serializer
        view_name='product-detail',
        lookup_field='pk',
        read_only=True

        )
    title = serializers.CharField(required=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True) 
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField( # HyperlinkedIdentityField only works on model serializer
        view_name='product-detail',
        lookup_field='pk'
        )
    title = serializers.CharField(validators= [validators.validate_title_no_hello, validators.unique_product_title])
    class Meta:
        model= Product
        fields = [
            'owner', # to avoid users trying to save products as others you should remove this field
            'url',
            'edit_url', 
            'pk',
            'title',
            'content',
            'price',
            'sale_price', 
            'public'
            ]

    def get_my_user_data(self, obj):
        return {
            'username':obj.user.username 
        }

    
    def get_edit_url(self, obj):
        # return f"/api/products/{obj.pk}/"
        request = self.context.get('request') #self.request on views yet here its self.context.get('request')
        if request is None:
            return None 
        return reverse("product-edit",kwargs={"pk":obj.pk},  request=request)

    