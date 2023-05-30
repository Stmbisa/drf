from rest_framework import serializers


class UserProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField( # HyperlinkedIdentityField only works on model serializer
        view_name='product-detail',
        lookup_field='pk',
        read_only=True

        )
    title = serializers.CharField(required=True)


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.IntegerField(read_only=True)
    # my_other_products = serializers.SerializerMethodField(read_only=True)

    # def get_my_other_products(self, obj):
    #     # print(obj)
    #     user = obj
    #     products_qs = user.product_set.all()[:5]
    #     return UserProductInlineSerializer(products_qs, many=True, context=self.context).data