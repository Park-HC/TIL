# Composition API

## 성격

- 컴포넌트 재사용 가능 로직을 작성할 수 있도록 도움
  - 2번 이상 반복되는 컴포넌트를 가져와서 재사용 가능
- 함수 기반의 API 작성
  - 타입스크립트 추론 이점 극대화
- 데이터, 로직 목적별로 관심사 분리 가능
  - 분기문, 반복문, 중첩 함수 내에서 사용 가능
  - 컴포넌트 생성 주기에 따라 **최초에 한 번만** 실행

- Optional
  - Vue 2와 같이 DCMW 사용 가능
  - 혹은 setup()으로 표현 가능
  - @vue/composition-api를 통해 Vue 2에서도 사용 가능



## 예시

### 기본

```vue
<template>
	<div>{{message}}</div>
	<button @click="changeMessage">변경</button>
</template>

<script>
import { defineComponent, ref } from 'vue';
    
export default defineComponent({
    setup() {
        // data 속성
        const message = ref('곧 바뀜');
        
        // 메서드
        const changeMessage = () => message.value = "바꼈다"
        
        return { message, changeMessage }
    }
})
</script>
```



### ref

```vue
<!-- vue 2 -->

<script>
export default {
    data() {
        return {
            isModalOpen: false
        }
    },
    methods: {
        openModal() {
            this.isModalOpen = true;
        },
        async submitForm() {
            //await loginUser();
            this.openModal();
        }
    }
}
</script>


<!-- vue 3 -->

<script>
import {ref} from 'vue' <!-- vue2면 @vue/composition-api -->
    
const useModal = () => {
    const isModalOpen = ref(false);
    const openModal = () => isModalOpen.value = true
    
    return { isModalOpen, openModal }
}
    
export default {
    setup() {
        return { ...useModal() }
    },
    methods: {
        async submitForm() {
            //await loginUser();
            this.openModal();
        }
    }
}
</script>
```



### reactive vs ref

```vue
<!-- reactive, 객체를 반환하는 경우 적용 가능 -->

<template>
	<h2>{{ username }}</h2>
	<h2>{{ age }}</h2>
</template>

<script>
import { reacitve, toRefs } from 'vue'
export default {
    name: "TestComponent",
    setup() {
        const state = reactive({
            username: "Scalper",
            age: 50,
        })
        
        return toRefs(state); // state의 value를 보낼 경우 반응성 상실
        					  // toRefs를 쓰면 외부에서 바로 값에 접근 가능
        					  // 동시에 반응성 유지 (Reference)
    }
}
</script>


<!-- ref -->

<template>
	<h2>{{ isNotUgly }}</h2>
</template>

<script>
import { ref } from 'vue'
export default {
    name: "TestComponent",
    setup() {
        let isHnadsome = ref(false); // ref 사용하지 않으면 false가 반환됨
        							 // 자동으로 object형 데이터가 됨
        let isNotUgly = isHandsome;
        isHandsome.value = true;
        
        return isNotUgly
    }
}
</script>


<!-- reactive + ref + function + v-model -->

<template>
	<h2>{{ isHandsome }}</h2>
	<button @click="changeName">change your face!</button>
	<h2>{{ job }}</h2>
	<button @click="changeJob">change your life!</button>

	<div>
        <input type="text" v-model="username">
    </div>
</template>

<script>
import { ref, reactive, toRef } from 'vue'
export default {
    name: "TestComponent",
    setup() {
        let isHnadsome = ref(false); 
        
        function plasticSurgery() {
            isHnadsome.value = true
        };
        
        const state = reactive({
            username: "Scalper",
            age: 50,
            job: "programmer",
        });
        
        function changeJob() {
            state.job = "건물주"
        }
        
        return {
        	isHandsome,
            plasticSurgery,
            ...toRefs(state),
        }
    }
}
</script>
```





## Vue 2에서 사용시 주의 사항

- 기존의 믹스인과 HOC을 이용한 코드 재활용 방식 지양
- 타입스크립트와 같이 사용했을 때 효과 상승
  - 훅에서 정의한 파일을 컴포넌트 안에서 재선언 했을 때 덮어쓰는 실수를 피할 수 있음
- reactive 보다는 ref 지향
- Vue 3의 모든 기능이 지원되는 건 아님