# Template

## 개요

- `데이터 표현을 제어하는 도구이자 표현에 관련된 로직`
- Django template language(DTL)을 built-in system으로 사용함
- `urls.py`, `views.py`, `templates` 중 가장 마지막에 실행되며 보통 마지막에 코딩됨



## DTL

- Django template에서 사용하는 built-in system
- 조건, 반복, 변수 치환, 필터 등의 기능 제공
- 단순히 Pythondl HTML에 포함된 것이 아님
- 프로그래밍적 로직이 아니라 **프레젠테이션을 표현하기 위한 것**
- Python처럼 일부 프로그래밍 구조(if, for 등) 사용 가능
- **이것은 Python 코드로 실행되는 것이 아님**



### 설계 철학

- 표현(template)과 로직(view)을 분리
  - DTL은 표현을 제어하는 도구이자 표현에 관련된 로직
  - 템플릿에서 이런 기본 목표를 넘어서는 기능을 지원해선 안 됨
- 중복 배제
  - header, footer, navbar 등 사이트 공통 디자인을 템플릿 상속을 통해 중복 코드를 없에고 한 곳에 저장



## DTL syntax

### Variable

```django
{{ variable }}
```

- render()를 사용하여 views.py에서 정의한 변수를 template 파일로 넘겨 사용하는 것
- 변수명은 영어, 숫자와 밑줄의 조합으로 구성될 수 있음
  - 단, 밑줄로 시작할 수 없음
  - 공백, 구두점 문자 사용 불가능
- dot(.)를 사용하여 변수 속성에 접근 가능
- render()의 세번째 인자로 {'key': value}같은 딕셔너리 형태로 넘겨줌
- 딕셔너리의 'key'가 template에 사용하는 변수명이 됨



### Filters

```python
{{ variable|filter }}

{{ name|lover }}
# name 변수를 모두 소문자로 출력
```

- 표시할 변수를 수정할 때 사용

- 60개의 built-in template filters 제공
- chained 가능
- 일부 필터는 인자를 받음



### Tags

```python
{% tag %}

{% if %}{% endif %}
```

- 출력 텍스트를 만듦
- 반복 또는 논리를 수행해 제어 흐름을 만듦
- 등 변수보다 복잡한 일들을 수행
- 일부 태그는 시작과 종료 태그 필요
- 약 24개의 built-in templates tags 제공



#### inclue

```python
{% include '' %}
```

- 템플릿을 로드하고 현재 페이지로 렌더링
- 템플릿 내에 다른 템플릿을 "포함"하는 방법
- 포함되는 템플릿은 파일 명 앞에 `_`를 포함된다는 의미로 붙이기도 함
- 템플릿 중간에 사용 가능



### Comments

```python
{# #}
```

- Django template에서 라인의 주석을 표현하기 위해 사용
- 유효하지 않은 템플릿 코드가 포함될 수 있음
- 한 줄 주석에만 사용 가능
- 여러 줄 주석은 `{% comment %}`와 `{% endcomment %}` 사이에 입력



## 템플릿 상속

- Template inheritance
- 코드의 재사용성을 높임
- 사이트의 모든 공통 요소를 포함하고, 하위 템플릿이 재정의(override)할 수 있는 블록을 정의하는 기본 **skeleton** 템플릿을 만들 수 있음

```python
# template.html

{% extends '' %}
# 자식(하위) 템플릿이 부모 템플릿을 확장한다는 것을 알림
# 반드시 템프릿 최 상단에 작성되어야 함

{% block content %} {% endblock %}
# 하위 템플릿에서 재지정(overridden) 할 수 있는 블록을 정의
# 하위 템플릿에서 채울 수 있는 공간
```

```python
# setting.py

TEMPLATES = [
    {
        'BACKEND': ...,
        'DIRS': [BASE_DIR / 'templates'],
        ....,
    }
]
# app_name/templates 외 skeleton을 작성할 프로젝트의 templates 폴더를 추가 경로로 설정
```

