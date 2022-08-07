# Collection Framework

## 개요

- 객체들을 한 곳에 모아 놓고 편리하게 사용할 수 있는 환경 제공

- 정적 자료구조(Static Structure)
  - 고정된 크기의 자료구조
  - 배열이 대표적인 정적 자료구조
  - 선언 시 크기를 명시하면 바꿀 수 없음
- 동적 자료구조(Dynamic Structure)
  - 요소의 개수에 따라 자료구조의 크기가 동적으로 증가하거나 감소
  - 리스트, 스택, 큐 등



## java.util 패키지

- 다수의 데이터를 쉽게 처리

- Collection Framework 핵심 interface

| interface | 특징                                                         |
| --------- | ------------------------------------------------------------ |
| List      | 순서가 있는 데이터의 집합<br />순서가 있으니까 데이터의 중복을 허락<br />ArrayList, LinkedList 등 |
| Set       | 순서를 유지하지 않는 데이터의 집합<br />순서가 없어서 같은 데이터를 구별할 수 없음<br />중복 허락하지 않음<br />HashSet, TreeSet 등 |
| Map       | key와 value 쌍으로 데이터를 관리하는 집합<br />순서는 없고 key의 중복 불가<br />value는 중복 가능<br />HashMap, TreeMap |



### List

- 순서가 있고 중복을 허용
- 구현 클래스
  - ArrayList
  - LinkedList

- 내부적으로 배열을 이용해 데이터 관리
- 배열과 다르게 크기가 유동적으로 변함(동적 자료구조)
- 배열을 다루는 것과 유사하게 사용 가능

#### ArrayList

- 가장 기본적인 형태의 자료 구조로 간단하며 사용 용이
- 접근 속도 빠름
- 크리를 변경할 수 없어 추가 데이터를 위해 새로운 배열을 만들고 복사해야 함
- 비순차적 데이터의 추가, 삭제에 많은 시간이 걸림

#### LinkedList

- 각 요소를 Node로 정의하고 Node는 다음 요소의 참조값과 데이터로 구성됨
- 각 요소가 다음 요소의 링크 정보를 가지며 연속적으로 구성될 필요 없음



### Set

- 순서가 없고 중복을 허용하지 않음
- 빠른 속도
- 효율적인 중복 데이터 제거 수단
- 단순 집합의 개념으로, 정렬하려면 별도 처리가 필요함
- 구현 클래스
  - HashSet
  - TreeSet



### Map

- Key와 Value를 하나의 Entry로 묶어서 데이터 관리
- 순서 없음
- 키에 대한 중복 불가능
- 빠른 속도
- 구현 클래스
  - HashMap
  - TreeMap



### 정렬

- 요소를 특정 기준에 대한 내림차순 또는 오름차순으로 배치하는 것
- 순서를 가지는 Collection들만 정렬 가능
  - List 계열
  - SortedSet
  - SortedMap
- `sort(List<T> list)`

- #### Comparable interface

- #### Comparator

  - 객체가 Comparable을 구현하고 있지 않거나 사용자 정의 알고리즘으로 정렬하려는 경우
  - `sort(List<T>list, Comparator<? Super T>c)`

