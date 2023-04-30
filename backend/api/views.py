from django.http import JsonResponse
import json

def api_home(request, *args, **kwargs):
    body = request.body
    data = {}
    try:
        data = json.loads(body)
    except:
        pass
    print(data)
    data['params']= dict(request.GET) # request.GET brings the params
    data ['headers']= dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)