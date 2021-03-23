from django.urls import path 
from django.conf import settings 
from .views import viewSet

urlpatterns = [ 
    path("v1/user", viewSet.as_view({"get": "list", "post": "add"}), name="user"),
    path("v1/user/<int:user_int>", viewSet.as_view({"get": "list"}), name="user"),
]