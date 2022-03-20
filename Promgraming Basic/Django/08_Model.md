# Model

## 개요

- 단일한 데이터에 대한 정보를 가짐
  - 사용자가 저장하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조(layout)
- Django는 model을 통해 데이터에 접속, 관리
- 일반적으로 각각의 model은 하나의 데이터베이스 테이블에 매핑됨
- **웹 애플리케이션의 데이터를 구조화하고 조작하는 도구**



## Django Model

### models.py 작성

```django
class Article(models.Model):
	title = models.CharField(max_length=10)
	content = models.TextFeilde()
```

- 각 모델은 django.models.Model 클래스의 서브(자식) 클래스로 표현

- models 모듈을 통해 어떠한 타입의 DB 컬럼을 정의할 것인지 정의
  - 위 예시에서 title과 content는 모델의 필드(속성, 열)를 표현



## DB API

- DB를 조작하기 위한 도구
- Django가 기본적으로 ORM을 제공하여 DB를 편하게 조작할 수 있게 함