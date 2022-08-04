# Life Cycle

## Life Cycle Hook

- composition api에서는 setup hook에서 beforeCreate, created에 해당하는 과정이 한꺼번에 처리됨
  - setup()가 바로 setup hook
- 각각 hook은 setup() 내부에서 접근 가능

| 라이프 사이클 훅 | Setup 내부 호출 | 설명                                                         |
| ---------------- | --------------- | ------------------------------------------------------------ |
| beforeCreate     | X               | Vue 객체가 생성되고 데이터에 대한 관찰 기능 및 이벤트 감시자 설정 전에 호출 |
| created          | X               | Vue 객체가 생성된 후 데이터에 대한 관찰 기능, computed, methods, watch 설정이 완료된 후 호출 |
| beforeMount      | onBeforeMount   | Component가 reactive state에 대한 설정을 끝낸 후, 마운트가 시작되기 전에 호출 |
| mounted          | onMounted       | Component의 mount가 된 후 호출<br />모든 자식 component들도 mount 완료 상태<br />DOM 트리가 완성되어 부모 container에 삽입 완료된 상태<br />DOM과 관련된 부가 수행 가능 |
| beforeUpdate     | onBeforeUpdate  | 가상 DOM이 렌더링, 패치되기 전에 데이터가 변경될 때 호출<br />이 단계에서 추가적인 상태 변경을 수행할 수 있지만 다시 렌더링 되지는 않음 |
| updated          | onUpdated       | 데이터 변경으로 가상 DOM이 다시 렌더링 되고 패치된 후 호출<br />컴포넌트 DOM이 업데이트 된 상태이므로 DOM에 종속적인 작업 가능 |
| beforeUnmount    | onBeforeUnmount | Vue 객체가 제거되기 전에 호출                                |
| unmounted        | onUnmounted     | Component가 unmount 된 후에 호출<br />모든 자식 component들도 unmount 됨<br />setup 과정에서 생성된 반응성 효과(computed, watcher 등) 중지<br />사용자 정의로 작성했던 timer 등에 중지 |



