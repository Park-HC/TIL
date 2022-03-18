# Django

## 개요

- Django는 높은 레벨의 파이썬 웹 프레임 워크
- `you can focus on writing your app without needing to reinvent the wheel`



## 세팅

1. 가상환경 생성 및 활성화

   ```python
   python -m venv venv
   source venv/Script/activate
   ```

2. Django 설치

   ```python
   pip install django==3.2.12
   # ==3.2.12를 명시하지 않으면 현재 최신버젼인 4버젼이 설치됨
   # 3.2 버전이 LTS(장기 지원 버전)이므로 더 안정성이 높음
   ```

3. 프로젝트 생성

   ```python
   django-admin startproject <프로젝트명> .
   # . 를 쓰지 않아도 생성되나, 사용하기 복잡해짐
   # . 를 씀으로서 프로젝트 폴더가 본 폴더에 바로 생성되고 manage.py가 이곳에서 생성됨
   ```

4. 서버 활성화

   ```python
   python manage.py runserver
   ```

   

## Project

### 구성

```python
__init__.py
# Python에게 이 디렉토리를 하나의 Python 패키지로 다루도록 지시

asgi.py
# Asynchronous Server Gateway Interface
# Django 애플리케이션이 비동기식 웹 서버와 연결 및 소통하는 것을 도움

settings.py
# 애플리케이션의 모든 설정을 포함

urls.py
# 사이트의 url과 적절한 view의 연결을 지정

wsgi.py
# Web Server Gateway Interface
# Django 애플리케이션의 웹서버와 연결 및 소통하는 것을 도움

manage.py
# Django 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
```



### 개요

- Project는 Application의 집합(collection of apps)
- 프로젝트에는 여러 앱이 포함될 수 있음
- **앱은 여러 프로젝트에 있을 수 있음**



## Application

### 구성

```python
__init__.py

admin.py
# 관리자용 페이지를 설정하는 곳

apps.py
# 앱의 정보가 작성된 곳

models.py
# 앱에서 사용하는 Model을 정의한 곳

tests.py
# 프로젝트의 테스트 코드를 작성하는 곳

views.py
# view 함수들이 정의되는 곳
```



### 개요

- 일반적으로 복수형으로 작명

- 앱은 실제 요청을 처리하고 페이지를 보여주고 하는 등의 역할 담당
- 하나의 프로젝트는 여러 앱을 가짐
- 일반적으로 앱은 하나의 역할 및 기능 단위로 작성함



### 앱 등록

- settings.py의 INSTALLED_APPS 리스트에 app 명칭을 등록해야 함
- 반드시 앱 생성 후 등록해야 함
- `Local apps`, `Third party apps`, `Django apps` 등 3가지로 나눌 수 있음