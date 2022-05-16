# Vuex

## 개요

- 상태 관리 패턴 + 라이브러리
- 상태를 전역 저장소로 관리할 수 있도록 지원하는 라이브러리
  - 애플리케이션의 모든 컴포넌트에 대한 중앙 집중식 저장소 역할
- Vue의 공식 devtools와 통합되어 기타 고급 기능을 제공



### 상태관리 패턴

- 컴포넌트의 공유된 상태 추출
- 전역에서 공유된 상태를 관리하도록 함
- 컴포넌트는 커다란 View가 되어 모든 컴포넌트는 트리에 상관 없이 State에 엑세스 하거나 동작을 트리거할 수 있음
- 코드의 구조와 유지 관리 기능 향상
- props, emit는 직관적이지만 트리가 크고 복잡해질수록 데이터 전달이 불편해짐
  - 상태를 공유하는 모든 컴포넌트들이 pass props & emit event를 통해 동기화되어야 함



## 핵심 컨셉

### state

- 중앙에서 관리하는 모든 상태 정보
- 모든 애플리케이션 상태를 포함하는 원본 소스의 역할
- 각 애플리케이션 마다 하나의 저장소만 갖게 됨



### mutations

- state를 변경하는 유일한 방법
- 동기적인 handler 함수만 지원
  - 비동기적 로직(콜백 함수 등)은 state가 변화하는 시점이 의도한 것과 달라질 수 있고
  - 콜백이 실제로 호출 될 시기를 알 수 없음(추적할 수 없음)

- 첫번째 인자는 무조건 state
- actions에서 commit() 메서드로 호출됨



### actions

- mutations을 호출하며, 비동기 작업이 포함 될 수 있음
- context 객체 인자를 받음
  - store/index.js 파일 내 모든 요소의 속성과 메서드에 접근 가능
  - 가능은 하지만, state를 직접 변경하지 않음
    - 명확한 역할 분담이 있어야 서비스 규모가 커져도 state를 관리하기 쉬움
- 컴포넌트에서 dispatch() 메서드로 호출됨



### getters

- state를 변경하지 않고 계산을 수행
- state 종속성에 따라 캐시(저장)되고 종속성이 변경된 경우에만 다시 계산 됨



## Component Binding Helper

- js Array helper Method를 통해 배열 조작을 편하게 하는 것과 유사
- 코드 자체가 변하는 것이 아니라 '쉽게' 사용할 수 있도록 되어 있음에 초점

### mapState

- computed와 Store의 state 매핑
- 매핑된 computed 이름이 state 이름과 같을 때 문자열 배열을 전달 할 수 있음

### mapGetters

- Computed와 Getters를 매핑
- getters를 객체 전개 연산자(Object Spread Operator)로 계산하여 추가

### mapActions

- action을 전달하는 컴포넌트 method 옵션을 만듦
- actions를 객체 전개 연산자로 계산하여 추가하기



## Local Sorage

```
$ npm i vuex-persistedstate
```

- Vuex state를 자동으로 브라우저의 Local Storage에 저장해주는 라이브러리 중 하나
- 페이지가 새로고침 되어도 Vuex state를 유지시킴