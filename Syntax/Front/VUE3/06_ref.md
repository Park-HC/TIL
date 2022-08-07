# Reactivity

## 반응성

- 데이터가 변경되었을 때 이를 감지하고 이에 반응하여 부가적인 동작을 수행하기 위한 성질
- 화면 갱신 발생!
- Vue는 이런 반응성을 Proxy API로 구현



## Proxy

- 메서드의 기본적인 동작을 가로채서 추가적인 작업을 수행하거나 대체하는 행위
- 현실로 치면 "음식 주문"을 가로채서 "배달"하는 "배달업체"가 Proxy에 해당



### 생성

```javascript
const target = {
    foodA: "김치찌게",
}
const handler = {}

// proxy 생성
const proxy = new Proxy(target, handler);

console.log(`주문: ${target.foodA},`, target);
console.log(`주문: ${proxy.foodA},`, proxy);
```



### Handler와 Trap

- hanlder는 trap들을 가지는 placeholder 객체

- trap은 target 객체의 property에 접근하기 위한 set/get 메서드

  - 이미 정의되어 있음

  - #### GET?

    - 어떤 객체의 속성을 사용하면 property 값이 바로 반환되지 않고 [[Get]] 내부 메서드가 호출됨
    - 값을 변경할 때도 [[Set]] 내부 메서드가 호출됨

- Trap get 메서드 => target [[Get]] 메서드

- `console.log(proxy.foodA)`같이 접근했을 때 get Trap이 호출 -> target의 [[Get]]을 호출

  - 실제 target 메서드 실행 전 끼어들기!

```javascript
// 메서드 구조

// trap get
new Proxy(target, {
    get: function(target, property, receiver) {
}});

// trap set
new Proxy(target, {
    set: function(target, property, value, receiver) {
}});

// target: target 객체 참조
// property: 사용하려는 target 객체의 속성 이름
// value: target 속성에 할당하려는 값
// receiver: proxy 자신 또는 proxy를 상속받을 객체
// return: 속성에 해당하는 Any 값(get)
//		   할당 성공 여부를 나타내는 Boolean 값(set)
```



## Reactive

- Vue의 reactive()는 원본 객체에 대한 Proxy를 제공하여 객체에 대한 반응성을 제공
- 하위의 중첩 속성까지 전파되는 깊은 반응성(`swallowReactive()`를 사용하면 보다 얕은 반응성이 제공됨)
- 객체를 proxy를 통해 접근할 때 반응성이 발생
- 객체의 특정 속성을 일반 변수에 할당하거나 다른 함수의 파라미터로 넘겨주면 반응성 상실함
- 객체 타입(objects, arrays, Maps, Set 등등)에서만 사용 가능
  - 기본형(string, number, boolean 등)에는 사용 불가능



## Ref

>  Vue 2의 `this.$ref`가 Vue 3에서는 각각의 함수로 나뉘어 쓰임

- 객체 타입은 물론 기본형 변수까지 모두 반응성을 제공
- 마운트된 요소에만 적용 가능
- 내부적으로 `value`라는 키 값에 변수의 단일 값 파라미터를 매핑
  - 실제 값에 접근하려면 `[변수명].value`로 한 단계 들어가야 됨
  - template에서 사용(출력, 값 변경 모두)할 때는 `.value`를 붙이지 않음
  - 단, ref()를 요소로 갖는 객체를 사용할 때는 요소의 값을 조작할 때 `.value`를 붙여야 됨



### 연관된 API

#### unref

- 주어진 인자가 ref라면 value 값을, 아니라면 인자 자체를 반환
- `val = isRef(val) ? val.value : val`을 수행하는 편의 함수

#### toRef

- 소스가 되는 reactive의 속성을 가져와 ref를 만듦
- 소스 객체에 대해 reactive한 연결을 유지
- 마운트된 프로퍼티가 아니더라도 사용이 가능해 (toRefs가 작용되지 않는) props를 사용하려할 때 유용

#### toRefs

- reactive 객체를 일반 객체로 변환하여 반환
- 변환된 객체들의 각 속성들이 ref로 원래 reactive 객체의 프로퍼티와 연결됨
- 반응성을 잃지 않고 반환된 값을 destructure / spread 할 수 있기 때문에 컴포지션 함수 등에 유용함

#### isRef

- 주어진 값이 ref 객체인지 확인

#### customRef

- 종속성 추적 및 업데이트 트리거를 명시적으로 커스터마이징 할 수 있는 ref를 만듦
- track 및 trigger 함수를 인수로 받고 get 및 set을 가진 객체를 반환하는 팩토리 함수를 인자로 넘겨야 됨

#### shallowRef

- `.value`가 변경되는 것은 추적하지만 value 값 자체를 반응적으로 만들지는 않는 ref

#### triggerRef

- shallowRef에 연결된 모든 effect를 수동으로 실행

#### readonly

- 반응형 객체를 전달받은 곳에서 반응성만 유지시키고 값의 변경은 막음



##### 참조

- https://jongik.tistory.com/22?category=993238
- https://goodteacher.tistory.com/531

##### 참고

- https://velog.io/@skyepodium/vue-ref-%EC%86%8D%EC%84%B1-feat.-%EC%A3%BC%EC%9D%98%ED%95%A0-%EC%A0%90#4-watch
  - Vue 2의 `this.$ref`를 설명함