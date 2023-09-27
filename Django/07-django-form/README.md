# Django Form
-----

## Intro

### &rarr; HTML - Form

- 지금까지 사용자로부터 데이터를 받기 위해 활용한 방법
- 그러나 비정상적 혹은 악의적인 요청을 필터링 할 수 없음

--> 유효한 데이터인지에 대한 확인이 필요

### &rarr; 유효성 검사

- 수집한 데이터가 정확하고 유효한지 확인하는 과정

### &rarr; 유효성 검사 구현

- 유효성 검사를 구현하기 위해서는 입력 값, 형식, 중복, 범위, 보안 등 많은 것들을 고려해야 함

- 이런 과정과 기능을 직접 개발하는 것이 아닌 Django가 제공하는 Form을 사용

------

## Django Form

### &rarr; Django Form

- 사용자 입력 데이터를 수집하고, 처리 및 유효성 검사를 수행하기 위한 도구

--> 유효성 검사를 단순화 하고 자동화 할 수 있는 기능을 제공


### &rarr; Widgets

- Widgets
: HTML 'input' element의 표현을 담당

- Widget 사용
    - widget은 단순히 input 요소의 속성 및 출력되는 부분을 변경하는 것

------

## Django ModelForm

### &rarr; Form & ModelForm

- Form
: 사용자 입력 데이터를 DB에 저장하지 않을 때 (ex. 로그인)

- ModelForm
: 사용자 입력 데이터를 DB에 저장해야 할 때 (ex. 게시글, 회원가입)

### &rarr; ModelForm

- Model과 연결된 Form을 자동으로 생성해주는 기능을 제공
    - Form + Model


### &rarr; ModelForm class 정의

```python
# articles/forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # 모델 등록만 하면 됨
    class Meta:
        model = Article
        fields = '__all__'
```

### &rarr; Meta class

- Model Form의 정보를 작성하는 곳

### &rarr; fields 및 exclude 속성

- exclude 속성을 사용하여 모델에서 포함하지 않을 필드를 지정할 수도 있음

```python
# articles/forms.py

from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    # 모델 등록만 하면 됨
    class Meta:
        model = Article
        fields = ('title',)     # field
        exclude = ('title',)    # exclude
```

### &rarr; ModelForm을 적용한 create 로직

```python
from .forms import ArticleForm

def create(request):
    form = ArticleForm(request.POST)

    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```

### &rarr; is_valid()

- 여러 유효성 검사를 실행하고, 데이터가 유효한지 여부를 Boolean으로 변환

- 공백 데이터가 유효하지 않는 이유와 에러메세지가 출력되는 과정
    - 별도로 명시하지 않았지만 모델 필드에는 기본적으로 빈 값은 허용하지 않는 제약조건이 설정 되어있음
    - 빈값은 is_valid()에 의해 False로 평가되고 form 객체에는 그에 맞는 에러 메세지가 포함되어 다음 코드로 진행됨

```python
#articles/views.py
from .forms import ArticleForm

def create(request):
    form = ArticleForm(request.POST)
    # 유효성 검사
    if form.is_valid():
        article = form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```


### &rarr; ModelForm을 적용한 edit 로직


```python
# articles/views.py

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)
```

```html
<!-- articles/edit.html -->

<h1>EDIT</h1>
  <form action="{% url "articles:update" article.pk %}" method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <input type="submit">
  </form>
```

### &rarr; ModelForm을 적용한 update 로직

```python
# articles/views.py

def update(request, pk):
    article = Article.objects.get(pk=pk)
    form = ArticleForm(request.POST, instance=article)
    if form.is_valid:
        form.save()
        return redirect('articles:detail', article.pk)
    context = {
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

### &rarr; save()

- 데이터베이스 객체를 만들고 저장
- save() 메서드가 생성과 수정을 구분하는 방법
    - 키워드 인자 instance 여부를 통해 생성할 지, 수정할 지를 결정


```python
# CREATE
form = ArticleForm(request.POST)
form.save()

# UPDATE
form = ArticleForm(request.POST, instance=article)
form.save()
```


### &rarr; Django Form 정리

- 사용자로부터 데이터를 수집하고 처리하기 위한 강력하고 유연한 도구
- HTML form의 생성, 데이터 유효성 검사 처리를 쉽게 할 수 있도록 도움


------

## Handling HTTP requests

### &rarr; view 함수 구조 변화

- new & create view 함수 간 공통점과 차이점
    - 공통점
    : 데이터 생성을 구현하기 위함
    - 차이점
    : new는 GET method 요청만을, create는 POST method 요청만을 처리

--> HTTP request method 차이점을 활용해 view 함수 구조 변경

- new & create 함수 결합

```python
from .forms import ArticleForm

def create(request):
    # 요청의 메서드가 POST라면 (create)
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검사
        # 유효성 검사가 통과된 경우
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)

    # 요청의 메서드가 POST가 아니라면 (new)
    else:
        form = ArticleForm()

    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)
```
