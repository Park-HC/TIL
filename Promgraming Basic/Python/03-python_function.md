# Function

> E = mc^2
>
> Error = morecode^2

## 기초

### 정의

- 특정한 기능을 하는 코드의 조각(묶음)
- 특정 명령을 수행하는 코드를 매번 다시 작성하지 않고, 필요 시에만 호출하여 간편히 사용



### 기능

- Abstraction(추상화)

  - 복잡한 내용을 모르더라도 사용할 수 있도록(블랙박스) 

  - 재사용성, 가독성, 생산성

- 코드 중복 방지

- 재사용 용이



### 사용자 함수(Custom Function)

- 구현되어 있는 함수(내장 함수)가 없어, 사용자가 직접 구현한 함수



### 기본 구조

#### 선언과 호출

- def 키워드를 활용함
- 들여쓰기를 통해 Function body(실행 코드 블록) 작성
- 함수는 parameter를 통해 넘겨줄 수 있음
- 동작후 return을 통해 결과값 출력

```python
def foo():
    return True

def add(x, y):
    return x + y
# --------------
f1 = lambda x: x ** 2 
# 한 줄일 때만 사용 가능한 표현 방식
```



#### 입력

- Parameter
  - 함수를 실행할 때, 함수 내부에서 사용되는 식별자
- Argument
  - 함수를 호출할 때, 넣어주는 값

- Keyword Argument(호출)

  - 직접 변수의 이름으로 Argument를 전달하는 방식

  ```python
  def add(x, y):
      return x + y
  
  print(add(1, 2))  # 위치 - 내부에서 바인딩
  print(add(y=2, x=1))  # 키워드
  print(add(x=1, 2))  # Syntaxerror: positionial argument follows keyword argument
  # 키워드로 지정하는 순간 위치가 이미 의미가 없어짐
  print(add(1, y=2))  # 동작됨
  ```



- Default Arguments Values(정의)

  - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
  - 정의된 것 보다 더 적은 개수의 argument들로 호출 될 수 있음

  ```python
  def add(x, y=0):
      return x + y
  
  add(2)
  # 2 + 0 = 2
  
  def greeting(me = 'I am', you):
      pass
  # 오류!
  ```

  ```python
  def greeting(age, name):
      return f'{name}은 {age}살입니다.'
  
  greeting(name='철수', age=24)
  # '철수은 24살입니다.'
  
  greeting(24, name='철수')
  # '철수은 24살입니다.'
  
  greeting(age=24, '철수')
  # SyntaxError: positional argument follows keyword argument
  
  greeting('철수', age = 24)
  # TypeError: greeting() got multiple values for argument 'age'
  ```

  



- Positional Argument Packing/Unpacking

  - 여러 개의 positional Argument를 하나의 필수 parameter로 받아서 사용

  ```python
  def add(*args):
      for arg in args:
          print(arg)
          
  add(2, 3, 4, 5)
  ```

  ```python
  def xprint(*asdf, e1='\n'):
      print(asdf)
      return
  
  xprint(1,2,3,4,5)
  # (1,2,3,4,5)
  xprint()
  # ()
  ```

  

- Keyword Arguments Packing/Unpacking

  - 함수가 임의의 개수 Argument를 Keyword Argument로 호출 될 수 있도록 지정
  - Argumnet들은 딕셔너리로 묶여 처리되며, paramenter에 **를 붙여 표현

  ```python
  def family(**kwargs):
      for key, value in kwargs:
          print(key, ":", value)
  family(father='John', mother='Susy', son='Micheal')
  ```

  

#### 문서화

##### Docstring(Document String)

- 함수나 클래스 설명

##### Naming Convention

> 좋은 함수와 parameter 이름을 짓는 방법

- 상수 이름은 영문 전체를 대문자
- 클래스 및 예외의 이름은 각 단어의 첫 글자만 영어 대문자
- 이외 나머지는 소문자 내지 밑줄로 구분한 소무자 사용(snake)
- 스스로를 설명
  - 함수의 이름만으로 어떠한 역할을 하는 함수인지 드러내기
  - 어떤 기능을 수행하는지, 결과 값으로 무엇을 반환하는지 등
- 약어 사용을 지양
  - 보편적으로 사용하는 약어만 제외



#### 범위

##### Local scope & Global scope

```python
def ham():
    a = 'spam'
    return a
    
ham()
print(a)
# NameError: name 'a' is not defined

-------------------------

n = 0

def func():
    n = n+1
    
func()
# UnboundLocalError: local variable 'n' referenced before assignment

---------------------------

n = 0

def func():
    print(n+1)
    
func()
# 1
```

```python
def list_sum_1(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

list_sum_1([1,2,3,4,5])
# return 있음, 다양한 상황에 사용 가능
---------------------------------
total = 0

def list_sum_2(numbers):
    global total
    for num in numbers:
        total += num
        
list_sum_2([1,2,3,4,5])
# return 없음, 특정한 상황에서만 사용 가능(사용을 위해 total 선언 및 재사용 필요)
```



