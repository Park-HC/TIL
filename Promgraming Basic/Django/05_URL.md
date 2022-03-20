# URLs

## 개요

- Dispatcher(발송자, 운항 관리자)로서의 URL
- 웹 애플리케이션은 URL을 통한 클라이언트 요청에서부터 시작 됨



## Variable Routing

- URL 주소를 변수로 사용하는 것

- URL 일부를 변수로 지정하여 view 함수 인자로 넘길 수 있음

- 변수 값에 따라 하나의 path()에 여러 페이지를 연결할 수 있음

  ```python
  path('accounts/user/<int:user_pk>', views.account),
  ```



## Path converters

- `str`
  - ``/`를 제외한 비어 있는 않은 모든 문자열과 매치
  - 작성하지 않을 경우 기본 값
- `int`
  - 0 또는 양의 정수 매치
- `slug`
  - ASCII 문자 또는 숫자, 하이픈 및 밑줄 문자로 구성된 모든 슬러그 문자열과 매치



## App URL mapping

- app의 view 함수가 많아져 path() 또한 많아지고, app 또한 더 많아지기 때문에 프로젝트의 `urls.py`만으로 모두 관리하는 것은 프로젝트 유지 보수에 좋지 않음

- 그러므로 각 app에 `urls.py` 작성 필요

  ```python
  from django.urls import path, include
  
  urlpatterns = [
      path('articles/', inclue('articles.urls')),
  ]
  ```

  

## Naming URL patterns

- url 직접 작성 대신 path의() 함수의 name 인자 정의해서 사용
- Django Template Tag 중 하나인 url 태그를 사용해서 path() 함수에 작성한 name 사용 가능
- url 설정에 정의된 특정한 경로들의 의존성을 제거 가능

```python
path('index/', views.index, name='index')

<a href="{% url 'index' %}">메인 페이지</a>
```

