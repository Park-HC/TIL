# CSS 기본 스타일

## 크기 단위

### px(픽셀)

- 모니터 해상도의 한 화소인 '픽셀' 기준
- 고정적인 단위

### %

- 백분율 단위
- 가변적인 레이아웃에 자주 적용

### em

- (바로 위 부모 요소에 대한) 상속의 영향을 받음
- 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐

### rem

- (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
- 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

### viewport

- 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
- 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
- vw, vh, vmin, vmax 등



## 색상 단위

### 색상 키워드

```css
p { color: black;}
```

- 대소문자 구분 없음
- red, blue, black 등 특정 색을 직접 글자로 나타냄

### RGB 색상

```css
p { color: #000; }
p { color: #000000; }
p { color: rgb(0, 0, 0); }
p { color: rgba(0, 0, 0, 0.5); }
```

- 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현

### HSL 색상

```css
p { color: hsl(120, 100%, 0); }
p { color: hsla(120, 100%, 0.5); }
```

- 색상, 채도, 명도를 통해 특정 색을 표현