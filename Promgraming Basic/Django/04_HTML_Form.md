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

- 전체 문서에서 고유(must be unique)해야 하는 식별자
- linking, scripting, styling 시 요소를 식별



## request method

- 주어진 리소스가 수행 할 작업을 나타내는 request methods 정의



### GET

- 서버로부터 정보를 조회하는 데 사용
- 데이터를 가져올 때만 사용해야 함
- 데이터를 서버로 전송할 때 body가 아닌 Query String Protocol를 통해 전송
- 

