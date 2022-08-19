# vue3의 router

## params 사용법

```javascript
import { useRoute } from 'vue-router'

export default {
  setup() {
    const route = useRoute()

    //onMounted(() => {
    //  const id = route.params.id
    //})
    const id = route.params.id
  }
}
```

```javascript
<script setup>
import { useRoute } from 'vue-router';

const route = useRoute();  
const id = route.params.id; // read parameter id (it is reactive) 

</script>
```

