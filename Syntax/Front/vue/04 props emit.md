# 컴포넌트 구축

## 컴포넌트 등록

1. 불러오기

   `import Name from '@/components/Name.vue`

2. 등록하기

   `compoents:{Name}`

3. 보여주기

   `<name></name>`



## 컴포넌트 간 소통

### 필요성

- 자연스럽게 이루어진 컴포넌트 트리
- 컴포넌트는 부모-자식 관계로 구성되어 이들 사이 소통이 필요함
- 부모는 자식에게 데이터를 Pass props
- 자식은 부모에게 메시지를 Emit event



### Props

- 부모 컴포넌트의 정보를 전달하기 위한 사용자 지정 특성
- 자식 컴포넌트는 props 옵션을 사용
- 수신하는 props를 명시적으로 선언 필요
- 숫자 전달시 v-bind 필요함

#### Static Props 작성법

##### 부모 컴포넌트

`<child-component-name prop-data-name="value"></child>`

##### 자식 컴포넌트

`props: { dataFromParents: String }`

`<p> {{ dataFromParents }} </p>`

#### Dynamic Props 작성법 

- v-bind directive를 사용
- 부모 데이터의 props를 동적으로 바인딩
- 부모 데이터가 업데이트 될 때마다 자식 데이터로 전달 됨

`<name :parent-data="parentData"></name>`

`data: function () { return { parentData : '어찌고' } }`

- 자식데이터에서는 마찬가지로



### Emit event

`$emit(eventName)`

- 현재 인스턴스에서 이벤트를 트리거(v-on)
- 추가 인자는 리스너의 콜백 함수로 전달

#### 자식 컴퍼넌트

`@keyup.enter="childInputChange"`

`childInputChange: function () { this.$emit('child-input-change', 'this.childInputData') }`

#### 부모 컴퍼넌트

`<name @child-input-change="parentGetChange"></name>`



## Vue Router

```
$ vue add router
```

- 라우트(route)에 컴포넌트 매핑 후 어떤 주소에 렌더링 할지 알려줌
- SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능 제공



- `<route-link>`

  - 사용자 네비게이션을 가능하게 하는 컴포넌트

  - 목적 경로는 'to' prop으로 지정됨

  - a 태그지만 기본 GET 요청을 보내는 이벤트가 제거된 형태

- `<route-view>`
  - 주어진 라우트에 대해 일치하는 컴포넌트를 렌더링하는 컴포넌트
- History Mode
  - HTML History API를 사용해서 router를 구현한 것
  - 브라우저의 히스터리는 남기지만 실페 페이지는 이동하지 않는 기능을 지원
  - 즉, 페이지를 다시 로드하지 않고 URL을 탐색할 수 있음
    - SPA 단점인 'URL이 변경되지 않음'을 해결