# Stack

## Stack의 개념

- 프로그램에서 중요성과 활용성이 매우 높은 자료구조
- 물건을 쌓아 올리듯 자료를 쌓아 올린 형태의 자료구조
- 스택에 저장된 자료는 선형 구조(자료간 일대일 대응)
- 스택에 자료를 삽입하거나 자료를 꺼낼 수 있음
- 자료를 꺼낼 때 마지막에 삽입한 자료를 가장 먼저 꺼냄
  - 후입선출(Last-in Frist-out)



## Stack의 구현

### 자료구조

- 자료를 선형으로 저장할 저장소가 필요함
  - C언어에서는 배열, 파이썬에서는 리스트를 사용함
  - 저장소 자체를 스택이라 부르기도 함
  - 마지막으로 삽입된 원소의 위치를 top이라 부름

### 연산

- `push`: 저장소에 자료를 저장함

```python
def push(self, item):
    self.append(item)
```

- `pop`: 저장소에서 자료를 꺼냄

```python
def pop(self):
    if len(self) == 0:
        # underflow
        return
    else:
        return self.pop(-1)
```

- `isEmpty`: 스택이 공백이지 아닌지 확인
-  `peek`: 스택의 top에 있는 item을 반환



### 주의 사항

- 리스트를 사용해 스택을 구현하면
  - 구현이 용이함
  - 리스트의 크기를 변경하는 작업이 크 overhead 발생 작업으로 많은 시간 소요됨

- 리스트의 크기가 변동되지 않도록 배열처럼 크기를 미리 정해놓고 사용하거나
- 동적 연결 리스트를 이용해 저장소를 동적 할당으로 구현하는 법



## Stack의 응용

### 괄호검사

#### 문제 조건

##### 괄호의 종류

- 대괄호: []
- 중괄호: {}
- 소괄호: ()

##### 괄호의 조건

- 왼쪽 괄호의 개수와 오른쪽 괄호의 개수가 같아야 함
- 같은 괄호에서 왼쪽 괄호는 오른쪽 괄호보다 먼저 나와야 함
- 괄호 사이에는 포함관계만 존재

#### 알고리즘

- 왼쪽 괄호가 나오면 스택에 push
- 오른쪽 괄호가 나오면 스택에서 pop
- 빈 스택을 pop하면 Error
- 수식이 끝났는데 괄호가 있으면 Error
- 짝이 맞지 않으면 Error

### 함수 호출 관리

#### 개요

- 함수 호출과 복귀에 따른 수행 순서 관리
- 가장 마지막에 호출된 함수부터 실행하고 복귀하는 후입선출 구조이므로 스택을 이용해 수행순서 관리
- 함수 호출 시 호출한 함수의 수행에 필요한 지역변수, 매개변수, 수행 후 복귀할 주소 등의 정보를 스택 프레임에 저장해 시스템 스택에 삽입
- 실행이 끝나면 시스템 스택의 top 원소를 pop하고 저장되어 있던 복귀 주소로 복귀
- 전체 프로그램 수행이 종료시 시스템 스택은 공백 스택이 됨



### 재귀 호출

#### 개요

- 재귀 호출은 자기 자신을 호출하여 순환 수행되는 것
- 프로그램의 크기를 줄이고 간단하게 작성 가능
- 디버깅이 어렵고 수행 시간이 늘어날 수 있음

#### Memoization(메모이제이션)

- 이전에 계산한 값을 메모리에 저장해서 매번 다시 계산하지 않도록 해 실행 속도를 빠르게 함
- DP(동적 계획법)의 핵심이 되는 기술

#### 예제 - 피보나치

```python
# memo를 위한 리스트 생성
# memo[0]을 0으로 memo[1]은 1로 초기화 한다

def fibo1(n):
    global memo
    if n>= 2 and len(memo) <= n:
        memo.append(fibo(n-1) + fibo(n-2))
    return memo[n]

memo = [0, 1]
```



### 동적 계획법(DP)

- 입력 크기가 작은 부분 문제들 모두 해결 후 그 해들을 이용해 보다 큰 크기의 문제 해결
- recursive 방식과 iterative 방식이 있음
- 성능면에서는 iterative가 앞섬



## 깊이 우선 탐색(DFS)

### 개요

- 시작 정점의 한 방향으로 갈 수 있는 경로가 있는 곳까지 탐색
- 더 이상 갈 곳이 없게 되면, 가장 마지막에 만났던 갈림길 간선이 있는 정점으로 되돌아 옴
- 다른 방향의 정점으로 탐색을 계속 반복하여 결국 모든 정점을 방문하여 순회
- 가장 마지막에 만났던 갈림길의 정점으로 되돌아가서 탐색을 반복해야 하므로 후입선출 방식의 Stakc을 사용함

### 알고리즘

1. 정점 v를 결정하여 방문
2. 정점 v에 인접한 정점이 있는지 탐색
3. 방문하지 않은 정점 w가 있으면 정점 v를 스택에 push하고 정점 w 방문
4. w를 v로 하여 1 반복
5. 방문하지 않은 정점이 없으면 스택을 pop하고 받은 가장 마지막 방문 정점을 v로 하여 다시 1 반복

### 가상 코드

```
visited[], stack[] 초기화

DFS(v)
	v 방문;
    visited[v] <- true;
    do {
        if {v의 인접 정점 중 방문 안 한 w가 있는가}
        	push(v);
        while(w) {
        	w 방문;
        	visited[w] <- true;
        	push(w);
        	v <- w;
        	v의 인접 정점 중 방문 안 한 w ckwrl
        }
        v <- pop(stack);
    } while(v)
end DFS()
```
