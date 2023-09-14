# Django Model
------

## 1. Model

### &rarr; Django Model
- DB의 테이블을 정의하고 데이터를 조작할 수 있는 기능들을 제공
    - 테이블 구조를 설계하는 `청사진`(blueprint)


### &rarr; model 클래스 작성

```python
from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
```
- 클래스 변수명
: 테이블의 각 필드(열) 이름

- model Field 클래스
    - 테이블 필드의 데이터 타입
    - 키워드 인자(필드 옵션)
        - 테이블 필드의 제약조건 관련 설정
        - ex. (max_length = 10)


### &rarr; model 제약 조건

- 데이터가 올바르게 저장되고 관리되도록 하기 위한 규칙
    - 숫자만 저장되도록, 문자가 100자 까지만 저장되도록 하는 것 등...

## 2. Migrations

### &rarr; Migrations
- model 클래스의 변경사항(필드 생성, 수정, 삭제 등)을 DB에 최종 반영하는 방법

### &rarr; Migrations 과정
- 1. model class (설계도 초안)
-> make migrations
- 2. migration 파일 (최종 설계도)
-> migrate
- 3. db.sqlite3 (DB)

![Alt text](src/migrations.PNG)

### &rarr; Migrations 핵심 명령어 2가지

1. model class를 기반으로 최종설계도(migration) 작성

```bash
python manage.py makemigrations
```

2. 최종 설계도를  DB에 전달하여 반영

```bash
python manage.py migrate
```

## 3. Admin Site