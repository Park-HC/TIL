# 자바스크립트의 정체

## 인터프리터

- 개발자 도구 콘솔에서 스크립트를 작성해 실행하는데 컴파일이 필요하지 않으므로 인터프리터 언어
- 다만 자바스크립트 엔진 속에서 컴파일을 진행하기도 함
  - 반복해서 실행되는 코드 블록을 컴파일하고 최적화된 코드를 원래 코드와 바꿔줌
  - 인터프리터를 실행하고 필요할 때 컴파일하는 방법을 **JIT** 컴파일러라고 부름
  - 크롬의 V8엔진, Mozilla의 Rhino, Firefox의 SpiderMonkey가 이 방식을 사용



## 싱글쓰레드

> **JavaScript** is a single-threaded, non-blocking, asynchronous, and concurrent language.

- 싱글 쓰레드, 논 블록킹, 비동기적 언어
- 싱글 쓰레드
  - 한 번에 하나의 작업만 함
- 논 블로킹, 비동기적
  - 순차적으로 코드를 처리하지 않고, 특정 입력 등이 발생할 때 필요한 코드를 처리함
  - 자바 스크립트가 싱글쓰레드이면서 멀티쓰레드처럼 보이는 이유

### setTimeout 예시

1. setTimeout이 호출되면 처리 과정을 WebAPIs에 위임
2. WebAPIs에서 이를 처리하고 모두 종료되면 Callback Queue에 콜백함수를 밀어 넣음
3. Event Loop에서 Call Stack을 주시하다가 처리할 수 있을 때 Callback Queue에 대기중인 콜백함수를 Callback Stack으로 밀어 넣음
4. CallStack은 전달받은 콜백 함수를 실행함



