# Watch

## 개요

- computed와 유사하게 data 변경시 동작하는 속성
- 값을 처리할 수 있지만 부가 동작 처리에 더 많이 이용
- computed는 template에 사용되야 동작하지만
  - watch는 template에 사용되지 않음!
- 특정한 값을 지켜보다가 변경되면 어떤 일을 처리함
- computed는 주로 동기로 값을 리턴
  - watch는 비동기로 처리되 값을 리턴하지 않음



## 사용법

```vue
Vue.watch(source, callback, option);
```

- source
  - 감시할 대상의 이름(변수 명)
  - 감시 대상은 ref 및 reactive 객체나 getter function 혹은 이들로 구성된 배열
- callback
  - 값이 변경되었을 때 동작을 수행할 callback 함수
  - 콜백 함수의 파라미터로 새로운 값과 기존 값이 전달됨
    - 만약 객체를 감시한다면 두 값이 동일함
- option
  - watch를 위한 부가적인 option들로 이뤄진 객체
  - `immediate`
    - watcher가 처음 생성될 때도 동작할 것인가를 설정
    - 초기의 old value는 undefined
    - default는 false
  - `deep`
    - 감시 대상이 객체인 경우 객체의 property가 변경되는 것까지 감시할 것인지 설정
    - 반응형 객체에 대한 감시인 경우 default가 true
    - getter function을 통한 감시인 경우 default가 false



## computed와 비교 예시

```javascript
<script>
	const { createApp, ref, watch, computed } = Vue;

	createApp({
        setup() {
            const num = ref(4);
            
            // computed: 값이 변경되면 계산 후 반환
            const squareC = computed(() => {
                return num.value * num.value
            })
            
            const squareW = ref(0);
            
            watch(
            	num, // 감시 대상
                (nv, ov) => {
                    console.log(`num 변경: ${ov} => ${nv}`);
                    squareW.value = nv * nv; // side effect로 처리(반환 X)
                }.
                { immediate: true } // 옵션 객체, num 생성 후 즉시 실행됨
                };
              
              return { num, squareC, squareW };
            )
        },
    }).mount("#app");
</script>
```

- 결과적으로는 squareC와 squareW가 동일하지만 동작은 다름



## deep 설정

```javascript
const obj = reactive({ user: { name: "홍길동" }});
const message = ref("");

watch(
	//obj.user,
    () => obj.user, // 이 경우는 얕은 감시만 진행
    (nv, ov) => {
        message.value = `정보 변경 기존: 신규: ${nv.name}, ${nv.age}, ${nv == ov}`;
    },
    { deep: true }  // 깊은 감시를 위해서 deep 속성 추가
);
```



## 비동기 처리

```javascript
const question = ref("");
const answer = ref("한방에 결정해주지!!");

watch(question, async (newQ, oldQ) => {
    answer.value = "그건 말이지....";
    try {
        const res = await fetch("https://yesno.wtf/api");
        answer.value = (await res.json()).answer;
    } catch (error) {
        answer.value = "network error: " + error;
    }
});

return { answer, question };
})
```





> 참조: https://goodteacher.tistory.com/542