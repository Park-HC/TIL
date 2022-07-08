# Shortcuts functions

- render()
- redirect()

## get_object_or_404()

- 모델 manager인 objects에서 get()을 호출
- 해당 객체가 없을 경우 DoesNotExist 예외 대신 Http 404를 raise
- get()의 경우 조건에 맞는 데이터가 없을 경우 예외를 발생시킴
  - 코드 실행 단계에서 발생한 예외 및 에러에 대해 브라우저는 500 Error 발생시킴
- 상황에 따라 적절한 예러를 발생시키기 위해 사용

- 외부에서 데이터를 받을 때(API 등) 사용
- 내부에서 데이터를 작성하는 사이트에선 사용이 곤란할 수 있음



# Decorators

- 다양한 HTTP 기능을 지원하기 위해 view 함수에 적용할 수 있는 것
- 어떤 함수에 기능을 추가하고 싶을 때, 해당 함수를 수정하지 않고 기능을 연장해주는 함수



## Allowed HTTP methods

- 요청 메서드에 따라 view 함수에 대한 엑세스를 제한
- 요청이 조건을 충족시키지 못하면 HttpResponseNotAllowed를 return(405 Method Not Allowed)



1. require_http_methods()
   - view 함수가 특정한 method 요청에 대해서만 허용하도록 하는 데코레이터
2. require_POST()
   - view 함수가 POST method 요청만 승인하도록 하는 데코레이터
3. require_safe()
   - view 함수가 GET 및 HEAD method만 허용하도록 요구하는 데코레이터
   - django는 require_GET 대신 require_safe() 사용을 권장



# Media file

- 사용자가 웹에서 업로드하는 정적 파일
- 유저가 업로드 한 모든 정적 파일

## Model filed

### ImageField()

- 이미지 업로드에 사용하는 모델 필드
- FileField를 상속받는 서브 클래스이기 때문에 FileField의 모든 속성 및 메서드를 사용 가능하며, 더해서 사용자에 의해 업로드 된 객체가 유효한 이미지인지 검사
- ImageField 인스턴스는 최대 길이가 100자인 문자열로 DB에 생성
- max_length 인자를 사용하여 최대 길이 변경 가능
- Pillow 라이브러리 필요



### FileField()

- 파일 업로드에 사용하는 모델 필드
- 2개의 선택 인자를 가지고 있음
  1. upload_to
  2. storage



### 작성법

- upload_to = 'images/'
  - 실제 이미지가 저장되는 경로 지정
- blank=True
  - 이미지 필드에 빈 값(빈 문자열)이 허용되도록 설정(이미짖 선택적으로 업로드 가능해짐)



### upload_to argument

#### 문자열 경로 지정 방식

- 파이썬의 strftime() 형식이 포함될 수 있음
- 파일 업로드 날짜/시간으로 대체 됨
- time.strftime(format[, t])
  - 날짜 및 시간 객체를 문자열 표현으로 변환하는 데 사용
  - 하나 이상의 형식화된 코드 입력을 받아 문자열 표현을 반환

#### 함수 호출 방식



### Model field option

#### blank

- 기본 값 False
- Ture인 경우 필드를 비워 둘 수 있음
  - DB에는 ''(빈 문자열)이 저장됨
- 유효성 검사에서 사용 됨(is_valid)
  - 모델 필드에 blank=True를 작성하면 form 유효성 검사에서 빈 값을 입력할 수 있음

#### null

- 기본 값 False
- True인 경우 django는 빈 값에 대해 DB를 NULL로 저장
- CharField, TextField와 같은 문자열 기반 필드에서는 사용을 피해야 함
  - 문자열 기반 필드에 True로 설정시 '데이터 없음'에 빈 문자열과 NULL 2가지 가능한 값이 있게 됨
  - 대부분의 경우 '데이터 없음'에 대해 두 개 이상의 가능한 값을 갖는 것은 중복
  - Django의 경우 기본적으로 빈 문자열을 '데이터 없음'으로 설정함
- DB에만 영향을 주므로 form에서 빈 값을 허용하고 싶으면 balnk=True를 해야함



### ImageField(FileFiield)를 사용하기 위한 단계

1. settings.py에 MEDIA_ROOT, MEDIA_URL 설정
2. upload_to 속성을 정의해 업로든 된 파일에 사용할 MEDIA_ROOT의 하위 경로를 지정
3. 업로드 된 파일의 경로는 django가 제공하는 'url' 속성을 통해 얻을 수 있음



### MEDIA_ROOT

- 사용자가 업로드 한 파일(미디어 파일)들을 보관할 디렉토리의 절대 경로
- django는 성능을 위해 업로드 파일은 데이터베이스에 저장하지 않음
  - 파일의 경로를 저장
- MEDIA_ROOT와 STATIC_ROOT는 겹쳐선 안 됨



### MEDIA_URL

- MEDIA_ROOT에서 제공되는 미디어를 처리하는 URL
- 업로드 된 파일의 주소(URL)를 만들어 주는 역할
  - 웹 서버 사용자가 사용하는 public URL
- 비어 있지 않은 값으로 설정한다면 반드시 `/`로 끝나야 함
- MEDIA_URL과 STATIC_URL은 겹쳐선 안 됨



# 이미지 업로드(CREATE)

## form 태그 - enctype(인코딩) 속성

### multipart / form-data

- 파일/이미지 업로드 시에 반드시 사용해야 함
- 전송되는 데이터와 형식을 지정
- `<input type = 'file'>` 사용시 사용



## input 요소 - accept 속성

- 이력 허용할 파일 유형을 나타내는 문자열
- 쉼표로 구분된 고유 파일 유형 지정자
- 파일을 검증하는 것은 아님