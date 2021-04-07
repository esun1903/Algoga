from django.contrib.auth.models import *
from rest_framework import permissions
from .serializers import *
from .models import *
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from django.views import View
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from .get_data import *
#from .pagination import PostPageNumberPagination
from collections import Counter
import requests
import os
from django.shortcuts import get_object_or_404

USER_PAGE = "https://www.acmicpc.net/user/"
ACCEPT_ALGORITHM_SEQ_LIST = list(range(1, 56)) + [62, 66, 68, 75]

@permission_classes([AllowAny])
class ProblemViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,View):
    
    serializer_class = UserProblemSerializer

    # 백준아이디 존재 확인
    def checkBaekjoon(self, request, baek_id):
        userURL = USER_PAGE + baek_id
        webpage = requests.get(userURL)
        bs = BeautifulSoup(webpage.content, "html.parser")

        level_img = bs.find('div', {'class': 'page-header'})

        if level_img is None:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(status=status.HTTP_200_OK)

    # 사용자가 푼 문제 갱신
    def callProblem(self, request, seq):
        user = get_object_or_404(User, seq = seq)

        userURL = USER_PAGE + user.baek_id
        webpage = requests.get(userURL)
        bs = BeautifulSoup(webpage.content, "html.parser")

        level_img = bs.find('div', {'class': 'page-header'})

        # 백준아이디가 잘못된 경우
        if level_img is None:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
            
        level = level_img.h1.img

        if level is None :
            level = 999
        else :
            level = int(level['src'].split('/')[-1].split('.')[0])

        divs = bs.findAll('div', {'class': 'panel-body'})

        # 1) 맞은 문제, 틀린 문제 가져오기, [0] : 맞은 문제 / [-1] : 시도했지만 틀린 문제
        user_problems = []
        for div in divs :
            problems = list(map(lambda x: int(x.text), div.find_all('a')))
            user_problems.append(problems)
        
        # 2) 디비에 있는 문제 중 맞은 문제, 틀린 문제만 가져오기
        totalProblem = Problem.objects.all()

        totalProblem_number = list(map(lambda x: x.number, totalProblem))
        totalProblem_seq = list(map(lambda x: x.seq, totalProblem))

        problem2seq = dict(zip(totalProblem_number, totalProblem_seq))

        correct_problems = list(set(totalProblem_number) & set(user_problems[0]))
        incorrect_problems = list(set(totalProblem_number) & set(user_problems[-1]))
            
        # 3) 기존 DB에 있는 사용자가 푼 문제들 삭제
        UserProblem.objects.filter(user_seq=user.seq).all().delete()
        
        # 4) DB에 푼 문제들 넣기, 맞으면 0, 틀리면 1
        for number in correct_problems:
            problem_seq = problem2seq[number]
            UserProblem.objects.create(problem_seq = totalProblem.get(seq = problem_seq), user_seq = user, correct = 0)
        
        for number in incorrect_problems:
            problem_seq = problem2seq[number]
            UserProblem.objects.create(problem_seq = totalProblem.get(seq = problem_seq), user_seq = user, correct = 1)

        # 5) 사용자 레벨 계산
        problem_exp = make_problem_exp_dict()
        level_exp = make_level_exp_dict()

        exp = sum(list(map(lambda x : problem_exp[x], correct_problems)))

        # 경험치에 맞는 레벨 계산
        calc_level = 0
        for cur_level in range(30, 0, -1) :
            if level_exp[cur_level - 1] <= exp :
                calc_level = cur_level
                break

        # 계산한 레벨과 solved 레벨의 차이가 크면 계산한 레벨로 업데이트
        diff = calc_level - level
        if diff < -5 or diff > 5 :
            level = calc_level

        user.level = level
        user.save()

        return Response(status=status.HTTP_201_CREATED)
        
    # 맞은 문제 중 가장 적은 알고리즘 문제들 추천
    def recommendProblemByCorrect(self, request, seq):
        
        # 유저seq가 없는 경우 404에러
        user = get_object_or_404(User, seq=seq)
        level = user.level

        myCorrectProblemSeq = UserProblem.objects.filter(user_seq=user.seq).filter(correct=0).values_list('problem_seq', flat=True)
        myInCorrectProblemSeq = UserProblem.objects.filter(user_seq=user.seq).filter(correct=1).values_list('problem_seq', flat=True)

        correctAlgoId = TypeOfProblem.objects.filter(problem_seq__in=myCorrectProblemSeq).values_list('type_seq', flat=True)
        
        # 맞은 문제가 없는 경우 406에러 -> 문제 갱신을 하거나 문제를 풀어라
        if len(correctAlgoId) == 0:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        # 알고리즘 분류별 개수
        correct_algo_dict = Counter(correctAlgoId)

        # 맞은 문제기반으로 추천해줄 알고리즘
        recommend_algo_seq_list = list(map(lambda x: x[0], correct_algo_dict.most_common()[-20:]))
        recommend_algo_seq_list = list(set(recommend_algo_seq_list) & set(ACCEPT_ALGORITHM_SEQ_LIST))

        # 해당 알고리즘 유형의 문제seq 추출
        recommend_problem = TypeOfProblem.objects.filter(type_seq__in = recommend_algo_seq_list).values_list('problem_seq', flat=True).distinct()

        # 추천할 문제 중 나의 레벨과 유사한 문제면서 내가 풀어보지 못한 문제를 제출수와 난이도 내림차순으로 정렬해서 20개만 보여주자
        recommend_problem = Problem.objects.filter(seq__in=recommend_problem).filter(level__range=(level - 5, level + 5)).exclude(seq__in = myCorrectProblemSeq).exclude(seq__in = myInCorrectProblemSeq).order_by('-submission_cnt', '-level')[:20]
        
        serializer = ProblemSerializer(recommend_problem, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 틀린 문제 중 가장 많은 알고리즘 문제들 추천
    def recommendProblemByInCorrect(self, request, seq):
        # 유저seq가 없는 경우 404에러
        user = get_object_or_404(User, seq=seq)
        level = user.level

        myCorrectProblemSeq = UserProblem.objects.filter(user_seq=user.seq).filter(correct=0).values_list('problem_seq', flat=True)
        myInCorrectProblemSeq = UserProblem.objects.filter(user_seq=user.seq).filter(correct=1).values_list('problem_seq', flat=True)

        InCorrectAlgoId = TypeOfProblem.objects.filter(problem_seq__in=myInCorrectProblemSeq).values_list('type_seq', flat=True)
        
        # 틀린 문제가 없는 경우 406에러 -> 틀린문제 기반으로 추천이 불가능하다
        if len(InCorrectAlgoId) == 0:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        # 알고리즘 분류별 개수
        incorrect_algo_dict = Counter(InCorrectAlgoId)

        # 틀린 문제기반으로 추천해줄 알고리즘
        recommend_algo_seq_list = list(map(lambda x: x[0], incorrect_algo_dict.most_common()[:10]))
        recommend_algo_seq_list = list(set(recommend_algo_seq_list) & set(ACCEPT_ALGORITHM_SEQ_LIST))

        # 해당 알고리즘 유형의 문제seq 추출
        recommend_problem = TypeOfProblem.objects.filter(type_seq__in = recommend_algo_seq_list).values_list('problem_seq', flat=True).distinct()

        # 추천할 문제 중 나의 레벨과 유사한 문제면서 내가 풀어보지 못한 문제를 제출수와 난이도 내림차순으로 정렬해서 20개만 보여주자
        recommend_problem = Problem.objects.filter(seq__in=recommend_problem).filter(level__range=(level - 5, level + 5)).exclude(seq__in = myCorrectProblemSeq).exclude(seq__in = myInCorrectProblemSeq).order_by('-submission_cnt', '-level')[:20]
        
        serializer = ProblemSerializer(recommend_problem, many=True)
        
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes([AllowAny])
    def allProblem(self, request):
        # 모든 문제 주기
        # 모든 문제를 줄 때
        totalProblem = Problem.objects.all()
        serializer = ProblemSerializer(totalProblem, many = True)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes([AllowAny])
    def searchNameProblem(self, request, name):
        # 이름 검색해서 나온 값 주기
        totalProblem = Problem.objects.filter(name=name)
        serializer = ProblemSerializer(totalProblem, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes([AllowAny])
    def searchLevelProblem(self, request, level):
        # 난이도 검색해서 나온 값 주기
        totalProblem = Problem.objects.filter(level=level)
        serializer = ProblemSerializer(totalProblem, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes([AllowAny])
    def searchNumberProblem(self, request, number):
        # 문제 번호 검색해서 나온 값 주기
        problem = get_object_or_404(Problem, number=number)
        serializer = ProblemSerializer(problem)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @permission_classes([AllowAny])
    def allPaginationProblem(self, request):
        # 모든 문제를 (problem_seq를 정렬해서 두기)
        totalProblem = UserProblem.objects.all().order_by('problem_seq')
        serializer_class = UserProblemSerializer(totalProblem,many=True)
        # pagination_class = PostPageNumberPagination
        return super().get_queryset().filter()

    @permission_classes([AllowAny])
    def Problem(self, request, seq):
        # 문제의 seq를 받아 그 문제에 대한 정보를 모두 리턴
        totalProblem = Problem.objects.get(seq=seq)
        serializer_class = ProblemSerializer(totalProblem)
        return Response(serializer_class.data, status=status.HTTP_200_OK)

    @permission_classes([AllowAny])
    def codeBoardProblem(self, request, seq):
        # 문제의 seq를 받아 그 문제에 codeBoard 정보를 리턴 
        print(seq)
        codeBoard =  CodeBoard.objects.filter(problem_seq = seq)
        serializer_class = CodeBoardSerializer(codeBoard, many=True)   
        return Response(serializer_class.data, status=status.HTTP_200_OK)