from django.urls import path 
from django.conf import settings 
from .views import *
from .problem_views import *
from . import views
from . import problem_views

urlpatterns = [ 
    #로그인
    path("v1/login/<str:email>/<str:password>", UserViewSet.as_view({"get": "login"})),
    #로그아웃
    path('v1/logout', UserViewSet.as_view({"get": "logout"})),
    #세션확인
    path('v1/sessionCheck', UserViewSet.as_view({"get": "sessionCheck"})),
    #회원가입
    path("v1/signUp", UserViewSet.as_view({"post": "signUp"})),
    #회원수정
    path("v1/userInfoUpdate/<str:email>", UserViewSet.as_view({"put": "userInfoUpdate"})),
    #회원탈퇴
    path("v1/userdelete/<str:email>", UserViewSet.as_view({"delete": "Userdelete"})),
    #codBoard 등록
    path("v1/codeBoardRegiste", codeBoardViewSet.as_view({"post": "codeBoardRegiste"})),
    #codBoard 수정
    path("v1/codeBoardUpdate/<int:code_seq>", codeBoardViewSet.as_view({"put": "codeBoardUpdate"})),
    #codBoard 삭제
    path("v1/codeBoardDelete/<int:code_seq>", codeBoardViewSet.as_view({"delete": "codeBoardDelete"})),
    #codBoard All
    path("v1/codeBoardAll", codeBoardViewSet.as_view({"get": "codeBoardAll"})),
    #codBoard page
    path("v1/codeBoardPage/<int:code_seq>", codeBoardViewSet.as_view({"get": "codeBoardPage"})),
    #commnet 등록
    path("v1/commentRegiste", commentViewSet.as_view({"post": "commentRegiste"})),
    
    #문제추천해주기 
    #path("v1/problem", viewSet.as_view({"put" : "update"}), name="userSeq"),
    
]