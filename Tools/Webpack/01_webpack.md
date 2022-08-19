# Webpack

## 개요

- 모듈 번들링
  - html 파일에 들어가는 js 파일들을 하나의 자바스크립트 파일로 만들어 주는 방식
  - 필요한 다수의 js 파일을 하나의 자바 스크립트 파일로 만들어 주는 것



## 필요성

- SPA의 대두로 하나의 html 페이지에 여러 개의 js 파일들을 포함시켜야 함
- 연관 되어 있는 js 종속성 있는 파일들을 하나의 파일로 묶어 관리하기 편하게 함
- 여러 파일을 하나의 파일로 번들링해 웹페이지 성능을 최적화 시킴



## Babel

- 최신 ES6버전을 구 버전인 ES5로 변환시켜줌
- ES6은 대부분의 에버그린 브라우저를 지원하지만, IE11은 그렇지 않아서 ES5 버젼으로 바꿔줘야 함
- 근데 지금은 IE11 끝났는데...?
  - 몰라도 될 듯



### +) 에버그린 브라우저

- 사용자에 대한 별도의 재설치를 요구하지 않고도 자동 업데이트가 가능한 브라우저
- 사용자의 편의성과 빠른 업데이트 적용을 위해 설계된 방식
- 빠른 업데이트 정책에 호환의 어려움이 발생할 수 있지만, 최대한 이를 고려하여 업데이트된다고 함
- Chrome, Firefox, Microsoft Edge 등이 해당 됨
