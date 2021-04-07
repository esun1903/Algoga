#from django.contrib.auth.models import User, Group
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
#이메일 인증을 위해 추가로 import 
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage, message
from django.utils.encoding import force_bytes, force_text
# from .text import message
import datetime 
import jwt
from django.conf import settings
from .utils import *
import os

from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from collections import Counter
from .get_data import *



  
@permission_classes([AllowAny])
class UserViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,View): 

    serializer_class = UserSerializer				
    
    def login(self, request):
         
        loginUser =  User.objects.filter(email =request.data["email"] , password = request.data["password"])
        
        if loginUser.exists():
            serializer = UserSerializer(loginUser, many=True) 
            access_token= generate_access_token(request.data["email"])
          
            Response.data = {
                'access_token': access_token,
                'userInfo': serializer.data,
                     }

            return Response(Response.data,status=status.HTTP_200_OK)
    
        return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
    
    def token_verify(self, request):        
        
        try:
            access_token = request.data["access_token"]
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')

        user = User.objects.filter(email=payload['user_id']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        access_token= generate_access_token(request.data["email"])
        Response.data = {
                'access_token': access_token,
             
                     }

        return Response(Response.data,status=status.HTTP_200_OK)
    
    def signUp(self, request): 
        #회원가입 시 
        users =  User.objects.filter(email =request.data["email"])

        if users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        userSerializer = UserSerializer(data=request.data, partial=True)
        if not userSerializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        userSerializer.save()

        return Response(status=status.HTTP_201_CREATED)

    def sendEmail(self, request, email):
        print(settings.DOMAIN)
        message = render_to_string('activation_email.html', {
                'email': email,
                'domain': settings.DOMAIN,
                'token' : email_token(email)
            })

        email = EmailMessage(
            'ALGOGA 회원가입 인증 메일입니다.',                # 제목
            message,       # 내용
            to=[email],  # 받는 이메일 리스트
        )
        email.send()   
        return Response(status=status.HTTP_200_OK)
    

    def emailAuthenticate(self, request, email,token):
        
        try:
            access_token = token
            payload = jwt.decode(
                access_token, settings.SECRET_KEY, algorithms=['HS256'])

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('access_token expired')
        except IndexError:
            raise exceptions.AuthenticationFailed('Token prefix missing')

        user = User.objects.filter(email=payload['user_id']).first()
        if user is None:
            raise exceptions.AuthenticationFailed('User not found')

        users =  User.objects.filter(email =email)
        users.update(is_active =1)   
        
        return Response(status=status.HTTP_200_OK)
     
    
    def passEmailCheck(self, request, email):

        users =  User.objects.filter(email =email,is_active =1)
        if not users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        return Response(True,status=status.HTTP_200_OK)

      
    def nicknameCheck(self, request, nickname):

        users =  User.objects.filter(nickname = nickname)
        if users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        return Response(status=status.HTTP_200_OK)
    
    def emailoverlapCheck(self, request, email):

        users =  User.objects.filter(email = email)
        if users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        return Response(status=status.HTTP_200_OK)     
         
    
    def findPassword(self, request, email):
        
        users =  User.objects.filter(email = email)
        if not users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        user =  User.objects.get(email=email)
        email = EmailMessage(
            'ALGOGA의 비밀번호 입니다.',                # 제목
            user.password,       # 내용
            to=[email],  # 받는 이메일 리스트
        )
        email.send()
        return Response(status=status.HTTP_200_OK)  

    def userInfo(self,request, seq):

        users =  User.objects.get(seq = seq)
        serializer = UserSerializer(users)
        print(serializer.data)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def userInfoUpdate(self,request, email ,format=None):

        users =  User.objects.filter(email=email)
        if not users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        userInfoModify = User.objects.get(email=email)
        userInfoModify.password = request.data["password"]
        userInfoModify.baek_id  = request.data["baek_id"]
        userInfoModify.nickname = request.data["nickname"]
        userInfoModify.profile_image = request.data["profile_image"]
        userInfoModify.save()

        return Response(status=status.HTTP_200_OK)

    def Userdelete(self,request,email): 
        
        users = User.objects.filter(email = email)
        if not users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
       
        users.delete()
        
        return  Response(status=status.HTTP_200_OK)
    
    
    # 사용자가 푼 알고리즘 수
    def UserTypeInfo(self, request, seq): 
        
        users = User.objects.filter(seq = seq)
        if not users.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        # 맞은 문제만 리턴
        user_problems = CodeBoard.objects.filter(user_seq = seq).values_list('problem_seq')
        user_problems = list(set(map(lambda x: x[0], user_problems)))
        
        print(user_problems)

        # 맞은 문제 번호로 문제별 알고리즘 가져오기
        user_type = Problem.objects.filter(seq__in=user_problems).values_list('algorithm_ids')
        user_type = list(map(lambda x: x[0].split(","), user_type))
        
        type_dict = make_type_dict()

        user_type = Counter([type_dict[int(type_id)] for types in user_type for type_id in types]).most_common()

        List = []
        for key, value in user_type:
            List.append({'type_name': key, 'type_cnt': value})

        return Response(List, status=status.HTTP_200_OK)
    
    def FollowUser(self,request,user_follower_seq, user_following_seq): 
        users = FollowUser.objects.filter(user_follower_seq = user_follower_seq)

        # 만약 중복된 값이 있다면 406리턴 
        for one_user in users :
            if one_user.user_follower_seq == user_follower_seq and one_user.user_following_seq == user_following_seq :
                return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        
        follower_id = User.objects.get(seq = user_follower_seq)
        following_id = User.objects.get(seq = user_following_seq)

        FollowUser.objects.create(
             user_follower_seq = follower_id.seq,
             user_following_seq = following_id.seq
        )

        return  Response(status=status.HTTP_200_OK)
    
    #user가 팔로잉하는 사람들의 List
    def FollowingList(self,request,user_follower_seq): 
        followingusers = FollowUser.objects.filter(user_follower_seq = user_follower_seq)
    
        if not followingusers.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = FollowingListSerializer(followingusers, many=True)
        
        return  Response(serializer.data, status=status.HTTP_200_OK)
    
    #user를 팔로워하는 사람들의 List
    def FollowerList(self,request,user_following_seq): 
        followerusers = FollowUser.objects.filter(user_following_seq = user_following_seq)
    
        if not followerusers.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = FollowerListSerializer(followerusers, many=True)
        
        return  Response(serializer.data, status=status.HTTP_200_OK)

    def DeletefollowingUser(self,request,user_follower_seq, user_delete_following_seq): 
        users = FollowUser.objects.get(user_follower_seq = user_follower_seq , user_following_seq = user_delete_following_seq )

        users.delete()

        return  Response(status=status.HTTP_200_OK)
    
    def DeletefollowerUser(self,request,user_following_seq, user_delete_follower_seq): 
        users = FollowUser.objects.get(user_following_seq = user_following_seq , user_follower_seq = user_delete_follower_seq )

        users.delete()

        return  Response(status=status.HTTP_200_OK)


@permission_classes([AllowAny])
class codeBoardViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,View):
    
    serializer_class = CodeBoardSerializer
   
    def codeBoardAll(self, request):

        boardcodes = CodeBoard.objects.all()
        serializer = CodeBoardSerializer(boardcodes, many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)

    def codeBoardLike(self, request, codeBoard_seq, user_seq):

        codeboardlike = CodeBoardLike.objects.filter(code_board_seq = codeBoard_seq) 
        codeBoard =  CodeBoard.objects.get(seq =codeBoard_seq)
    
        # 만약 중복된 값이 있다면 406리턴 
        for one_codeboardlike in codeboardlike : #만약 좋아요기록이 이미 있다면?
            if one_codeboardlike.code_board_seq == codeBoard_seq and one_codeboardlike.user_seq == user_seq :
                codeBoard.like_cnt =  codeBoard.like_cnt-1
                codeBoard.save()
                one_codeboardlike.delete()
                return Response(status=status.HTTP_200_OK)
        
        CodeBoardLike.objects.create(
             code_board_seq = codeBoard_seq,
             user_seq = user_seq
        )
        codeBoard.like_cnt =  codeBoard.like_cnt + 1
        codeBoard.save()
        return Response(status=status.HTTP_200_OK)
    
    def codeBoardLike_User(self, request, codeBoard_seq):

        codeboardlike = CodeBoardLike.objects.filter(code_board_seq = codeBoard_seq) 
        user = list()
        # 만약 중복된 값이 있다면 406리턴 
        for one_codeboardlike in codeboardlike : #만약 좋아요기록이 이미 있다면?
            user.append(one_codeboardlike.user_seq)
                
        return Response(user,status=status.HTTP_200_OK)

    def codeBoardUser(self, request, email):

        seq = User.objects.get(email=email)
        userseq = seq.seq
        print(userseq)
        codeBoards =  CodeBoard.objects.filter(user_seq =userseq)
        serializer = CodeBoardSerializer(codeBoards, many=True)

        return Response(serializer.data,status=status.HTTP_200_OK)
    

    def codeBoardPage(self, request , codeBoard_seq):
       
        codeBoard =  CodeBoard.objects.filter(seq =codeBoard_seq)
        if not codeBoard.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = CodeBoardSerializer(codeBoard, many=True)    

        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def codeBoardRegister(self, request):
        
        codeBoardSerializer = CodeBoardSerializer(data=request.data, partial=True)
        if not codeBoardSerializer.is_valid():
            print(request.data)
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        
        problem_seq = request.data['problem_seq']
        language = request.data['language']
        language_seq = request.data['language_seq']

        problem = Problem.objects.filter(seq=problem_seq)

        problem_languages = problem.values_list('languages', flat=True)[0].split(',')
        problem_languages.append(language)
        problem_languages = ','.join(list(set(problem_languages)))

        problem_language_seqs = problem.values_list('language_seqs', flat=True)[0].split(',')
        problem_language_seqs.append(str(language_seq))
        problem_language_seqs = ','.join(list(set(problem_language_seqs)))

        problem.update(languages = problem_languages , language_seqs = problem_language_seqs)

        codeBoardSerializer.save()

        return Response(status=status.HTTP_201_CREATED)
    
    def codeBoardUpdate(self, request, codeBoard_seq):
        
        codeBoard =  CodeBoard.objects.filter(seq =codeBoard_seq)
        if not codeBoard.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        codeBoard.update(code =request.data["code"],explanation  =request.data["explanation"],free_write =request.data["free_write"],problem_seq=request.data["problem_seq"],language_seq=request.data["language_seq"])
        return Response(status=status.HTTP_200_OK)


    def codeBoardDelete(self, request, codeBoard_seq):

        codeBoard = CodeBoard.objects.filter(seq =codeBoard_seq)
        if not codeBoard.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        problem_seq = codeBoard.values('problem_seq')[0]['problem_seq']
        language = codeBoard.values('language')[0]['language']
        language_seq = codeBoard.values('language_seq')[0]['language_seq']

        languages = CodeBoard.objects.filter(problem_seq=problem_seq).values_list('language', flat=True)
        
        if Counter(languages)[language] == 1:
            problem = Problem.objects.filter(seq=problem_seq)

            problem_languages = problem.values_list('languages', flat=True)[0].split(',')
            problem_languages.remove(language)
            problem_languages = ','.join(problem_languages)

            problem_language_seqs = problem.values_list('language_seqs', flat=True)[0].split(',')
            problem_language_seqs.remove(str(language_seq))
            problem_language_seqs = ','.join(problem_language_seqs)

            problem.update(languages = problem_languages , language_seqs = problem_language_seqs)
       
        codecomment = Comment.objects.filter(code_board_seq =codeBoard_seq)
        for one_codecomment  in codecomment:
            one_codecomment.delete()

        codeBoard.delete()
   
        return  Response(status=status.HTTP_200_OK)

@permission_classes([AllowAny])
class commentViewSet(viewsets.GenericViewSet,mixins.ListModelMixin,View):

    serializer_class = CommentSerializer

    def commentRegister(self, request):
        commentSerializer = CommentSerializer(data=request.data, partial=True)
        if not commentSerializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
  
        commentSerializer.save()


        return  Response(status=status.HTTP_201_CREATED)   

    def commentUpdate(self, request, comment_seq):
        
        comment =  Comment.objects.filter(seq =comment_seq)
        if not comment.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        comment.update(text =request.data["text"])
        return Response(status=status.HTTP_200_OK)
    
    def commentDelete(self, request, comment_seq):

        comment =  Comment.objects.filter(seq =comment_seq)
        if not comment.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        comment.delete()
        
        return  Response(status=status.HTTP_200_OK)
    
    def commentList(self, request , codeBoard_seq):
       
        comments =  Comment.objects.filter(code_board_seq = codeBoard_seq)
        if not comments.exists():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

        serializer = CommentSerializer(comments, many=True)    

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post (self, request, format=None):
        serializers = PhotoSerializer(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status= status.HTTP_201_CREATED)
        return Response(serializers.errors, status= status.HTTP_400_BAD_REQUEST)