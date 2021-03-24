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
from rest_framework_jwt.authentication import JSONWebTokenAuthentication




class viewSet(viewsets.ModelViewSet):
 
    serializer_class = UserSerializer
 
    # UserUpdate 
    def Userupdate(self, request): 
        return Response("수정완료", status=status.HTTP_201_CREATED)


    # UserDelete
    def Userdelete(self,request,user_seq): 
        deleteuser = User.objects.get(user_seq = user_seq)
        deleteuser.delete()
        return  Response("완료", status=status.HTTP_200_CREATED)


@permission_classes([AllowAny])
class UserViewSet(viewsets.GenericViewSet, 
                mixins.ListModelMixin, 
                View): 

    serializer_class = UserSerializer				

    def login(self, request, email, password):
         
        loginUser =  User.objects.filter(email =email , password = password)
        
        if loginUser.exists():
            return Response(status=status.HTTP_200_OK)
        
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        

    def signUp(self, request): 
        users =  User.objects.filter(email =request.data["email"])
        if users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        userSerializer = UserSerializer(data=request.data, partial=True)
        if not userSerializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        user = userSerializer.save()

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)

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

        return Response(status=status.HTTP_201_CREATED)


