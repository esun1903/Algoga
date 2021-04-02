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
    path('v1/logout/<str:email>', UserViewSet.as_view({"get": "logout"})),
    #세션확인
    path('v1/sessionCheck/<str:email>', UserViewSet.as_view({"get": "sessionCheck"})),
    #회원가입
    path("v1/signUp", UserViewSet.as_view({"post": "signUp"})),
    #회원수정
    path("v1/userInfoUpdate/<str:email>", UserViewSet.as_view({"put": "userInfoUpdate"})),
    #회원탈퇴
    path("v1/userdelete/<str:email>", UserViewSet.as_view({"delete": "Userdelete"})),
    #이메일전송
    path("v1/activate/<str:uidb6>", UserViewSet.as_view({"delete": "Userdelete"})),
    #codBoard 등록
    path("v1/codeBoardRegiste", codeBoardViewSet.as_view({"post": "codeBoardRegiste"})),
    #codBoard 수정
    path("v1/codeBoardUpdate/<int:codeBoard_seq>", codeBoardViewSet.as_view({"put": "codeBoardUpdate"})),
    #codBoard 삭제
    path("v1/codeBoardDelete/<int:codeBoard_seq>", codeBoardViewSet.as_view({"delete": "codeBoardDelete"})),
    #codBoard All
    path("v1/codeBoardAll", codeBoardViewSet.as_view({"get": "codeBoardAll"})),
    #codBoard page
    path("v1/codeBoardPage/<int:codeBoard_seq>", codeBoardViewSet.as_view({"get": "codeBoardPage"})),
    #commnet 등록
    path("v1/commentRegiste", commentViewSet.as_view({"post": "commentRegiste"})),
    #commnet 수정
    path("v1/commentUpdate/<int:comment_seq>", commentViewSet.as_view({"put": "commentUpdate"})),
    #commnet 삭제
    path("v1/commentDelete/<int:comment_seq>", commentViewSet.as_view({"delete": "commentDelete"})),
    #commentList
    path("v1/commentList/<int:codeBoard_seq>", commentViewSet.as_view({"get": "commentList"})),
    #사용자가 맞은 문제 불러오기
    path("v1/userProblem/<int:seq>", ProblemViewSet.as_view({"get" : "callProblem"}), name="callProblem"),
    #모든 문제 리턴 (pagenation)
    path("v1/allProblem", ProblemViewSet.as_view({"get" : "allProblem"}), name="allProblem"),
    #문제 이름 검색
    path("v1/searchNameProblem/<str:name>", ProblemViewSet.as_view({"get" : "searchNameProblem"}), name="searchNameProblem"),
    #문제 난이도로 검색
    path("v1/searchLevelProblem/<int:level>", ProblemViewSet.as_view({"get" : "searchLevelProblem"}), name="searchLevelProblem"),
    #모든 문제 리턴 (pagination)
    path("v1/allPaginationProblem", ProblemViewSet.as_view({"get" : "allPaginationProblem"}), name="allPagenationProblem"),
    #문제 세부 정보 
    path("v1/Problem/<int:seq>", ProblemViewSet.as_view({"get" : "Problem"}), name="Problem"),
    
]