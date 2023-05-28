from rest_framework import generics, mixins #authentication,
# from api.authentication import TokenAuthentication

from .models import Product
from .serializers import ProductSerializer
# from api.permissions import IsStaffEditorPermission
from api.mixins import StaffEditorPermissionMixin 
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from django.http import Http404
from django.shortcuts import get_object_or_404

class ProductListCreateView(
    StaffEditorPermissionMixin, 
    generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = (
    #     authentication.SessionAuthentication,
    #     TokenAuthentication
    #                           ) set in deffault authentication_classes
    # permission_classes = [permissions.DjangoModelPermissions]
    # permission_classes = [permissions.IsAdminUser, IsStaffEditorPermission] # replaced by the custom mixin

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user,)
        print(serializer.validated_data)
        email = serializer.validated_data.pop('email')
        print(email)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content )

# class ProductCreateView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

#     def perfom_create(self, serializer):
#         # serializer.save(user=self.request.user,)
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content') or None
#         if content is None:
#             content=title
#         serializer.save(content=content )

product_list_create_view = ProductListCreateView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

class ProductUpdateAPIView(
    StaffEditorPermissionMixin,
    generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    # authentication_classes = (authentication.SessionAuthentication,)

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(
    StaffEditorPermissionMixin,
    generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    


    def perform_destroy(self, instance):
        # do something with the instance
        super().perform_destroy(instance)

product_delete_view = ProductDestroyAPIView .as_view()



# class ProductListAPIView(generics.ListAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # lookup_field = 'pk'

# product_list_view = ProductListAPIView.as_view()


class ProductMixinView(
    StaffEditorPermissionMixin,
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk' #default settings but can change



    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get('pk')
        # pk = kwargs
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs )
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def perfom_create(self, serializer):
        serializer.save(user=self.request.user,)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content=title
        serializer.save(content=content )

product_mixin_view = ProductMixinView.as_view()

@api_view(['POST', 'GET'])
def product_alt_view(request,pk=None, *args, **kwargs):
    method = request.method

    if method == 'GET':
    #  url_args
    # get request  -> detail view
        # queryset = Product.objects.filter(pk=pk)
        # if not queryset.exists:
        #     raise Http404
        if pk is not None:
            obj= get_object_or_404(Product, pk=pk)
            data = ProductSerializer(obj, many=False).data
            return Response(data)
        else:
    #  list

            queryset = Product.objects.all()
            data = ProductSerializer(queryset, many=True).data
            return Response(data)
    
    if method == 'POST':
        # create an item
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content=title
            serializer.save(content=content )
            return Response(serializer.data)
        else:
            errors = serializer.errors
            return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)