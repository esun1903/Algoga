from django.urls import path 
from django.conf import settings 
from .views import *
from . import views

urlpatterns = [ 
    #로그인
    path("v1/login/<str:email>/<str:password>", UserViewSet.as_view({"get": "login"})),

    #회원가입
    path("v1/signUp", UserViewSet.as_view({"post": "signUp"})),

    #회원수정
    path("v1/userInfoUpdate/<str:email>", UserViewSet.as_view({"put": "userInfoUpdate"})),

    #회원탈퇴
    path("v1/userdelete/<int:user_seq>", viewSet.as_view({"get": "Userdelete"}), name="user_seq"),

    #로그아웃
   # path('logout/', LogoutView.as_view(), name='auth_logout'),

    #JWT인증
    #path('posts/', views.posts, name='posts'),
    
]