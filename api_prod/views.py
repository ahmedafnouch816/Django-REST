import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.


def api_view(request, *args, **kwargs):
    #request est une instance de htttprequests
    print(request.body)  #byte string
    data = json.loads(request.body) # converti les donnees en dict c'est le loads
    pre_data = json.dumps(data)
    print(data)
    data['headers'] = dict(request.headers)
    data['params'] = dict(request.GET)
    data['post'] = dict(request.POST)
    print(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)





