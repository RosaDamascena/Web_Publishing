from django.shortcuts import render
from .models import Articles

# Create your views here.
def index(request):
    # DB에서 전체 게시글 조회 후 받은 전체 데이터 게시글 데이터를 변수에 담아
    # index 템플릿에서 사용할 수 있도록 전달
    articles = Articles.objects.all()
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)