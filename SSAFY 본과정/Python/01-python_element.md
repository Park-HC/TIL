# Python 변수와 연산자

  ## 프로그래밍

  - 선언적 지시
  - 명령적 지시

  ## 코드 스타일 가이드

  - 코드를 '어떻게 작성할지'에 대한 가이드라인
  - 추천 스타일: PEP 8
  - 그외 오픈소스 등: 구글 스타일 가이드

  ### Space Sensitive

  - 문장을 구분할 때, 중괄호 대신 들여쓰기 사용
  - 들여쓰기에는 4(Tab칸 사용)

  ## 파이썬과 변수

  ### 변수란?

  컴퓨터 메모리 어딘가에 저장되어 있는 객체를 참조하기 위해 사용되는 이름

  데이터를 담는 상자 혹은 상자의 이름

  ### 객체란?

  숫자, 문자, 클래스 등 값을 가지고 있는 모든 것

  ### 변수의 데이터

  - 할당 연산자(=)를 통해 값을 할당(assignment)
  - `type()`
    - 변수에 할당된 값의 타입
  - `id()`
    - 메모리 주소



  ### 식별자(Identifiers)

```python
dust = 60
# 식별자(이름)은 dust
# 객체(값)은 60
```

  1. 영어 알파벳, 언더스코어, 숫자로 구성
  2. 첫 글자에 숫자가 올 수 없음
  3. 길이제한 없음
  4. 대소문자 구별
  5. 변수와 함수 이름 지을 때는 소문자+언더스코어(snake 케이스)
  6. 클래스 이름 지을 때는 대문자
  7. 몇몇 키워드로 *만들 수 없음*
  7. 내장함수나 모듈 등의 이름으로 *만들면 안 됨*
  7. 쓸데없이 긴 변수명보다는 짧은 변수명이, 알아보기 힘들 정도로 짧은 변수명보다는 긴 변수명이 더 낫다



  ### 사용자 입력

  - input([prompt])

  ### 주석

  ```python
  # 한 칸 띄기
  print('hello world')  # 두 칸 띄고 한 칸 띄기
  """
  여러줄
  쓰려면
  세 쌍따옴표 쓰기
  """
  ```

  

  ## 데이터 타입

  ### 불린(Boolean)

  - False
    - 0
    - ''
    - []
  - True
    - 1
    - -1
    - [1,2,3]

  ### 수치형

  - 모든 정수형 변수는 'int' 형태

  - 오버플로우 오류 없음

    - 가변 데이터

  - 정수가 아닌 모든 실수는 'float' 형태

    - 실수를 컴퓨터가 표현할 때 2진수(비트)로 표현함
    
    - 이 과정에서 floating point rounding error 발생, 예상치 못한 결과 발생
    
      > 부동소수점 문제
    
    ```python
    bool(3.14 - 3.02 == 0.12)
    	False
    ```
    
    ```python
    # 1. 임의의 작은 수
    abs(a - b) <= 1e-10
    
    # 2. system상의 machine epslion
    import sys
    print(abs(a - b)) <= sys. float_info.epsilon)
    print(sys.float_info.epsilon)
    
    # 3. Python 3.5이상
    import math
    math.isclose(a, b)
    ```

- 복소수는 'complex' 형태

  ```python
  a = 3 + 4j
  complex('1+2j')
  # 문자열을 complex로 치환할 수 있음
  complex('1 + 2j')
  # 문자열에 공백이 있으면 complex로 치환할 수 없음
  ```

  



  ### 문자열(String Type)

  - 모든 문자는 str 타입

  - 문자열은 ''나 ""로

  - Immutable

  - Iterable

  - 삼중따옴표

    - 여러줄 나누어서 표기할 때 사용

  - Escape Sequence

    | 에약문자 | 내용            |
    | -------- | --------------- |
    | \n       | 줄 바꿈         |
    | \t       | 탭              |
    | \r       | 캐리지리턴      |
    | \0       | 널(Null)        |
    | \\\      | \               |
    | \'       | 단일인용부호(') |
    | \"       | 이중인용부호(") |

  - String Interpolation

    - 문자열을 변수를 활용하여 만드는 법

    - %-formatting

      ```python
      print('Hello, %s' % name)
      print('내 성적은 %d' % score)
      ```

      

    - str.format()

      ```python
      print('Hello, {}! 성적은 {}'.format(name, score))
      ```

      

    - f-strings 방법

      ```python
      print(f'Hello, {name}! 성적은 {score}')
      ```

  ### None

  

  ## Container 변수

  ### List

  #### 생성

  ```python
  my_list = []
  your_list = ['서울', '부산']
  their_list = list()
  ```

 변수명에 `_list`를 붙이거나 복수형으로 써서 한 눈에 List란 걸 알아 볼 수 있게 설정하자

