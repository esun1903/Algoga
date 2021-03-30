from django.contrib.auth.models import *
from rest_framework import permissions
from .serializers import *
from .Userproblemserializers import *
from .Problemserializers import *
from .models import *
from rest_framework import status, viewsets, mixins 
from rest_framework.response import Response 
from django.views import View 
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from .pagination import PostPageNumberPagination
import pandas as pd
import requests
import os
import time

DATA_DIR = "./data"
rankpage = "https://www.acmicpc.net/ranklist/"
userpage = "https://www.acmicpc.net/user/"
    

@permission_classes([AllowAny])
class ProblemViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,View):
    
    serializer_class = UserProblemserializers
    # serializer_problem_class = 
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
        
        totalProblem = Problem.objects.all()
        mySet = set()
        for problem in totalProblem :
                mySet.add(problem.number)

        solveProblemList = list()

        for problem in user_problems[0]: 
                if int (problem) in mySet: 
                    solveProblemList.append(problem)
                    
        #  만약. user.seq
        # if usersProblems.exists(): 
        #     for Problem_one in usersProblems :
        #         Problem_one.delete() 

        users =  UserProblem.objects.filter(user_seq = user.seq)
        if  users.exists():
            for userProblem in users :
                userProblem.delete()
    
        # 디비에 있는 맞은 문제 번호 리스트 
        for num in solveProblemList:
                for problem in totalProblem :
                        if int (num) == int (problem.number): 
                                test3 = {'problem_seq' : int(problem.seq) , 'user_seq' : int(problem.seq),'correct': 0}
                                problem_list =  UserProblemserializers(data = test3 ) 
                                new_post = UserProblem.objects.create(problem_seq = Problem.objects.get(seq=problem.seq), user_seq = User.objects.get(seq=user.seq),correct = 0)
        
        mySet = set()
        for problem in totalProblem :
                mySet.add(problem.number)

        solveProblemList = list()

        for problem in user_problems[1]: 
                if int (problem) in mySet: 
                    solveProblemList.append(problem)
                    
        # 디비에 있는 맞은 문제 번호 리스트 
        for num in solveProblemList:
                for problem in totalProblem :
                        if int (num) == int (problem.number): 
                                test3 = {'problem_seq' : int(problem.seq) , 'user_seq' : int(problem.seq),'correct': 1}
                                problem_list =  UserProblemserializers(data = test3 ) 
                                new_post = UserProblem.objects.create(problem_seq = Problem.objects.get(seq=problem.seq), user_seq = User.objects.get(seq=user.seq),correct = 1)
                

        return Response("갱신되었습니다 !", status=status.HTTP_201_CREATED)
    



    @permission_classes([AllowAny])
    def allProblem(self, request): 
        #모든 문제 주기
        totalProblem = Problem.objects.all()
        serializer = Problemserializers(totalProblem, many=True)    
        return  Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes([AllowAny])
    def searchNameProblem(self, request,name): 
        #이름 검색해서 나온 값 주기
        totalProblem = Problem.objects.filter(name = name)
        serializer = Problemserializers(totalProblem, many=True)    
        return  Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes([AllowAny])
    def searchLevelProblem(self, request,level): 
        #난이도 검색해서 나온 값 주기
        totalProblem = Problem.objects.filter(level= level)
        serializer = Problemserializers(totalProblem, many=True)    
        return  Response(serializer.data, status=status.HTTP_200_OK)


    @permission_classes([AllowAny])
    def allPaginationProblem(self, request): 
        #모든 문제를 (problem_seq를 정렬해서 두기)
        totalProblem = UserProblem.objects.all().order_by('problem_seq')
        serializer_class = UserProblemserializers(totalProblem,many=True)
        pagination_class = PostPageNumberPagination
        return  super().get_queryset().filter()

    @permission_classes([AllowAny])
    def Problem(self, request ,seq ): 
        #문제의 seq를 받아 그 문제에 대한 정보를 모두 리턴 
        totalProblem = Problem.objects.get(seq=seq)
        serializer_class = Problemserializers(totalProblem)
        return  Response(serializer_class.data, status=status.HTTP_200_OK)


        # # 시도했지만 맞지 못한 문제 
        #     for problem in user_problems[1] :
        #     problem_list = UserProblem()
        #     problem_list.problem_seq = problem
        #     problem_list.correct = 1
        #     problem_list.user_seq = user.seq
        #     UserProblem.problem_seq 
        #     problem_list.save()
        #TINYINT : 0 ~ 255 까지의 범위를 갖고있다. 
        #correct : 맞은 문제 : 0
        #        : 시도했지만  맞지 못한 문제 : 1 
        #        : 맞았지만 만점을 받지 못한 문제 : 2
        # 맞은문제
        # problem2 = Problem.objects.filter(number = two_problem ) # 모든 문제에서 검색해서 

                #List<Problem> list  = new LinkedList<>(); 
        # Set<Integer> set = 갖고와
        # for (int i : user_problem[0]) :
            # if(set.__contains__(i)) {
                # list.add (new Proble(i, userId, 0));
            # }
        # for(Problem problem : list) {
            # db.save(problem);
        # }    

        # print("시도했지만  맞지 못한 문제") 
        # print(user_problems[-1])
        # print("*******************")
        

        # 얘에 대한 처리 나중에 꼭 해줘야함 
        # print("맞았지만 만점을 받지 못한 문제")  
        # print(user_problems[1])
        # print("*******************")

        
        # 만약, user_problem 테이블에 사용자 seq가 있는 컬럼들을 검색해서 
        # 다 삭제하고 
        # 넣어주기 
        # print("유저의 번호:")
        # print(user.seq)
        # usersProblems = UserProblem.objects.filter(user_seq = user.seq)
        
        # # # 다 삭제하기 ~
        
        # if usersProblems.exists(): 
        #     for Problem_one in usersProblems :
        #         Problem_one.delete() 

        # for one_problem in user_problems[0] :
        #     print("문제")
        #     print(one_problem)

        #     temp = Problem.objects.get(number = int(one_problem))
        #     print(temp)
        # if Problem.objects.get(number = int(one_problem))  == None :
        #     print("==============")
        #     continue
        # else :
        #     test = Problem.objects.get(number = int(one_problem))
            
        #     print(test)
        #     if test != None:
        #         test3 = {'problem_seq' : int(test.seq) , 'user_seq' : int(user.seq), 'correct': 0}
        #         problem_list =  UserProblemserializers(data = test3) 
        #         new_post = UserProblem.objects.create(problem_seq = Problem.objects.get(seq=test.seq), user_seq = User.objects.get(seq=user.seq), correct = 0)
            
        #     else :
        #         continue


        #     # print("문제의 seq")
        #     # # print(test.seq)
        #     # print("유저의 seq")
        #     # print(user.seq)
            
        #     # print("내가 이걸 체크해")
        #     # # print(test.seq)]