from django.shortcuts import render
import random

# Create your views here.
def index(request):
    context = {
        'name' : 'Jane',
    }
    return render(request, 'apps/index.html', context)

def dinner(request):
    foods = ['국밥', '국수', '카레', '탕수육',]
    picked = random.choice(foods)
    empty_ls = []
    context = {
        'foods' : foods,
        'pocked' : picked
    }
    return render(request, 'apps/dinner.html', context)

def search(request):
    return render(request, 'apps/search.html')

def throw(request):
    return render(request, 'apps/throw.html')

def catch(request):
    print(request)
    print(type(request))
    print(request.GET)
    print(request.GET.get('message'))
    # 사용자로부터 요청 받기
    # 요청에서 사용자 입력 데이터 찾아
    # context에 저장 후 catch 템플릿에 출력
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request, 'apps/catch.html')

def greeting(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'apps/greeting.html', context)

def detail(request, num):
    context = {
        'num' : num,
    }
    return render(request, 'apps/detail.html', context)