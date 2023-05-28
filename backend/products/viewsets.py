from rest_framework import mixins, viewsets

from .models import Product
from .serializers import ProductSerializer


class ProductViewSet(viewsets.ModelViewSet):
    """
    get -> list -> queryset
    get -> retrieve -> product instance detail view 
    post -> create -> new instance 
    put -> updated 
    patch -> partial update 
    delete -> destroy 
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    # mixins.CreateModelMixin, #you add onluy mixins that you would like to have in this type of vieset 
    viewsets.GenericViewSet):
    """
    get -> list -> queryset
    get -> retrieve -> product instance detail view 
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

product_list_view = ProductGenericViewSet.as_view({'get':'list'})
product_detail_view = ProductGenericViewSet.as_view({'get':'retrieve'})
#  those can be used in urls as  normal function based views and send them where you want them to be which isnt the case with viewsets
