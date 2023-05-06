from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import json
from rest_framework.response import Response
from products.models import Product

from rest_framework.decorators import api_view
from django.http import JsonResponse
from rest_framework import status

from products.models import Product
from products.serializers import ProductSerializer

@api_view(['POST'])
def api_home(request, *args, **kwargs):
    """
    DRF API View
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        # instance = serializer.save()
        print(serializer.data)
        return Response(serializer.data)
    else:
        errors = serializer.errors
        return Response({'errors': errors}, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET'])
# def api_home(request, *args, **kwargs):
#     instance = Product.objects.all().order_by("?").first()
#     data={}
#     if instance:
#         # data = model_to_dict(instance, fields=['id', 'title', 'price','sale_price'])
#         data = ProductSerializer(instance).data
#     return Response(data)

# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data={}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title', 'price'])
#     return JsonResponse(data)
    #     print(data)
    #     json_data_str = json.dumps(data)

    # return HttpResponse(data, headers= {"Content-Type": "application/json"})


# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by("?").first()
#     data={}
#     if model_data:
#         data['id'] = model_data.id
#         data['title'] = model_data.title
#         data['content'] = model_data.content
#         data['price'] = model_data.price

#     return JsonResponse(data)


# def api_home(request, *args, **kwargs):
#     body = request.body
#     data = {}
#     try:
#         data = json.loads(body)
#     except:
#         pass
#     print(data)
#     data['params']= dict(request.GET) # request.GET brings the params
#     data ['headers']= dict(request.headers)
#     data['content_type'] = request.content_type
#     return JsonResponse(data)