# namespace (이름공간)

- 이름공간은 객체를구분할 수 있는 범위를 나타내는 말
- 하나의 이름 공간에서는 하나의 이름이 단 하나의 객체만을 가리킴

## django의 경우

- 서로 다른 app의 같은 이름을 가진 url name은 이름공간을 설정해서 구분
- template, static 등 django는 정해진 경로 하나로 모아서 보기 때문에 중간에 폴더를 임의로 만들어 줌으로써 이름공간을 설정



# Static files

### 웹 서버

- 특정 위치(URL)에 있는 자원(resource)을 요청(HTTP request) 받아서 제공(serving)하는 응답(HTTP response)을 처리하는 것을 기본 동작으로 함

- 자원과 접근 가능한 주소가 정적으로 연결된 관계

- 웹 서버는 요청 받은 URL로 서버에 존재하는 정적 자원(static resource)를 제공



### Static file

- 정적 파일
- 응답할 때 별도의 처리 없이 파일 내용을 그대로 보여주면 되는 파일
  - 사용자의 요청에 따라 내용이 바뀌는 것이 아님
  - 요청한 것을 그대로 보여주는 파일
- 파일 자체가 고정되어 있고, 서비스 중에도 추가되거나 변경되지 않고 고정되어 있음
- CSS, 자바스크립트, 이미지 파일등이 정적 파일에 해당함



#### Django에서

- django.contrib.sstaticfiles가 INSTALLED_APPS에 포함되어 있는지 확인
- settings.py에서 STATIC_URL을 정의
- 템플릿에서 static 템플릿 태그를 사용하여 지정된 상대경로에 대한 URL을 빌드
- 앱의 static 디렉토리에 파일을 저장