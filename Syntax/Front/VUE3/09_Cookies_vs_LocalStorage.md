# Cookies

## 개요

- 웹사이트에 의해 유저 컴퓨터에 저장되는 작은 텍스트 파일
- 최대 용량 4KB
- 방문한 페이지나 유저 로그인 정보를 저장
- 문자열만 저장 가능



## 유형

### Session Cookies

- 만료일 없음
- 브라우저나 탭이 열러있는 동안에만 저장됨
  - 브라우저 종료시 영구적으로 삭제
- 은행 등 보안이 필요한 작업에서 사용됨

### Persistent Cookies

- 만료일 있음
- 만료일까지 유저 디스크에 저장됨
  - 만기시 삭제



# Local Storage

## 개요

- HTML5에서부터 도입된 개념
- HTTP 요청에 데이터를 주고 받을 필요 없음
- 클라이언트와 서버간 전체 트래픽과 낭비되는 대역폭 양을 줄일 수 있음
  - 인터넷이 끊어져도 데이터가 삭제되지 않음
- 최대 용량 5MB
- Javascript로 지우지 않는 이상 자동으로 삭제되지 않음
- 문자열, Javascript의 primitives와 object도 저장
- 단, 저장된 데이터의 보안 수준이 높아야 됨



> https://erwinousy.medium.com/%EC%BF%A0%ED%82%A4-vs-%EB%A1%9C%EC%BB%AC%EC%8A%A4%ED%86%A0%EB%A6%AC%EC%A7%80-%EC%B0%A8%EC%9D%B4%EC%A0%90%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9D%BC%EA%B9%8C-28b8db2ca7b2