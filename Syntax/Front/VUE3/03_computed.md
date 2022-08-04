# Computed

## 개요

- module의 데이터를 template에서 변형하여 사용할 때 사용
- Vue가 가지는 함수형 속성
- computed의 파라미터는 로직을 가지고 값을 계산한 후 리턴하는 함수
- computed의 반환값은 파라미터 함수가 반환하는 값을 가지는 Proxy 객체의 일종
  - 그래서 연결되는 data가 변경되면 자동으로 새로운 값을 계산하고 화면에 반영

- 변수의 이름은 일반적인 data 이름처럼 사용됨



## filter 역할

- Vue 2에서 존재하던 filter가 Vue 3에서 사라졌지만 computed로 유사하게 사용 가능

```vue
const price = 1000000;

const pretty = computed(() => {
	const option = { style: "currency", currency: "KRW" };
	return new Intl.NumberFormat("ko-KR", option).format(price);
})
```



## Caching

- 종속 대상이 변경되지 않으면 다시 계산하지 않음





> 참조 https://goodteacher.tistory.com/541?category=983324