from django.urls import path
from .views import DetailApiView

urlpatterns = [
    path("<int:pk>/", DetailApiView.as_view()),
    
]
