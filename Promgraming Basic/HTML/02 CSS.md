# CSS

> Cascading Stytle Sheets

## 개요

- 스타일을 지정하기 위한 언어
- 선택하고, 스타일을 지정한다

```css
h1 { # 선택자
    color: blue; # 선언
    font-size: 15px; # 속성, 값
}
```

- 선택자: 스타일을 지정할 HTML 요소 선택
- 선언: 중괄호 안에서 속성과 값 하나의 쌍으로 이루어짐
- 속성: 어떤 스타일 기능을 변경할지 결정
- 값: 어떻게 스타일 기능을 변경할지 결정



## 정의 방법

### 인라인(inline)

```html
<h1 style="color: blue; font-size; 100px;">Hello</h1>
```

- 해당 태그에 직접 style 속성을 활용



### 내부 참조(embedding) - `<style>`

```html
<style>
    h1 {
        color: blue;
        font-size: 100px;
    }
</style>
```

- `<head>` 태그 내에 `<style>`에 지정



### 외부 참조(link file) - 분리된 CSS 파일

```html
<link rel="stylesheet" href="mystyle.css">
```

```css
h1 {
    color: blue;
    font-size: 20px
}
```



## 계발자 도구

- styles : 해당 요소에 선언된 모든 CSS
- computed : 해당 요소에 최종 계산된 CSS



## 선택자

> Selector

### 유형

- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자



### CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다

| 상속이 되는 속성          | Text 관련 요소, opacity, visibilty 등          |
| ------------------------- | ---------------------------------------------- |
| **상속이 되지 않는 속성** | **Box model 관련 요소, position 관련 요소 등** |

