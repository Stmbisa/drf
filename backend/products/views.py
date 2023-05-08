from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from django.http import Http404
from django.shortcuts import get_object_or_404

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perfom_create(self, serializer):
        # serializer.save(user=self.request.user,)
        print(serializer.validated_data)
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

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

product_update_view = ProductUpdateAPIView.as_view()


class ProductDestroyAPIView(generics.DestroyAPIView):
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