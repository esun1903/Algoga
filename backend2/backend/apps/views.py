from django.contrib.auth.models import User, Group
from rest_framework import permissions
from rest_framework import response
from .serializers import UserSerializer
import json
from django.http import HttpResponse, JsonResponse
from .models import User
from rest_framework import status, viewsets, mixins 
from rest_framework.response import Response 
from django.views import View 
from django.http import Http404



class viewSet(viewsets.ModelViewSet):
 
    
    serializer_class = UserSerializer
 
     
    def add(self, request): 
        
        musics = User.objects.filter(**request.data)
        #이걸로 중복체크하고
        if musics.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        music_serializer = UserSerializer(data=request.data, partial=True)
        
        #여기서 유효성검사하면되네
        if not music_serializer.is_valid():

            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        music = music_serializer.save()

        return Response(UserSerializer(music).data, status=status.HTTP_201_CREATED)


class UserViewSet(viewsets.GenericViewSet, 
                mixins.ListModelMixin, 
                View): 

    serializer_class = UserSerializer
    def get_queryset(self):
        
        conditions = {
            
            'email': self.request.GET.get('email', None),
            'password': self.request.GET.get('password', None),
            'baek_id': self.request.GET.get('baek_id', None),
            'nickname': self.request.GET.get('nickname', None),

        }
        conditions = {key: val for key, val in conditions.items() if val is not None}
        
        users =  User.objects.filter(**conditions)
        if not users.exists():
            raise Http404()

        return users

    def add(self, request): 
       
        users =  User.objects.filter(**request.data)
      
        if users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        userSerializer = UserSerializer(data=request.data, partial=True)
        if not userSerializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        user = userSerializer.save()

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
   
    
  

    def regist(self, request): 
        
        users =  User.objects.filter(email =request.data["email"])
        print(request.data["email"])

        if users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        userSerializer = UserSerializer(data=request.data, partial=True)
        print(userSerializer)
        if not userSerializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        user = userSerializer.save()

        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)






