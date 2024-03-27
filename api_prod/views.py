import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.


def api_view(request, *args, **kwargs):
    #request est une instance de htttprequests
    print(request.body)  #byte string
    data = {
        'name': 'ahmed',
        'language': 'en'
    }
    return JsonResponse(data)





