from django.shortcuts import render,redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def main(request):
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/main.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('main')
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, article_pk):
    if request.method == 'POST':
        article = Article.objects.get(pk=article_pk)
        article.delete()
    return redirect('main')

def likes(request, article_pk):
    if request.user.is_authenticated:
    # 특정 게시글과 요청 보낸 유저의 M:N 관계를 생성
        article = Article.objects.get(pk=article_pk)
        
        if request.user in article.like_users.all():
            # 이미 관계를 맺고 있는 상태에서 온 M:N 관계 관련 요청
            # 관계 해제 요청
            article.like_users.remove(request.user)
        else:
            article.like_users.add(request.user)
        return redirect('main')
    return redirect('accounts:login')