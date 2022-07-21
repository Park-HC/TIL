## quasar에서 vuex 속성 불러오는 법

$store.dispatch('모듈명/acitions 명')

$store.getters['모듈명/getters 명']

$store.commit('모듈명/mutations 명')

$store.state.모듈명.state 명



## vue3 ref 변수 수정하는 법

변수 = ref(값)

const 함수 = () => {

​	**변수.value** = 새값

​	// 'this' 필요 없음

}

