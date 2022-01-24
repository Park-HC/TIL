# 데이터 구조

## 문자열

### 정의

- 문자들의 나열
- 모든 문자는 str 타입
- ''나 ""로 표기
- immutable



### 조회, 탐색 메소드

```python
s. find(x)
# x의 첫번째 위치를 반환, 없으면 -1 반환

s.index()
# x의 첫번째 위치를 반환, 없으면 오류 발생

s.isalpha()
# 알파벳 문자(숫자가 아닌 문자) 여부

s.issupper()
# 대분자 여부

s.islower()
# 소문자 여부

s.istitle()
# 타이틀 형식 여부

## is가 붙은 메소드는 대부분 boolean 반환
```



#### ''.find() vs ''.index()

- 있는 문자를 검색시 반환하는 값은 둘이 같음
- 없는 문자를 검색시, find는 -1을 반환하고 index는 오류가 발생함
- 상황에 따라 둘 중 어느 것이 유용한지가 정해짐(return 값 vs 에러 예외처리)

```python
a = 'apple'
a.find('p')
a.index('p')
# 1 1

a.find('z')
# -1

a.index('z')
# ValueError: substring not found
```

#### 문자열 검증 메소드

```python
s.isdecimal()
s.isdigit()
s.isnumeric()
# 아래로 갈 수록 포괄적
```



### 문자열 변경 메소드

> 문자열을 직접 수정하는 게 아니라, 수정된 문자열을 반환하는 것임

```python
s.replace(old, new[, count])
# 바꿀 대상 글자를 새로운 글자로 바꿔서 반환

s.strip([chars])
# 공백이나 특정 문자를 제거

s.split(sep=None, maxsplit=-1)
# 공백이나 특정 문자를 기준으로 분리
# 선행 후행 공백은 빈 문자열 포함시키지 않음
# maxsplit == -1인 경우 제한 없음

'separator'.join([iterable])
# 구분자로 iterable을 합칩

s.capitalize()
# 가장 첫 번째 글자를 대문자로

s.title()
# '나 공백 이후를 대문자로

s.upper()
# 모두 대문자

s.lower()
# 모두 소문자

s.swapcase()
# 대 <-> 소문자 변경하여
```



## 리스트(List)

### 정의

- 순서를 가지는 0개 이상의 객체를 참조하는 자료형
- 가변자료형

### 메소드

```python
L.append(x)
# 리스트 마지막에 항목 x 삽입

L.extend(iterable)
# 리스트에 반복가능한 변수를 삽입함
# 문자열을 직접 입력할 경우, 문자 하나하나가 삽입됨

L.inser(i,x)
# 인덱스 i에 항목 x 삽입

L.remove(x)
# 리스트 가장 왼쪽에 있는 항목 x를 제거
# 항목이 존재하지 않으면 ValueError

L.pop()
# 리스트의 마지막 항목을 삭제하고 그 항목을 반환함

L.pop(i)
# 리스트의 인덱스 i 항목을 삭제하고 그 항목을 반환함

L.index(x, start, end)
# x 값을 찾아 인덱스를 반환

L.reverse()
# L의 순서를 뒤집고 None 반환
# reversed는 뒤집힌 리스트를 반환만 함

L.sort()
# L을 정렬하고 None 반환
# sorted는 정렬된 리스트를 반환만 함

L.count(x)
# x 값의 개수를 반환

```



## 튜플(Tuple)

### 정의

- 순서를 가지는 0개 이상의 객체를 참조하는 자료형
- 불변 자료형
- 값에 영향을 미치지 않는 메소드만을 지원
- 리스트 메소드 중 항목 젼경 메소드 제외하고 대부분 동일함



## 셋(Set)

### 정의

- 순서없이 0개 이상의 해시 가능한 객체를 참조하는 리스트
- 해시 가능한 객체(불변자료형)만 담을 수 있음(리스트, 딕셔너리 불가능)
- 가변자료형



### 메소드

```python
s.add(x)
# set에 x가 없다면 추가함

s.copy()
# set의 shallow copy를 반환

s.pop()
# set에서 랜덤하고 항목을 지우고 그 항목을 반환함
# set이 비었을 경우 KeyError

s.remove(x)
# set에서 항목 x를 제거함
# 항목 x가 없는 경우 KeyError

s.discard(x)
# set에 항목 x가 있는 경우 제거함

s.update(t)
# set t에 있는 모든 항목 중 셋 s에 없는 항목을 추가함

s.clear()
# 모든 항목을 제거함

s.isdisjoint(t)
# set s와 set t가 공유하는 항목이 없을 경우 True 반환

s.issubset(t)
# set s가 set t의 하위 셋인 경우 True 반환

s.issuperset(t)
# set s가 set t의 상위 셋인 경우 True 반환
```



## 딕셔너리(Dictionary)

### 정의

- 순서 없이 키-값 쌍으로 이뤄진 객체를 참조하는 자료형
- 딕셔너리의 키는 해시가능한 불변 자료형
- 키의 값은 모든 형태 가능



### 메소드

```python
d.claer()
# 모든 항목 제거

d.copy()
# dictionary의 shallow copy를 반환

d.keys()
# dictionary의 모든 키를 담은 뷰 반환

d.values()
# dictionary의 모든 값을 담은 뷰 반환

d.items()
# dictionary의 모든 키-값 쌍을 담은 뷰 반환

d.get(k)
# 키 k의 값 반환
# 없을 경우 None 반환

d.get(k, v)
# 키 k의 값 반환
# 없을 경우 v 반환

d.pop(k)
# 키 k를 삭제하고 값 반환
# 없을 경우 KeyError

d.pop(k, v)
# 키 k를 삭제하고 값 반환
# 없을 경우 v 반환

d.update(....)
# dictionary d의 값을 매핑하여 업데이트
```



## 얕은 복사, 깊은 복사

### 할당(assignment)

```python
list_b = list_a
```

- 대입 연산자
- 해당 객체에 대한 객체 참조를 복사함
- 해당 주소의 일부 값을 변경하는 경우 이를 참조하는 모든 변수에 영향



### 얕은 복사(shallow copy)

```python
list_b = list_a[:]
```

- Slice 등을 이용해 원소 값만을 복사(저장)하
- 복사 대상인 리스트에 주소를 참조하는 변수인 원소(이중 리스트 등)가 있다면
- 할당처럼 복사 결과인 리스트에도 같은 주소를 참조하는 원소가 생기게 됨



### 깊은 복사(deep copy)

```python
import copy
list_b = copy.deepcopy(list_a)
```

- 복사 대상과 결과물 중 같은 대상을 참조하는 원소가 없게 함