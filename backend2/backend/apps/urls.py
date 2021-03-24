from django.urls import path 
from django.conf import settings 
from .views import *
from . import views

urlpatterns = [ 
    #로그인
    path("v1/login/<str:email>/<str:password>", UserViewSet.as_view({"get": "login"})),

    #로그아웃
    path('v1/logout/', UserViewSet.as_view({"get": "logout"})),

    #세션확인
    path('v1/sessionCheck/', UserViewSet.as_view({"get": "sessionCheck"})),

    #회원가입
    path("v1/signUp", UserViewSet.as_view({"post": "signUp"})),

    #회원수정
    path("v1/userInfoUpdate/<str:email>", UserViewSet.as_view({"put": "userInfoUpdate"})),

    #회원탈퇴
    path("v1/userdelete/<str:email>", UserViewSet.as_view({"delete": "Userdelete"})),

    
    
]