# Vuex 추가 학습

> 충격! 이제 미래는 Vuex가 아니라 Pinia에 있다고 한다!



## quasar와 vuex

### quasar의 기본 vuex 구조

- `src/store/index.js`와 `src/store/[모듈명]/[state.js, actions.js, mutations.js, getters.js, index.js]`로 구성
- 모듈 별로 파일을 만드는 것이 아니라 폴더를 만들고 state, actions, mutations, getters 등을 관리할 파일을 하나씩 만듦
- 모듈 별로 기능들을 수합할 index.js를 하나 씩 가지고, store 바로 아래에는 모듈멸 index.js를 다시 수합하는 index.js가 있음



### 모듈 생성

```bash
$ quasar new store <store_name> [--format ts]
```

- 이후 `store/index.js`에 새 모듈 명을 추가함
- 기능을 추가할 대는 state를 제외하고는 파일 내에 바로 함수를 정의함



### 컴포넌트에서 속성 불러오는 법

```javascript
import { useStore } from 'vuex'

export default {
    setup () {
        const $store = useSotre()
        
        // state
        $store.state.모듈명.state 명

        // mutations
        $store.commit('모듈명/mutations 명' [, '전달인자'])

        // actions
        $store.dispatch('모듈명/actions 명' [, '전달인자'])

        // getters
        $store.getters['모듈명/getters 명']
    }
}

```



## vuex에 대한 팁들

### 다른 모듈에 접근하는 방법

#### rootState

- 기본적으로 state 변수 값은 돌일 모듈에 있는 state만 참조
- 최상위에 있는 state 변수나 다른 모듈의 변수 값을 활용하기 위해서는 **rootState**를 활용해야 함
- rootState는 actions와 getters의 인자로만 사용 가능
- mutations에서 사용하고 싶다면 actions에서 바다 mutations 쪽으로 commit해야 함



#### Mutations, Actions

- 세번째 인자에 `{ root: true }` 지정
- 최상위 경로인 root에서부터 하위 경로를 찾아 들어갈 수 있음
- `dispatch("path1/actionsA)", payload, { root: true});`
- `commit("path1/mutationsA)", payload, { root: true});`



### 데이터 처리 상관 관계

```
각 컴포넌트 (dispatch) => actions (commit) => mutations (state) => state => 모든 컴포넌트에서 활용
```



### 사용가능 인자

#### Mutations

- mutations 내 함수 인자는 `state`와 `payload`
- 기본 인자는 state
- 전달 인자는 payload
- payload는 여러 변수를 묶은 객체 형태로 전달 가능

#### Actions

- 기본 인자는 {rootState, state, dispatch, commit}
- 기본 인자는 중괄호로 묶어서 전달 받음
- 전달 인자는 payload



## Pinia의 특이점

1. mutations가 없다
2. Vue3처럼 Store를 선언할 수 있게 한다
3. `computed`를 구조분해 할당으로 처리할 수 있다
4. Typescript를 지원한다
5. autocompletion을 지원한다
6. namespaced modules가 없어도 된다
7. devtools를 공식 지원한다
8. Vuex 5의 구현체로 작성되었으며, 추후 Vuex 5와 합쳐지거나 쉽게 혼용될 수 있도록 지원될 예정이다





