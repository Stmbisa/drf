from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import json

from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data={}
    if model_data:
        data = model_to_dict(model_data, fields=['id', 'title', 'price'])
    return JsonResponse(data)
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