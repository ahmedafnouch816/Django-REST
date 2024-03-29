from django.urls import path
from .views import DetailApiView,ListCreateApiView,UpdateApiView,DeleteProductView,ListProductView,ProductMixinsViews

urlpatterns = [
    #path("<int:pk>/", DetailApiView.as_view()),
    #path("create/", CreateApiView.as_view()),
    #path("<int:pk>/update", UpdateApiView.as_view()),
    #path("<int:pk>/delete", DeleteProductView.as_view()),
    #path("list/", ListProductView.as_view()),
#
    path("create-list/", ListCreateApiView.as_view()),
    path("<int:pk>/detail", ProductMixinsViews.as_view()),
    #path("<int:pk>/detail", ProductMixinsViews.as_view()),
    path("<int:pk>/update", ProductMixinsViews.as_view()),
    path("<int:pk>/delete", ProductMixinsViews.as_view()),
    path("list/", ProductMixinsViews.as_view()),

]
