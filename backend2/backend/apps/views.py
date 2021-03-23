from django.contrib.auth.models import User, Group
from rest_framework import permissions
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
        if musics.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        music_serializer = UserSerializer(data=request.data, partial=True)
        if not music_serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        music = music_serializer.save()

        return Response(UserSerializer(music).data, status=status.HTTP_201_CREATED)



      