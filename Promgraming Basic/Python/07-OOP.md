# 객체재향 프로그래밍

> 파이썬은 모두 객체로 이뤄져 있다.

## 정의

- 프로그램을 여러개의 독립된 객체들과 그 객체들 간의 상호작용으로 파악하는 프로그램밍 방법



### 객체(Object)

> 객체는 특정 타입의 인스턴스이다.

- 타입(type: 어떤 연산자(operator)와 조작(method)이 가능한가?
- 속성(attribute): 어떤 상태(데이터)를 가지는가?
- 조작법(method): 어떤 행위(함수)를 할 수 있는가?



### 특성

- 컴퓨터 프로그래밍의 패러다임
- 객체 지향 프로그래밍은 컴퓨터 프로그래밍을 명령어의 목록으로 보는 시각에서 벗어남
- '객체'라는 여러개의 독립된 단위들의 모임으로 파악함
- 각 객체는 메시지와 데이터를 주고 받음



### 절차지향 프로그래밍

- 절차지향 프로그래밍은 데이터와 함수로 인해 변함
- 객체지향 프로그래밍은 데이터와 기능(메소드)를 분리한 추상화된 구조(인터페이스)

```python
sorted(a) vs a.sort()
```



### 장점

- 프로그램을 유연하고 변경이 용이하게 만들기에 대규모 소프트웨어 개발에 많이 사용
- 프로그래밍 학습이 쉬움
- 소프트웨어 개발과 보수 편함
- 직관적인 코드 분석 가능



## 기초

### 용어

- 클래스: 객체들의 분류(class)
- 인스턴스: 하나하나의 실체/예(instance)
- 속성: 특정 데이터 타입/클래스의 객체들이 가지게 될 상태/데이터를 의미
- 메소드: 특정 데이터 타입/클래스의 객체에 공통적으로 적용 가능한 행위(함수)



### 기본 문법

```python
# 클래스 정의
class MyClass:

# 인스턴스 생성
my_istance = MyClass()

# 메소드 호출
my_instance.my_method()

# 속성
my_instance.my_attribute
```



### 객체 비교하기

- ==
  - 동등한(equal)
  - 변수가 참조하는 객체가 동등한(내용이 같은) 경우 True
  - 두 객체가 같아보이지만 실제로 동일한 대상을 가리키고 있다고 확인해 준 것은 아님
- is
  - 동일한(identical)
  - 두 변수가 동일한 객체를 가리키는 경우



### 인스턴스

#### 인스턴스 변수

- 인스턴스가 개읹적으로 가지고 있는 속성
- 각 인스턴스들의 고유한 변수
- 생성자 메소드에서 self.<name>으로 정의
- 인스턴스가 생성된 이후 <instance>.<name>으로 접근 및 할당



#### 인스턴스 메소드

- 인스턴스 변수를 사용하거나, 인스턴스 변수에 값을 설정하는 메소드
- 클래스 내부에 정의되는 메소드의 기본
- 호출 시, 첫번째 인자로 인스턴스 자기자신이 전달됨



#### self

- 인스턴스 자기자신
- 파이썬이 인스턴스 메소드 호출 시 첫번째 인자로 인스턴스 자신이 전달되게 설계
- 매개변수 이름으로 self를 첫번째 인자로 정의
- 다른 단어로 써도 작동하지만, 파이썬의 암묵적인 규칙

```python
class Rectangle:
    def area(self):  # self 인자가 없으면 class 변수 조작할 수 없음
        return self.x * self.y
```



#### 생성자(constructor) 메소드

- 인스턴스 객체가 생성될 때 자동으로 호출되는 메소드
- 인스턴스 변수들의 초깃값을 설정
  - 인스턴스 생성
  - `__init__` 메소드 자동 호출

```python
class Person:
    def __init__(self, name, age):
        #인스턴스 변수를 정의하기 위해 사용!
        self.name = name
        self.age = age
        
p1 = Person()
# TypeError, 인자 수 부족!
```

```python
class Person:
    def __init__(self, name, age = 1):
        #인스턴스 변수를 정의하기 위해 사용!
        self.name = name
        self.age = age
        print('응애')
        
p1 = Person('지혜')
# 응애
print(p1.naem, p1.age)
# 지혜 1
```



#### 소멸자(destructor) 메소드

- 인스턴스 객체가 소멸되기 직전에 호출되는 메소드

```python
class Person:
    ...
    def __del__(self):
        print('으억')
...
del p1
# 으억
```



#### 매직 메소드

- Double underscore(__)가 있는 메소드
- 특수한 동작을 위해 만들어진 메소드
- 특정 상황에 자동으로 불러와지는 메소드
- 객체의 특수 조작 행위를 지정(함수, 연산자 등)
  - `__str__`: 해당 객체의 출력 형태를 지정
    - 프린트 함수 호출시, 자동으로 호출
    - 어떤 인스턴스를 출력하면 `__str__`의 return 값이 출력
  - `__repr__`: 해당 객체 자체를 호출할 때 출력 형태
  - `__gt__`: 부등호 연산자(>, greater than)
  - `__ eq__`: 등호 연산자(==, equal)
  - `__doc__`: 클래스의 "docstring"(클래스 내부의 주석)를 출력



### 클래스

#### 클래스 변수

- 한 클래스의 모든 인스턴스가 공유하는 똑같은 값 속성
- 클래스 이름 대신 인스턴스 이름을 쓰면 인스턴스 변수임

##### 클래스 속성(attribute)

- 한 클래스의 모든 인스턴스라도 똑같은 값을 가지고 있는 속성
- 클래스 선언 내부에서 정의

```python
class Circle:
    pi = 3.14
cl = Circle()
print(Circle.pi)  # 3.14
print(cl.pi)  # 3.14
```



#### 클래스 메소드

- 클래스가 사용할 메소드
- @classmethod 데코레이터를 사용하여 정의
  - 데코레이터: 함수를 어떤 함수로 꾸며서 새로운 기능을 부여
- 호출 시, 첫번째 인자로 클래스(cls)가 전달됨

```python
class MyClass:
    
    @classmethod
    def class_method(cls, arg1, ...):
My.class_method(...)
```

```python
@classmethod
def class_method(cls):
    return cls

MyClass.class_method() is MyClass
# True
mc.class_method() is mc
# False
```





#### 스태틱 메소드

```python
@staticmethod
def static_method(arg):
    return arg
"""..."""

MyClass.static_method()
# static_method() missing 1 required positional argument: 'arg'

MyClass.static_method(MyClass) is MyClass
# True
```



- 인스턴스 변수, 클래스 변수를 전혀 다루지 않는 메소드

- 속성을 다루지 않고 단지 기능(행동)만을 하는 메소드를 정의할 때 사용
- 클래스가 사용할 메소드
- @staticmethod 데코레이터를 사용하여 정의
- 호출 시, 어떠한 인자도 전달되지 않음(클래스 정보에 접근/서정 불가)



## 개념

### 추상화

- 언어적 설계를 기반으로 프로그램을 설계함
- 세부적인 내용은 감추고 필수적인 부분만 표현하는 것
- 여러 클래스가 공통적으로 사용할 속성 및 메서드를 추출하여 기본 클래스로 작성



### 상속

- 두 클래스 사이 부모 - 자식 관계를 정립하는 것
- 모든 파이썬 클래스는 object를 상속 받음
- 하위 클래스는 상위 클래스에 정의된 속성, 행동, 관계 및 제약 조건을 모두 상속 받음
- super()를 통해 부모 클래스의 요소를 호출할 수 있음
- 메소드 오버라이딩을 통해 자식 클래스에서 재정의 가능함
- 코드 재사용성 높아짐

```python
isinstance(object, classinfo)
# classinfo의 instance거나 subclass인 경우 True

issubclass(class, classinfo)
# class가 classinfo의 subclass면 True
# classinfo는 클래스 객체의 튜플일 수 있으며, classinfo의 모든 항목을 검사

super()
# 자식클래스에서 부모클래스를 사용하고 싶은 경우
```

```python
p1 = Person('s')
dir(p1)

['__class__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',]

# 모든 클래스는 object의 자식 클래스이며, 고로 그 메소드를 상속 받고 있다.
```



#### 다중 상속

- 두 개 이상의 클래스를 상속 받는 경우
- 상속 받은 모든 요소를 활용 가능함
- 중복된 속성이나 메서드가 있는 경우 상속 순서에 의해 결정됨
  - 먼저 상속 받은 클래스가 우선됨



#### mro 메소드(Mehtod Resolution Order)

- 해당 인스턴스의 클래스가 어떤 부모 클래스를 가지는지 확인한느 메소드
- 기존 인스턴스 -> 클래스 순
  - 인스턴스 -> 자식 클래스 -> 부모 클래스 순



### 다형성

- 동일한 메소드가 클래스에 따라서 다르게 행동할 수 있음
  - 서로 다른 클래스에 속해있는 객체들이 동일한 메시지에 대해 다른 방식으로 응답될 수 있음

#### 메소드 오버라이딩

- 상속 받은 메소드를 재정의
- 부모 클래스에서 정의한 메소드를 자식 클래스에서 변경
- 같은 이름의 메소드로 자식 클래스에서 덮어씀
- 부모 클래스 메소드를 실행시키고 싶을 경우 super활용



### 캡슐화

- 객체의 일부 구현 내용에 대해 외부로부터 직접 엑세스 하는 것을 차단

- 파이썬에서 암묵적으로 존재하지만, 언어적으로는 존재하지 않음

- 접근 제어자
  - Public Access Modifier
  - Protected Access Modifier
  - Private Access Modifier
  
  

#### Public Member

- 언더바 없이 시작하는 메소드나 속성
- **어디서나 호출 가능**, 하위 클래스 override 허용
- 메소드와 속성의 대다수를 차지



#### Protected Member

- 언더바 1개로 시작하는 메소드나 속성
- **암묵적 규칙에 의해 부모 클래스 내부와 자식 클래스에서만 호출 가능**
- 하위 클래스 override 허용



#### Private Member

- 언더바 2개로 시작하는 메소드나 속성
- 본 클래스 내부에서만 사용이 가능
- **하위클래스 상속 및 호출 불가능(오류)**
- 외부 호출 불가능(오류)



#### getter 메소드와 setter 메소드

- 변수에 접근할 수 있는 메소드를 별도로 생성
- getter 메소드: 변수의 값을 읽는 메소드
  - @property 데코레이터 사용
    - 함수를 변수처럼 선언할 수 있음
- setter 메소드: 변수의 값을 설정하는 성격의 메소드
  - @변수.setter 사용
    - 함수를 변수처럼 할당할 수 있음

```python
class Person:
    
    def __init__(self, age):
        self._age = age 
        
    @property
    def age(self):
        return self._age
    
    @age.setter  # progerty의 age를 의미함 _age로 쓰면 예외 발생
    def age(self, new_age):
        if new_age <= 19:
            raise ValueError('Too Young For SSAFY')
            return
        
        self._age = new_age
```

