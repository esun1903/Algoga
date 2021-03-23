from django.urls import path 
from django.conf import settings 
from .views import viewSet

urlpatterns = [ 


    #회원가입
    path("v1/user", viewSet.as_view({"get": "list", "post": "add"}), name="user"),
    path("v1/user/<int:user_int>", viewSet.as_view({"get": "list"}), name="user"),

    #회원수정
    path("v1/userupdate?", viewSet.as_view({"post" : "update"}), name="userSeq"),

    #회원탈퇴
    path("v1/userdelete/<int:user_seq>", viewSet.as_view({"get": "Userdelete"}), name="user_seq"),
    
]