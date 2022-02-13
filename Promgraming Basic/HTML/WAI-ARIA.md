# WAI-ARIA

## 개념

- 마우스 등 포인팅 장비를 사용하기 힘든 스크린 리더 사용자에게
- 동적 컨텐츠(javascrpit, vue, react 등) 영역에 역할, 속성, 상태 정보를 추가해
- 동적 컨텐츠와 페이지에 대한 접근성을 높여 사용자들에게 원활한 페이지 이용을 도와줌



## 예시

```html
<li tabindex="0" class="checkbox" checked>
    Receive promotional offers
</li>
<!-- 스크린리더로 화면을 탐색하는 사용자는 위의 css 정보를 얻을 수 없음-->

<li tabindex="0" class="checkbox" role="checkbox" checked aria-checked="true">
    Receive promotional offers
</li>
<!-- 해당 영역이 체크박스인지, 체크가 되었는지 안되었는지 명시 가능-->
```



## 주의점

- 스크린 리더 이용자는 오직 ARIA의 정보에 의지하게 되기에 부정확한 정보를 제공할 경우 있느니만 못하게 됨
- 태그의 역활과 의미에 맞게 작성



## 태그별 role

| HTML 태그                 | 암묵적 기본 역할(role="")                  |
| ------------------------- | ------------------------------------------ |
| `<a href ="">`            | role = "link"                              |
| `<a>`(href 없음)          |                                            |
| `<article>`               | role = "article"                           |
| `<aside>`                 | role="complementary"                       |
| `<header>`                | role = "banner"(일반)                      |
| `<footer>`                | role = "contentinfo"(일반)                 |
| `<section>`               | role="region"(accessible name이 있을 경우) |
| `<button>`                | role="button"                              |
| `<div>`                   |                                            |
| `<dl>`                    |                                            |
| `<dt>`                    | role="term"                                |
| `<dd>`                    | role="definition"                          |
| `<fieldset>`              | role="group"                               |
| `<form>`                  | role="form"(accessible name이 있을 경우)   |
| `<h1> ~ <h6>`             | role="heading"                             |
| `<img = alt="텍스트">`    | role="img"                                 |
| `<img alt="">`            |                                            |
| `<img>`(alt 없음)         | role="img"                                 |
| `<ul>`                    | role="list"                                |
| `<ol>`                    | role="list"                                |
| `<li>`                    | role="listitem"                            |
| `<nav>`                   | role="navigation"                          |
| `<svg>`                   | role="graphics-document"                   |
| `<input type="button">`   | role="button"                              |
| `<input type="checkbox">` | role="checkbox"                            |
| `<input type="radio">`    | role="radio"                               |
| `<input type="text">`     | role="textbox"                             |



## 접근 가능한 설명용 텍스트

### `aria-label`

- 모든 html 태그에 사용 가능
- 이미지를 사용해서 시각적 표현을 할 경우 대체 텍스트를 제공
- 네이티브 텍스트와 같이 사용시, aira-label 속성에 작성된 정보만 스크린 리더에서 출력됨



### `aria-labelledby`

- 모든 html 태그에 사용 가능
- 현재 요소를 설명할 텍스트가 있을 경우 해당 텍스트 영역과 현재 요소를 연결해 사용함
- 숨겨져 있는 요소(display:none, visibility:hidden)도 참조
- 네이티브 텍스트와 aria-label, aria-labelledby가 같이 사용된다면 aria-labelledby의 내용이 최우선됨



출처: https://abcdqbbq.tistory.com/76, https://abcdqbbq.tistory.com/77