- local에서 global 변수에 재할당할 수는 없지만, 수정할 수는 있음!

  ```python
  a = [3, 2, 1]
  
  def func():
      a.sort()
      a.append(4)
  
  func()
  print(a)
  # [1, 2, 3, 4]
  ```

  

##### 변수 수명주기(lifecycle)

- 변수는 각자의 수명주기가 있음

1. built-in scope
   - 파이썬이 실행된 이후부터 영원히 유지

2. global scope
   - 모듈이 호출된 시점 이후 혹은 인터프리터가 끝날 때까지 유지

3. local scope
   - 함수가 호출될 때 생성되고, 함수가 종료될 때까지 유지

##### 이름 검색 규칙(Name Resolution)

- 파이썬에서 사용되는 이름들은 이름공간(namespace)에 저장되어 있음
- LEGB 규칙
  1. Local scope: 함수
  2. Enclosed scope: 특정 함수의 상의 함수
  3. Global scope: 함수 밖의 변수, Import 모듈
  4. Built-in scope: 파이썬 안에 내장되어 있는 함수 또는 속성
- 함수 내에서 바깥 Scope 변수에 접근 가능하나 수정은 할 수 없음
  - global, nonlocal을 쓰면 수정 가능
    - 블랙박스 원칙 위반!
    - 함부로 쓰면 추적이 어렵고 예기치 않은 오류가 생길 수 있으므로 가능한 지양

```python
a = 0
b = 1
def enclose():
    a = 10
    c = 3
    def local(c):
        print(a, b, c)
        # 10 1 300
    local(300)
    print(a, b, c)
    # 10 1 3
enclose()
print(a, b)
# 0 1
# ------------------
a = 10
def func1():
    global a
    a = 3:
funcl()
print(a)
# 3
# ------------------
a = 10
def func1():
    print(a)
    global a
    a = 3:
funcl()
print(a)
# Error
# ------------------
x = 0
def func1():
    x = 1
    def func2():
        nonlocal x
        x = 2
    func2()
    print(x)
func1()
print(x)
# 2
# 0
```



#### 결과값

- Void function
  - 명시적인 return 값이 없는 경우, None을 반환하고 종료
- Value returning function



## 응용

### 내장함수(Bulit-in Functions)

### map

```python
map(function, iterable)
```

- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용,
- 그 결과를 map object로 반환

> ~ object는 원소를 꺼낼 때 원소를 만듦



### Filter

```python
filter(function, iterable)
```

- 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function) 적용,

- 그 결과가 True인 것들을 filter object로 반환



### Zip

```python
zip(*iterable)
```

- 복수의 iterable을 모아 듀플을 원소로하는 zip object 반환



### Lamda

```python
lambda [parameter] : <expression>
```

- 표현식을 계산한 결과값을 반환하는 함수
- return문을 가질 수 없음
- 간편 조건문 외 조건문이나 반복문을 가질 수 없음
- 함수 정의보다 간결하게 사용 가능
- def 사용할 수 없는 곳에서도 사용 가능

```python
def odd(n):
    return n % 2

print(list(filter(odd, range(5))))
print(list(filter(lambda n : n % 2, range(5))))
```



### 재귀함수(recursive function)

-  자기 자신을 호출하는 함수
- 무한한 호출이 목표가 아니며, 알고리즘 설계 및 구성에 유용히 쓰임
- 알고리즘 중 재귀 함수로 로직을 표현하기 쉬운 경우가 있음
- 변수의 사용이 줄어듦
- 코드의 가독성이 높아짐
- 1개 이상의 base case(종료되는 상황)이 존재, 수렴

```python
def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)
```

#### 주의사항

- base case가 없거나 도달할 수 없다면 계속 함수가 호출됨
- 메모리 스택이 넘치게 되면(stack overflow) 프로그램이 중지됨
- 파이썬의 최대 재귀 깊이(maximum recursion depth)가 1000번으로, 호출 횟수가 이를 넘어가면 Recursion Error 발생

```python
def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)
```

#### 반복문 vs 재귀함수

- 알고리즘 자체가 재귀적인 표현이 자연스러운 경우

- 재귀함수는 변수 사용이 줄어듦

- 재귀함수는 함수 호출/사용이 늘어남

- 입력 값이 커질수록 연산량이 많아짐

  ```python
  def fib(n):
      if n < 2:
          return n
      return fib(n-1) + fib(n-2)
  
  fib(35)
  # 수초가 걸림
  
  ----------------------------------------
  
  def fib_loop(n):
      fibos = []
      
      for i in range(n+1):
          if i < 2:
              fibos.append(i)
          else:
              fibos.append(fibos[i - 1] + fibos[i - 2])
      
      return fibos[-1]
  
  fib_loop(35)
  # 거의 즉시 출력
  ```

  