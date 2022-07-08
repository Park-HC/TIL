# 에러 및 예외 처리

## 디버깅

### 방법

1. print 함수 활용
   - 코드를 bisection으로 나눠서 생각
2. IDE 등 개발 환경에서 제공하는 기능 활용
   - breakpoint, 변수 조회 등
3. Python tutor 활용
   - 단순 파이썬 코드일 경우
4. 뇌컴파일, 눈디버깅



### 로직 에러

#### branches

- 이 코딩이 모든 조건(극단적인 조건까지) 포괄하는가?

#### for loops

- 반복문에 진입하는지
- 반복문이 원하는 횟수만큼 실행되는지
- 반복문 값 - 진입 값과 결과 값이 내가 원한 바와 같은가?

#### while loops

- 반복문에 진입하는지
- 반복문이 원하는 횟수만큼 실행되는지
- 반복문 값 - 진입 값과 결과 값이 내가 원한 바와 같은가?
- 종료 조건이 제대로 설정했는지

#### function/method

- 함수의 호출이 제대로 되었는지
- 파라미터와 결과 값이 제대로 설정되었는지
- type 처리가 제대로 되었는지



### 해결방법

- 에러가 발생한 위치 찾아 해결
- 다른 결과가 나왔다면...
  - 정상적으로 동작하였던 코드 이후 작성된 코드를 되짚어봄
  - 전체 코드를 살펴봄
  - 잠깐 쉬었다 오기
  - 누군가에게 설명해 봄..



## 에러와 예외

### 문법 에러(Syntax Error)

#### 정의

- 파이썬이 코드를 읽어 나갈 때(parser) 문제가 발생한 위치를 표현
- 에러가 감지된 가장 앞 위치를 가리키는 캐럿 기호(^) 표시

#### 종류

- Invalid syntax
- assign to literal
- EOL(End of Line)
- EOF(End of File)



### 예외

#### 정의

- 실행 도중 예상치 못한 상황을 맞이하면 프로그램을 멈춤
- 문법적으로 올바르더라도 발생하는 에러

#### 예외

- ZeroDivisoinError

  - 숫자형 자료를 0으로 나눌 경우 발생

- NameError

  - namespace에 이름이 없는 객체를 호출할 경우

- TypeError

  - 함수 인자의 타입이 함수에서 요구하는 것과 일치하지 않을 경우
  - 함수 인자의 개수가 함수에서 요구하는 것에 못 미치거나 더 많을 경우

  ```python
  1 + '1'
  round('3.5')
  # 타입 불일치
  
  divmod()
  divmod(1, 2, 3)
  sorted(1)
  # argument를 잘못 넣음
  ```

- ValueError

  - 타입은 올바르지만 값이 올바르지 않거나 없는 경우

  ```python
  int('3.5')
  range(3).index(6)
  # 타입은 올바르나 값이 적절하지 않거나 없는 경우
  ```

- IndexError

  - List에서 존재하지 않거나 범위를 벗어난 인덱스를 호출했을 경우

- KeyError

  - Dictionary에서 존재하지 않는 키를 호출했을 경우

- MoudleNotFoundError

  - 존재하지 않는 Module을 import 했을 경우

- ImportError

  - Moudle은 있으나 그 Module에서 존재하지 않는 클래스/함수 등을 가져오려고 했을 경우

- KeyboardInterrupt

  - 임의로 프로그램을 종료했을 경우

- IndentationError

  - Indentation(코드 블록)이 적절하지 않는 경우




## 예외 처리

```python
try:
    try 명령문
except 예외그룹-1 as 변수-1 :
    예외처리 명령문 1
except 예외그룹-2 as 변수-2 :
    예외처리 명령문 2
finally:
    finally 명령문
```

```python
try:
    num = input('숫자입력 : ')
    print(int(num))
except ValueError:
    print('숫자가 입력되지 않았습니다.')
```

- try

  - 코드 실행

- except

  - try 문에서 예외 발생 시 실행
  - as <변수>
    - 원본 에러 메시지를 변수에 넣음

- else

  - try 문에서 예외 발생하지 않으면 실행

- finally

  - 예외 발생 여부와 관계없이 항상 실행

  

## 예외 발생 시키기

- raise

  ```python
  raise <에러타입> (메시지)
  ```

  - 예외를 강제로 발생

- assert

  ```python
  assert <표현식>, <메시지>
  ```

  - 예외를 강제로 방생
  - 표현식이 False인 경우 Assertion Error가 발생
  - 디버깅 용도