# List

## 정의

> C나 Java의 배열과 유사

같은 타입 변수들을 하나의 이름으로 열거하여 사용하는 자료구조

### 배열과 리스트의 차이점

| ()     | 배열                     | 리스트               |
| ------ | ------------------------ | -------------------- |
| 데이터 | 같은 타입 데이터만 가능  | 다양한 데이터 가능   |
| 크기   | 처음 지정 후 변경 불가능 | 가변적으로 변경 가능 |

### 시퀸스(Sequence) 자료형

순서가 존재함으로서, 인데싱과 슬라이싱 연산 모두 가능

- 인덱싱(Indexing)

  - 시퀸스 자료형에서 하나의 요소를 인덱스 연산자를 통하여 참조하는 것

    ```python
    arr[0]
    arr[-1]
    ```

- 슬라이싱(Slicing)

  - 시퀸스 자료형의 원하는 범위를 선택하는 연산

    ```python
    arr[:]
    arr[1:3]
    ```



## 사용법

### 리스트 생성

#### 공백 리스트

```python
num = []
arr = list()
```

### 리스트 함축(List Comprehension)

```python
new list = [i for i in mylist if i&2==0]
```



## 2차원 List

### 구조

- 1차원 list를 묶어놓은 list

- 2차원 이상의 다차원 List는 차원에 따라 Index를 선언

- 2차원 List의 선언, 세로길이(행), 가로길이(열)을 필요로함

  ```python
  arr = [[0, 1, 2, 3], [4, 5, 6, 7]]
  
  brr=[[0,0,0] for _ in range(3)]
  
  crr=[[0,0,0] * 3]
  ```





### 선언

```python
"""
3 4
0 1 0 0
0 0 0 0
0 0 1 0
입력 받기
"""

# 1
n, m = map(int, input().split())

mylist = [0 for _ in range(n)]
# mylist = [0] * n

for i in range(n):
    mylist[i] = list(map(int, input().split()))
    
# 2
n, m = map(int, input().split())

mylist = []
for i in range(n):
    mylist.append(list(map(int,input().split())))
    
# 3
n, m = map(int, input().split())
mylist = [list(map(int, input().split())) for _ in range(n)]
```



### 위치 찾기

```python
newlist = [(i, j) for i in range(n) for j in range(m) if mylist[i][j] == 1]
```



### List 순회

> List의 모든 원소를 빠짐 없이 조사하는 방법

#### 행 우선 순회

```python
for i in range(len(arr)):
    for j in range(len(arr[i])):
        arr[i][j]
```



#### 열 우선 순회

```python
for j in range(len(arr[0])):
    for i in range(len(arr)):
        arr[i][j]
```



#### 지그재그 순회

> 첫 열은 우측으로 다음 열은 좌측으로 조사하는 방법

```python
for i in range(len(arr)):
    for j in range(len(arr[0])):
        arr[i][j + (m-1-2*j)*(i%2)]
```



### 델타 탐색 방법

- 2차 list의 한 좌표에서 네 방향의 인접 list 요소를 탐색할 때 사용하는 방법
- 델타 값은 한 좌표에서 네 방향의 좌표와 x, y의 차이를 저장한 list로 구현
- 델타 값을 통해 특정 원소의 상하좌우에 위치한 원소에 접근할 수 있음
- 상화좌우에 원소가 없을 수 있으므로, index 제한이 필요함

```python
# arr: N * N
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for x in range(len(arr)):
    for y in range(len(arr[x])):
        for i in range(4):
            testX = x + dx[i]
            testY = y + dy[i]
            print(arr[testX][testY])
```



#### 전치행렬

- 행과 열의 값이 반대인 행렬을 의미
- 대각선 기준 한쪽만 바꿔야 함

```python
arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for i in range(3):
    for j in range(3):
        if i < j:
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]
            
# zip 사용
list(zip(*arr))
```



### Bit List

- 0과 1로 이루어진 리스트
- 모든 가능한 bit list를 만들어 어느 집합의 모든 부분집합의 합들을 완전 탐색할 때 쓸 수 있음

#### Bit List 없이 부분집합 구하기?

```python
n = len(arr)

for i in range(1<<n):  # 부분 집합의 개수
    for j in range(n):  # 원소의 수만큼 비트 비교
        if i&(1<<j):  # i의 j번째 비트가 1이면 j번째 원소 출력
            print(arr[j], end=",")
print()
```

