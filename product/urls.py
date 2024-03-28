from django.urls import path
from .views import DetailApiView,CreateApiView,UpdateApiView

urlpatterns = [
    path("<int:pk>/", DetailApiView.as_view()),
    path("create/", CreateApiView.as_view()),
    path("<int:pk>/update", UpdateApiView.as_view()),

    

    
]
