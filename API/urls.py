from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api_prod/", include("api_prod.urls")),
    path("product/", include("product.urls")),

]

