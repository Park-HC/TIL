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



### 사용 모델 필드

#### CharField(max_length=None, **options)

- 길이의 제한이 있는 문자열을 넣을 때 사용
- CharField의 max_length는 필수 인자
- 필드의 최대 길이(문자), 데이터베이스 레발과 Django의 유효성 검사(값을 검증하는 것)을 활용

### TextField(**options)

- 글자의 수가 많을 때 사용
- max_length 옵션 작성시 자동 양식 필드인 textarea 위젯에 반영되나 모델과 데이터베이스에는 적용 안 됨



## Migrations

- Django가 model에 생긴 변화를 반영하는 방법



### Commands

#### makemigartions

`$ python manage.py makemigrations`

- model을 변경한 것에 기반한 새로운 마이그레이션을 만들 때 사용
- `migrations/0001_init.py` 파일 등 생성

#### migrate

`$ python manage.py migrate`

- 마이그레이션을 DB에 반영하기 위해 사용
- 설계도를 실제 DB에 반영하는 과정
- 모델에서의 변경 사항들과 DB의 스키마가 동기화를 이룸

#### sqlmigrate

- 마이그레이션에 대한 SQL 구문을 보기 위해 사용
- 마이그레이션이 SQL 문으로 어떻게 해석되어 동작할지 미리 확일할 수 있음

#### showmigrations

- 프로젝트 전체의 마이그레이션 상태를 확인하기 위해 사용
- 마이그레이션 파일들이 migrate 됐는지 안됐는지 여부를 확일할 수 있음



### DateField option

- DataTimeField는 Datefield와 동일한 추가 인자(extra argument) 사용
- DataTimeField는 Datefield의 서브 클래스

#### auto_now_add

- 최초 생성 일자
- Django ORM이 최초 insert(테이블에 어떤 값을 최초로 넣을 때)시에만 현재 날짜와 시간으로 갱신

#### auto_now

- 최종 수정 일자
- Django ORM이 save 할 대마다 현재 날짜와 시간으로 갱신

