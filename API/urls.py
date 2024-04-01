from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api_prod/", include("api_prod.urls")),
    path("product/", include("product.urls")),
    
]
endpoint = 'http://127.0.0.1:8000/product/mixins'