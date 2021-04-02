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

USER_PAGE = "https://www.acmicpc.net/user/"

@permission_classes([AllowAny])
class ProblemViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,View):
    
    serializer_class = UserProblemSerializer
    # serializer_problem_class = 
    # 내가 푼 문제와 내 레벨 가져오기, [0] : 맞은 문제 / [-1] : 시도했지만 틀린 문제

    # 사용자가 '문제 불러오기'를 클릭하면
    def callProblem(self, request, seq):
        
        user = User.objects.get(seq=seq)

        # 1. 백준에서 사용자 아이디가 푼 문제 가져오기
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

        # 푼 문제가 적을 경우 브론즈5문제 중 제출 많은 애들 추천
        if len(correct_problems) + len(incorrect_problems) < 10:
            recommend_problem = totalProblem.filter(level=1).order_by('-submission_cnt')[:20]
            serializer = ProblemSerializer(recommend_problem, many=True)
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        # 3) 기존 DB에 있는 사용자가 푼 문제들 삭제
        UserProblem.objects.filter(user_seq=user.seq).all().delete()
        
        # 4) DB에 푼 문제들 넣기, 맞으면 0, 틀리면 1
        # bulk_create??
        for number in correct_problems:
            problem_seq = problem2seq[number]
            UserProblem.objects.create(problem_seq = totalProblem.get(seq = problem_seq), user_seq = user, correct = 0)
        
        for number in incorrect_problems:
            problem_seq = problem2seq[number]
            UserProblem.objects.create(problem_seq = totalProblem.get(seq = problem_seq), user_seq = user, correct = 1)

        # 5) 사용자 레벨 다시 구하기
        problem_exp = make_problem_exp_dict()
        level_exp = make_level_exp_dict()

        exp = sum(list(map(lambda x : problem_exp[x], correct_problems)))

        # 경험치에 맞는 레벨 계산
        calc_level = 0
        for cur_level in range(30, 0, -1) :
            if level_exp[cur_level - 1] <= exp :
                calc_level = cur_level
                break

        # 계산한 레벨과 solved 레벨의 차이가 4,5 이상이면 계산한 레벨을 사용한다
        diff = calc_level - level
        if diff < -5 or diff > 5 :
            level = calc_level

        # 6) 문제 추천해주기
        proble_type_dict = make_problem_type_dict()

        correct_algo = []
        incorrect_algo = []

        # 맞은 문제들의 알고리즘 분류
        for problem in correct_problems :
            correct_algo += list(map(int, proble_type_dict[problem].split(',')))

        # 틀린 문제들의 알고리즘 분류
        for problem in incorrect_problems :
            incorrect_algo += list(map(int, proble_type_dict[problem].split(',')))

        # 알고리즘 분류별 개수
        correct_algo_dict = Counter(correct_algo)
        incorrect_algo_dict = Counter(incorrect_algo)

        # 추천할 알고리즘 목록들
        accept_alogithm_list = [
            124, 25, 102, 7, 175, 33, 158, 11, 125, 65, 120, 97, 12, 100, 95, 126, 6, 121, 139,
            127, 22, 141, 14, 81, 5, 24, 128, 106, 92, 45, 71, 59, 96, 80, 87, 74,
            9, 140, 39, 13, 49, 62, 8, 67, 31, 28, 78, 40, 148, 73, 43]

        # 맞은 문제에서 뽑은 추천해줄 알고리즘, 틀린 문제에서 뽑은 추천해줄 알고리즘
        recommend_algo_id_list = list(map(lambda x : x[0] , correct_algo_dict.most_common()[-10:])) + list(map(lambda x : x[0] , incorrect_algo_dict.most_common()[:10]))
        recommend_algo_id_list = list(set(recommend_algo_id_list) & set(accept_alogithm_list))

        # id로 seq 검색
        algo_seq = list(map(lambda x: x['seq'], Type.objects.filter(id__in = recommend_algo_id_list).values('seq')))

        problem_seq = list(map(lambda x: x['problem_seq'], TypeOfProblem.objects.filter(type_seq__in=algo_seq).values('problem_seq').distinct()))

        # 추천할 문제 중 나의 레벨과 유사한 문제면서 내가 풀어보지 못한 문제를 제출수와 난이도 내림차순으로 정렬해서 20개만 보여주자
        recommend_problem = totalProblem.filter(seq__in=problem_seq).filter(level__range=(level - 5, level + 5)).exclude(number__in=correct_problems + incorrect_problems).order_by('-submission_cnt', '-level')[:20]
        
        serializer = ProblemSerializer(recommend_problem, many=True)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @permission_classes([AllowAny])
    def allProblem(self, request):
        # 모든 문제 주기
        # 모든 문제를 줄 때
        totalProblem = Problem.objects.all()
        List = list()
        serializer = ProblemCustomSerializer
        for problem in totalProblem:
            print(problem.seq)
            test = CodeBoard.objects.filter(problem_seq=problem.seq)
            one_problem = {'seq': int(problem.seq), 'number': int(problem.number), 'name': problem.name,
                           'correct_user': int(problem.correct_user), 'submission_cnt': int(problem.submission_cnt),
                           'correct_rate': int(problem.correct_rate), 'level': int(problem.level),
                           'avg_try': int(problem.avg_try), 'time_limit': problem.time_limit, 'memory_limit': problem.memory_limit,
                           'algorithms': problem.algorithms, 'algorithm_ids': problem.algorithm_ids, 'review_count': len(test)}

            print(one_problem)
            serializer = ProblemCustomSerializer(data=one_problem)
            List.append(one_problem)

        return Response(List, status=status.HTTP_200_OK)

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