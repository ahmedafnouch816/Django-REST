
from django.http import JsonResponse
from .models import Product 
from django.forms.models import model_to_dict 

from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import ProductSerializers
from rest_framework import generics


class DetailApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


