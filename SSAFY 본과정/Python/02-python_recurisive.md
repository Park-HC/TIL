# Python 제어문(Control Statement)

> **코드 실행의 순차적인 흐름을 제어**(Control Flow)하는 코드

  ## 조건문(Contional Statement)

  ### 기본 형식

  ```python
if <expression == True>:  # expression은 참 거짓 판단이 가능해야함
    # Run this Code Block
else :
    # Run this Code Block
  ```



  ### 복수 조건문

  ```python
if <expression == True>:
    # Run this Code Block
elif <expression == True>:
    # Run this Code Block
elif <expression == True>:
    # Run this Code Block
else:
    # Run this Code Block
  ```



  ### 중첩 조건문

  ```python
if <expression == True>:
    # Run this Code Block
    if <expression == True>:
        # Run this Code Block
elif <expression == True>:
    # Run this Code Block
elif <expression == True>:
    # Run this Code Block
else:
    # Run this Code Block
  ```

  

  ### 조건 표현식

  ```python
value = num if num >= else -num
# value = abs(num)

result = '홀수입니다.' if num % 2 else '짝수입니다'
  ```

  

  ## 반복문

  ### While

  ```python
while <expression>:
    # Code block
  ```

  ### For

  ```python
for <변수명> in <iterable>:
    #Code block
else:
    #Code block
  ```

  ```python
chars = input()

for char in chars:
    print(char)

for idx in range(len(chars)):
    print(chars[idx])
  ```

  #### List Comprehension

  ```python
[<expression> for <변수> in <iterable>]
[<expression> for <변수> in <iterable> if <조건식>]
  ```

  #### Dictionary Comprehension

  ```python
{key: value for <변수> in <iterable>}
{key: value for <변수> in <iterable> if <조건식>}
  ```

  ### 반복문 제어

    1. break
       - 반복문을 종료
    2. continue
       - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
    3. for-else
       - 끝까지 반복문을 실행한 이후에 else문 실행
       - break 종료되는 경우 else문은 실행되지 않음
    4. pass
       - 아무것도 하지 않음
       - 반복문이 아니여도 사용 가능