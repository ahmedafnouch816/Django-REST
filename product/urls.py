from django.urls import path
from .views import DetailApiView,CreateApiView,UpdateApiView,DeleteProductView

urlpatterns = [
    path("<int:pk>/", DetailApiView.as_view()),
    path("create/", CreateApiView.as_view()),
    path("<int:pk>/update", UpdateApiView.as_view()),
    path("<int:pk>/delete", DeleteProductView.as_view()),


    
]
