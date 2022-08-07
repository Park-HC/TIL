# Generics

- 다양한 타입의 객체를 다루는 메서드
- 컬렉션 클래스에서 컴파일 시에 타입 체크하여 타입 파라미터들에 타입을 대입
  - **미리 사용할 타입을 명시해서 형 변환을 하지 않아도 되게 함**
  - 객체 타입에 대한 안전성 향상 및 형 변환의 번거로움 감소

- 조상 클래스/미들웨어 등에서는 쓰일 수 있지만
  - 구체적인 구현에서는 generic으로 구축할 일 없음
  - generic 형식을 받아 코드를 구성할 일이 있으므로 이해가 필요



## 예제

### 객체 생성

```java
Class_Name<String> generic = new Class_Name<String>();
Class_Name<String> generic2 = new Class_Name<>();
Class_Name generic = new Class_Name();
```

### 클래스 생성

```java
// non-generic
// Object를 파라미터로 사용하면 어떤 객체든지 수용 가능
class NormalBox{
    private Object some;
    
    public Object getSome() {
        return some;
    }
    
    public void setSome(Object some) {
        this.some = some;
    }
}

// generic
// T로 객체를 한정해 T의 자식까지만 허용됨
class GenericBox<T> {
    private T some;
    
    public T getSome() {
        return some;
    }
    
    public void setSome(T some) {
        this.some = some;
    }
}
```



## 표현

- 클래스 또는 인터페이스 선언시 `<>`에 타입 파라미터 표시

```java
ClassName: Raw Type;
ClassName<T>: Generic Type;
```

- 타입 파라미터
  - 특별한 의미의 알파벳 보다는 단순히 임의의 참조형 타입을 말함
  - T
    - reference Type
    - 별다른 목적이 없을 경우(일반적인 경우) 사용
  - E
    - Element
  - K
    - Key
  - V
    - Value



## Type Parameter 제한

- 필요에 따라 구체적인 타입 제한 필요
  - 계산기 구현시 Number 이하 타입(Byte, Short, Integer 등)로 제한하는 등
- type parameter 선언 뒤 extends와 함께 상위 타입 명시

```java
class NumberBox<T extends Number>
```

- 인터페이스로 제한할 경우도 extends로 사용
- 클래스와 함께 인터페이스 제약 조건을 이용할 경우 &로 연결



## Generics

- Generic Type 객체를 할당 받을 때 와일드 카드 이용

  - generic type에서 구체적인 타입 대신 사용

  | 표현                        | 설명                                   |
  | --------------------------- | -------------------------------------- |
  | `Generic type<?>`           | 타입에 제한이 없음                     |
  | `Generic type<? extends T>` | T 또는 T를 상속받은 타입들만 사용 가능 |
  | `Generic type<? super T>`   | T 또는 T의 조상 타입만 사용 가능       |



### Generic Method

- 파라미터와 리턴타입으로 type parameter를 갖는 메서드
- 메서드 리턴 타입 앞에 타입 파라미터 변수 선언

```java
[제한자] <타입_파라미터, [...]> 리턴_타입 메서드_이름(파라미터) {
    // do something
}
```

