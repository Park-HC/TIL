# Media Query

## 개요

- CSS 에서 `@media` 키워드를 활용하여 브라우저 및 디바이스 등 환경에 따라 CSS를 적용할 수 있는 방법

## 요소

```css
@meida (orientation: landscape){}

@media (orientation: portrait) {}

@media only print {}
```



## BEM(Block Element Modifier) 방법론

### Block

- 재사용 가능하고 기능적으로 독립적인 개체

### Element

- Block의 구성 요소
- 독립적으로 활용되지 않음(블록 내에서 의미)

### Modifier

- Blcok이나 Element의 속성
- 다른 형태(color, size)sk 행동(disabled, checked)

### 예시

- `block`
- `block__element`
- `block__element__modifire`



## Icon

- `<i>`로 자주 씀(이탤릭체 대체)
- https://fontawesome.com/ 등에서 참조
- 이미지 색상, 사이즈 조절 용이



## fonts

- https://fonts.google.com/
- noto sans 등 한글도 지원



## Bootstrap

### SCSS

- CSS를 만들기 위한 도구로 변수, 상속

- https://getbootstrap.com/docs/5.1/examples/carousel







- data-bs-toggle="modal" data-bs-target"#some_id"
- 