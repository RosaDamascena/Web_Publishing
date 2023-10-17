from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

# Create your views here.
def signup(request):
    # 회원가입 버튼 클릭 -> 회원가입 할 수 있는 페이지 보여줘
    # 회원가입 할 수 있는 페이지를 사용자에게 변환
    # 렌더 함수가 하는 일 : html 파일 렌더링

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            auth_login(request, user)
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인이란 현재 사용자가 보내준 데이터를 기반으로 특정 유저를 찾는다.
            # 그 특정 유저에 대한 정보를 암호화하여 사용자에게 돌려준다.
            # 사용자는 다음 요청부터는 넘겨받았던 데이터를 함께 동봉해서 보낸다.
            # 서버는 그렇게 사용자가 보내준 암호화된 데이터를 토대로 유저를 인식한다.
            auth_login(request, form.get_user())
            return redirect('main')
    else:
        form = AuthenticationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    # session에서 연결된 user 정보 제거
    if request.method == 'POST':
        auth_logout(request)
        
    return redirect('accounts:login')