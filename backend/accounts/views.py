from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm,
)
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_http_methods, require_safe
from django.contrib.auth import update_session_auth_hash
from .forms import CustomUserChangeForm
from django.http import HttpResponse, JsonResponse


# 질문 1. render 에 html 말고 Vue에 보내야할 것 같은데 어떻게 보내야하는지? 
# 일반적으로 render 함수를 반환한다.  필수 인자인 request 와 template 이름을 반드시 지정해야 한다. 

# views.py 함수 정의 


# 위의 것들은 이 url에 의해 함수가 실행되기 전에 선행조건으로 걸러준다고 생각해주시면되요
# api_view에서 get요청과 post요청이 아니면 이 함수는 실행하지 않겠다라는 뜻입니다.
# 요청에 담겨저있는 요청키가 jwt가아니면 이 함수는 실행되지 않습니다 등등입니다.
# @api_view(['GET', 'POST'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])



# 회원가입 
@require_http_methods(['GET', 'POST']) #GET, POST의 요청일때만 받는다. 
def signup(request):
    try:
        print('Hello Python!')
        if request.user.is_authenticated:
            return redirect('articles:index')

        if request.method == 'POST':
            form = UserCreationForm(request.POST)
        if form.is_valid():
            print('Hello Python!2')
            user = form.save()
            auth_login(request, user)
            return HttpResponse(status=200)  # 만약, 옳다면 
        else:
            form = UserCreationForm()
        context = {
        'form': form,
        }
    except KeyError:
        return JsonResponse({"message" : "INVALID_KEYS"}, status=400)

# 로그인
@require_http_methods(['GET', 'POST'])  #GET, POST의 요청일때만 받는다. 
def login(request):
    try:
        if request.user.is_authenticated:
            return redirect('articles:index')
            
        if request.method == 'POST':
            form = AuthenticationForm(request, request.POST)
            if form.is_valid():
                # 로그인
                auth_login(request, form.get_user())
                print(request.GET.get('next'))
                # return JsonResponse({"token" : token}, status=200)
                return HttpResponse(status=200)
        else:
            form = AuthenticationForm()
        context = {
            'form': form,
        }
    except KeyError:
        return JsonResponse({"message" : "INVALID_KEYS"}, status=400)

#로그아웃
@require_POST
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
