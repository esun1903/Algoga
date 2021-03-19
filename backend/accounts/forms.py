from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ('user_email', 'user_baek_id', 'user_password','user_nickname')
         # 이메일, 비밀번호, 백준 아이디, 닉네임, 프로필이미지(기본) , 회원가입날짜