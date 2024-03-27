
from django.http import JsonResponse
from .models import Product 
from django.forms.models import model_to_dict 

def api_view(request):
    # request =! requests 
    # request c'ets instance de httprequest
    
    query = Product.objects.all().order_by('?').first()
    
    # creation dictionary 
    data = {}
    
    if query:
        data = model_to_dict(query)
        #serialization: Mettre  des données sur  forme de dict 
    return JsonResponse(data)
        
        
    
    
    
