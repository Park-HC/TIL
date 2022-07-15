```
$vue add vuetify
$npm install --save material-design-icons-iconfont

import 'vuetify/dist/vuetify.min.css'
import 'material-design-icons-iconfont/dist/material-design-icons.css'


$npm install vue bootstrap bootstrap-vue-3

import BootstrapVue3 from 'bootstrap-vue-3'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue-3/dist/bootstrap-vue-3.css'
createApp(App).use(router).use(BootstrapVue3).mount('#app')
```



```
vue add vuetify
npm install vuetify@^3.0.0-alpha.11
# new project에서는 성공, skeleton에서는 실패
```



```
npm install element-plus --save
npm install sass
# skeleton에서 성공
```





# Vue framework 비교

## Vuetify

- 아직 Vue 3 버전이 정식 배포되지 않음
  - 배타 버젼 배포 중
  - 안정성 문제인지 skeleton project에 적용하기 어려움
- 버튼
  - https://next.vuetifyjs.com/en/components/buttons/



## Bootstrap-vue-3

- 버튼
  - https://bootstrap-vue.org/docs/components/button



## Element-plus

- 버튼
  - https://element-plus.org/en-US/component/button.html#basic-usage
- Carousel을 보니 예시 코드에 `<style>`을 지정....
- skeleton project의 기본 스타일로 보임
- 한글 자료 거의 없음, 검색 자료 중 절반 정도는 중문
- API 적 성격 강함
  - 개칭 전에는 Element UI로 불렸음
  - 자체적으로 이벤트 핸들링이 있는 듯?



## Quasar

- 버튼
  - https://quasar.dev/vue-components/button
  - 예시가 상당히 많음
- 자체적으로 cli를 제공
  - 처음 프로젝트에 적용하기 힘듦
  - 적용 후에도 이런 저런 문제가 발생



#### 참조

- https://memi.dev/board/community/1631177262211?category=%EC%82%AC%EC%9A%A9%EA%B8%B0