`enumerate()`: (index, value) 형태의 tuple로 구성된 열거 객체 반환

  

  ### Tuple

  - 불변 자료형
  - 소괄호 형태
  - 튜플 대입
    - 우변의 값을 좌변의 변수에 한 번에 할당하는 것

  ### Range

  - 숫자 시퀸스

  ### 패킹, 언패킹

  ```python
  x, *y = 1, 2, 3, 4
  x == 1
  y == [2,3,4]
  ```

  ```python
  def multiply(x, y ,z):
      return x * y * z
  
  numbers = [1,2,3]
  multiply(*numbers)
  	6
  ```

  

  ### Set

  - 순서 없이 0개 이상의 해시 가능한(중복 없는) 객체를 참조하는 자료형
  - 가변 자료형
  - {} set()
  - 순서가 없어, 별도의 값에 접근 불가능

  ### Dictionary

  * key는 변경 불가능한 데이터(list, dictionary 등 불가능)
    * 거의 대부분 string을 사용

  * value는 모든 값을 설정 가능

  	`keys()`: Key로 구성된 결과
  	
  	`values()`: value로 구성된 결과
  	
  	`items()`: (Key, value)의 튜플로 구성된 결과

  




  ### 형 변환(Typecasting)

  #### 암시적 형 변환

  사용자가 의도하지 않아도 파이썬 내부에서 자료형 변환함

  - bool

    ```python
    True + 100
    # 출력: 101
    
    3 + 3.2
    # int + float => float
    
    3 + (3 + 2j)
    # float + complex => complex
    
    3.2 + (3 + 2j)
    # float + complex => complex
    ```

    

  - 수치형(int <-> float)

  #### 명시적 형 변환

  

  ## 연산자

  ### 산술 연산자

  ### 비교 연산자

  ### 논리 연산자

  * 단축평가

  ```python
  a = 5 and 4
  b = 5 or 3
  c = 0 and 5
  d = 5 or 0
  
  a, b, c, d = (4, 5, 0, 5)
  ```

```python
True and False and True and True and False
# 2번째 연산에서 종료

True or True or True or False or False or 5 / 0
# 1번째 연산에서 종료, error 없음

'' or [] or None or 0 or 'a' or 'b' and ''
# 'a' 출력

'a' and 'b' in 'aeiou'
'b' and 'a' in 'aeiou'
# False, True
```



  ### 복합 연산자

```python
a += b  # a = a + b
a -= b  # a = a - b
a *= b  # a = a * b
a /= b  # a = a / b
a //= b  # a = a // b
a %= b  # a = a % b
a **= b  # a = a ** b
```



  ### 식별 연산자(Identity Operator)

```python
a = 3
b = 3
a is b  # True, -5 ~ 256까지 정수의 id는 동일

a = [1, 2]
b = [1, 2]
a is b  # False

a = 257
b = 257
a is b  # False # 257 이상의 정수는 id가 다름
```



  ### 멤버십 연산자

```python
not in
in
```



  ### 시퀸스형 연산자

  - 산술연산자(+)
    - 시퀸스 간의 연결, 연쇄
    
  - 반복연산자(*)
    - 시퀸스를 반복
    
  - 인덱싱
    - 특정 인덱스 값에 접근
    - 인덱스가 없는 경우 IndexError
    
  - 슬라이싱

    - 슬라이스 마지막 인덱스가 지나치게 크더라도 오류가 발생하지 않는다

      ```python
      print(s[::])    # 정순정렬(s 그대로 출력)
      print(s[::-1])  # 역순정렬
      ```

      

  - set 연산자
    - |: 합집합
    - &: 교집합
    - -: 여집합
    - ^: 대칭차

### 연산자 우선순위

```python
-3 ** 6 != (-3) ** 6
```

