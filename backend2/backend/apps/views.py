from django.contrib.auth.models import User, Group
from rest_framework import permissions
from .serializers import *
from .models import User
from rest_framework import status, viewsets, mixins 
from rest_framework.response import Response 
from django.views import View 
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny,IsAuthenticated




@permission_classes([AllowAny])
class UserViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,View): 

    serializer_class = UserSerializer				

    def login(self, request, email, password):
         
        loginUser =  User.objects.filter(email =email , password = password)
        
        if loginUser.exists():
            request.session['email'] = email
            return Response("로그인성공",status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def sessionCheck(self, request):
        
        userSession = request.session.get('email')
        
        if userSession :
            user = User.objects.get(email = userSession)
            return Response(user.email)
       
        return Response("로그인 필요",status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def logout(self, request):
        request.session.clear();
        return Response("로그 아웃",status=status.HTTP_200_OK)
        
    def signUp(self, request): 
        users =  User.objects.filter(email =request.data["email"])
        if users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        userSerializer = UserSerializer(data=request.data, partial=True)
        if not userSerializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        userSerializer.save()
        #UserSerializer(user).data list 할때 필요
        return Response("회원가입완료", status=status.HTTP_201_CREATED)

    def userInfoUpdate(self,request, email):

        users =  User.objects.filter(email =email)
        if not users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        userInfoModify = User.objects.get(email=email)
        userInfoModify.password =request.data["password"]
        userInfoModify.baek_id  =request.data["baek_id"]
        userInfoModify.nickname =request.data["nickname"]
        userInfoModify.profile_image=request.data["profile_image"]
        userInfoModify.save()

        return Response("수정 성공",status=status.HTTP_201_CREATED)

    def Userdelete(self,request,email): 
        
        users = User.objects.filter(email = email)
        if not users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
      
        userdelete = User.objects.get(email = email)
        userdelete.delete()
        
        return  Response("삭제성공", status=status.HTTP_201_CREATED)

@permission_classes([AllowAny])
class codeBoardViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,View):
    
    serializer_class = CodeBoardSerializer
   
    def solutionCodeList(self, request, email, password):
        return
    def solutionCodePage(self, request, email, password):
        return
    def codeBoardRegiste(self, request):
        codeBoardSerializer = CodeBoardSerializer(data=request.data, partial=True)
        if not codeBoardSerializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        codeBoardSerializer.save()

        return Response("코드보드 등록완료", status=status.HTTP_201_CREATED)
    
    def codeBoardUpdate(self, request, code_seq):
        
        codeBoard =  CodeBoard.objects.filter(seq =code_seq)
        if not codeBoard.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        codeBoard.update(code =request.data["code"],explanation  =request.data["explanation"],free_write =request.data["free_write"],problem_seq=request.data["problem_seq"],language_seq=request.data["language_seq"])
        return Response("수정 성공",status=status.HTTP_201_CREATED)


    def codeBoardDelete(self, request, code_seq):

        codeBoard =  CodeBoard.objects.filter(seq =code_seq)
        if not codeBoard.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        codeBoard.delete()
        
        return  Response("삭제성공", status=status.HTTP_201_CREATED)

    