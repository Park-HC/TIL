# DB API

## 개요

- database-abstract API 혹은 database-access API
- DB를 조작하기 위한 도구
- Django가 기본적으로 ORM을 제공하여 DB를 편하게 조작할 수 있게 함
- Model을 만들면 Django는 객체를 만들고 읽고 수정하고 지울 수 있는 database-abstract API를 자동을 만듦



## Manager

- Django 모델에 데이터베이스 query 작업이 제공되는 인터페이스
- 기본적으로 모든 Django 모델 클래스에 objects라는 Manager를 추가



## QuerySet

- 데이터베이스로부터 전달받은 객체 목록
- queryset 안의 객체는 0개, 1개 혹은 여러 개일 수 있음
- 데이터베이스로부터 조회, 필터, 정렬 등을 수행할 수 있음



## Django shell

- 장고 프로젝트 설정이 load된 Python shell을 활용해 DB API 구문 테스트



# CRUD

- 생성, 읽기, 갱신, 삭제

## CREATE

### save() method

- 객체를 데이터베이스에 저장
- 데이터 생성시 save()를 호출하기 전에는 객체의 ID 값이 무엇인지 알 수 없음
  - ID 값은 Django가 아니라 DB에서 계산
- 단순히 모델을 인스턴스화 하는 것은 DB에 영향이 미치기 않기 때문에 반드시 save() 필요



## READ

- QuerySet API method 사용

### all()

- 현재 QuerySet의 복사본 반환

### get()

- 주어진 lookup 매개변수와 일치하는 객체를 반환
- 객체를 찾을 수 없으면 DoesNotExist 예외 발생
- 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외 발생
- 그러므로 PK 같이 고유성을 보장하는 속성으로 조회해야 함

### filter()

- 주어진 lookup 매개변수와 일치하는 객체를 포함하는 새 QuerySet 반환

#### subject__contains

```python
Question.objects.filter(subject__contains='장고')
# subject 속성에서 '장고' 문자열이 포함된 Question 모델들을 찾아 QuerySet으로 반환함
```





## UPDATE

### save()

- 객체의 인스턴스 값 변경 후 save()로 저장



## DELETE

### delete()

- QuerySet의 모든 행에 대해 SQL 삭제 쿼리 수행
- 삭제된 객체 수와 객체 유형당 삭제 수가 포함된 딕셔너리 반환



## Field lookups

- 조회 시 특정 검색 조건을 지정 가능
- QuerySet 메서드 filter(), exclude() 및 get()에 대한 키워드 인수로 지정

```python
Article.objects.filter(pk__gt=2)
Article.objects.filter(content__contains='ja')
```



# Redirect

```python
from django.shortcuts import render, redirect

def create(request):
    return redirect('articles:index')
```

- 새 URL로 요청을 다시 보냄
- 인자에 따라 HttpResponseRedirect를 반환
- 브라우저는 현재 경로에 따라 전체 URL 자체를 재구성(reconstruct)
- 사용 가능한 인자
  1. model
  2. view name
  3. absolute or relative URL



## Detail

```python
# articles/urls.py
path('<int:pk>/', views.detail, name='detail')

# aricles/views.py
def detail(request, pk):
    article = Article.objects.get(pk=pk)  # variable routing
    context = {
        'article': article,
    }
    return render(request, 'article/detail.html', context)

# templates/articles/index.htmls
<a href='{% 'articles:detail' article.pk %}'>[detail]</a>
    
    
# articles/views.py
def create(request):
    return redirect('article:detail', article.pk)
```

