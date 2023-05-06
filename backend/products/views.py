from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perfom_create(self, serializer):
        # serializer.save(user=self.request.user,)
        print(serializer)
        serializer.save()

product_create_view = ProductCreateView.as_view()

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
