from django.urls import path 
from django.conf import settings 
from .views import *

urlpatterns = [ 
 
    path("v1/user", UserViewSet.as_view({"get": "list", "post": "add"}), name="musics"),
    path("v1/user/<str:email>", UserViewSet.as_view({"get": "list"}), name="email"),


    path("v1/test", UserViewSet.as_view({"post": "regist"})),
   

]