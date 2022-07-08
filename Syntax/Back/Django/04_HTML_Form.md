# HTML

## 태그, 속성

### forms

#### 개요

- 웹에서 사용자 정보를 입력하는 여러 방식 제공
- 사용자로부터 할당된 데이터를 서버로 전송

#### 핵심 속성

- `action`: 입력 데이터가 전송될 URL 지정
- `method`: 입력 데이터 전달 방식 지정



### input

#### 개요

- 사용자로부터 데이터를 입력 받기 위해 사용
- type 속성에 따라 동작 방식이 달라짐

#### 핵심 속성

- `name`: 중복 가능, 양식 제출 시 name이라는 이름에 설정된 값을 넘겨서 값을 가져올 수 있음
- name은 key, value는 value로 GET/POST 방식으로 전달시 매핑됨



### label

#### 개요

- 사용자 인터페이스 항목에 대한 설명(caption) 나타냄
- `input`에 `id`속성 부여 후 `label`에는 `input`의 `id`와 동일한 값의 `for` 속성 필요
- `label`을 클릭해서 `input`에 focus를 맞춰서 활성화(activate)시킬 수 있음



### for

- for 속성의 값과 일치하는 id를 가진 문서의 첫 번째 요소 제어
  - 연결된 요소가 labelable elements인 경우 이 요소에 대한 labeled control이 됨
- `labelable elements`
  - label 요소와 연결할 수 있는 요소
  - `button`, `input(not hidden type)`, `select`, `textarea`...



### id

- 전체 문서에서 고유해야 하는 식별자
- linking, scripting, styling 시 요소를 식별



## request method

- 주어진 리소스가 수행 할 작업을 나타내는 request methods 정의



### GET

- 서버로부터 정보를 조회하는 데 사용
- 데이터를 가져올 때만 사용해되야 함
- DB에 변화를 주지 않음
- CRUD에서 read를 담당
- 데이터를 서버로 전송할 때 body가 아닌 Query String Protocol를 통해 전송



### POST

- 서버로 데이터를 전송할 때 사용
- 리소스를 생성/변경하기 위해 데이터를 HTTP body에 담아 전송
- 서버에 변경사항을 만듦
- CRUD에서 create, update, delete를 담당



## 사이트 간 요청 위조(Cross-site request forgery)

- 웹 애플리케이션 취약점 중 하나
- 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여 특정 웹페이지를 보안에 취약하게 하거나, 수정 삭제 등의 작업을 하게 만드는 공격 방법
- Django는 CSRF에 대항하여 middleware와 template tag 제공



### CSRF 공격 방어

#### Secrutiy Token 사용 방식

- 사용자의 데이터에 임의의 난수 값 부여
- 매 요청 때마다 해당 난수값을 포함하여 전송
- 이후 서버에서 요청 받을 대마다 전달된 token 값이 유효한지 검증

- 일반적으로 데이터 변경이 가능한 POST, PATCH, DELETE Method 등에 적용(GET 제외)
- Django는 CSRF token 템플릿 태그 제공



#### csrf_token template tage

```python
{% csrf_token %}
```

- input type이 hidden으로 작성
- value는 Django에서 생성한 hash 값
- 해당 태그 없이 요청을 보내면 Django 서버는 403 forbidden을 응답



#### CsrfViewMiddelware

```python
MIDDELWARE = [
    'django.middleware.csrf.CsrfViewMiddleware'
]
```



- CSRF 공격 관련 보안 설정은 settings.py에서 MIDDELWARE에 작성되어 있음
- 실제 요청 과정에서 urls.py 이전 Middleware 설정 사항을 순차적으로 거침
- 응답은 하단에서 상단으로 미들웨어 적용

##### Middleware

- 공통 서비스 및 기능을 애플리케이션에 제공하는 소프트웨어
- 데이터 관리, 애플리케이션 서비스, 메시징, 인증 및 API 관리는 주로 미들웨어를 통해 처리

