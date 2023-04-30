from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    return JsonResponse({
       'message': 'Hello, This is django API response!!!.',
    })