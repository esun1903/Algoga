from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser) : # 상속 AbstractUser 의 기본적인 속성을 상속받겠다. 
    # id는 기본적으로 처음 테이블 생성시 자동으로 만들
    user_email     = models.EmailField(max_length = 30)  # 이메일
    user_password  = models.CharField(max_length = 20) # 비밀번호
    user_baek_id = models.CharField(max_length = 20) # 백준 아이디
    user_nickname = models.CharField(max_length = 20)  # 닉네임 
    user_profile_image = models.TextField()  # 프로필 이미지
    user_register_date = models.DateTimeField(auto_now_add=True)  # 회원가입 날짜

    class Meta:
        db_table = 'user'
# Create your models here.
