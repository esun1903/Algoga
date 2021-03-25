from django.contrib.auth.models import User, Group
from rest_framework import permissions
from .serializers import *
from .problemserializers import *
from .models import User
from rest_framework import status, viewsets, mixins 
from rest_framework.response import Response 
from django.views import View 
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from bs4 import BeautifulSoup
import pandas as pd
import requests
import os
import time

DATA_DIR = "./data"

rankpage = "https://www.acmicpc.net/ranklist/"
userpage = "https://www.acmicpc.net/user/"
    

@permission_classes([AllowAny])
class ProblemViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,View):
    
    serializer_class = UserSerializer				
    # 내가 푼 문제와 내 레벨 가져오기, [0] : 맞은 문제 / [-1] : 시도했지만 틀린 문제

   # 사용자가 '문제 불러오기'를 클릭하면 
   # 1. db에서 user테이블에서 그 사용자의 백준아이디와 seq를 가져온다. 
    def callProblem(self, request , seq): 
        
        print("******************")
        print("입력받은 email : ")
        print(seq)
        user = User.objects.get(seq = seq)
        print("입력받은 email에 대한 백준 id는 ?"+ user.baek_id)
        print("입력받은 email에 대한 백준 seq는 ?")
        print(user.seq)

        userURL = userpage + user.baek_id
        webpage = requests.get(userURL)
        bs = BeautifulSoup(webpage.content, "html.parser")

        level = bs.find('div', {'class': 'page-header'}).h1.img
        if level is None :
            level = 999
        else :
            level = level['src'].split('/')[-1].split('.')[0]

        divs = bs.findAll('div', {'class': 'panel-body'})

        user_problems = []
        for div in divs :
            problems = list(map(lambda x : x.text, div.find_all('a')))
            user_problems.append(problems)

      
        print("맞은문제")  
        print(user_problems[0])
        print("*******************")



        print("시도했지만  맞지 못한 문제") 
        print(user_problems[-1])
        print("*******************")
    
    
        # 얘에 대한 처리 나중에 꼭 해줘야함 
        # print("맞았지만 만점을 받지 못한 문제")  
        # print(user_problems[1])
        # print("*******************")
        
   
        
       
        # 만약, user_problem 테이블에 사용자 seq가 있는 컬럼들을 검색해서 
        # 다 삭제하고 
        # 넣어주기 
        print("여기야~~~~~~~~~~~~~")
        print(user.seq)
        
        usersProblems = User_Problem.objects.filter(user_seq = user.seq)
        # 다 삭제하기 ~
        if usersProblems.exists():
            for Problem in usersProblems :
                Problem.delete()
        

        #TINYINT : 0 ~ 255 까지의 범위를 갖고있다. 
        #correct : 맞은 문제 : 0
        #        : 시도했지만  맞지 못한 문제 : 1 
        #        : 맞았지만 만점을 받지 못한 문제 : 2
        # 맞은문제
        for problem in user_problems[0] :
            problem_list = User_Problem()
            problem_list.correct = 0
            problem_list.problem_seq = problem
            problem_list.user_seq = seq
            print(problem_list)
            problem_list.save()

        # # 시도했지만 맞지 못한 문제 
        for problem in user_problems[1] :
            problem_list = User_Problem()
            problem_list.correct = 1
            problem_list.problem_seq = problem
            problem_list.user_seq = seq
            print(problem_list)
            problem_list.save()

    




        
        return Response("성공 ~ ", status=status.HTTP_201_CREATED)
    
