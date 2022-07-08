# SELECT 문

## 순서

### SELECT 문 서술 순서

```sql
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
```



### SELECT 문 논리적 수행 순서

1. FROM
2. WHERE
3. GROUP BY
4. HAVING
5. SELECT
6. ORDER BY



## SELECT 문

- 저장되어 있는 데이터를 조회하고자 할 때 사용하는 명령어

`SELECT 컬럼1, 컬럼2, ..., FROM 테이블 WHERE 컬럼1 = '아무개';`

- `*`(asterisk) 쓰면 전체 컬럼이 테이블 컬럼 순서대로 조회됨
- `WHERE`절 없으면 테이블의 전체 인스턴스가 조회됨



### Alias

- Alias로 별칭을 붙이면, 그 이후론 이 별칭을 써야함
- `AS`로 Alias 붙일 수 있지만, SELECT의 Alias는 ORDER BY에만 쓸 수 있음!
- Alias를 붙여야 소문자로 컬럼명을 쓸 수 있음!



## WHERE 절

- INSERT를 제외한 DML 문을 수행시 원하는 데이터만 골라 수행할 수 있도록해주는 구문
- 비교 연산자 등을 사용



## GROUP BY

- 데이터를 그룹별로 묶을 수 있게 해주는 절
- BY 뒤에는 하나 이상의 기준 컬럼이 오게됨



## HAVING

- GROUP BY의 조건절
- 집계함수 사용 가능
- WHERE로 사용 가능한 조건은 WHERE에서 사용하는 것이 성능상 유리함
  - 연산 데이터량을 줄일 수 있음

- Group 없어도 반드시 사용불가능하진 않음



## ORDER BY

- SELECT한 데이터를 정렬함
- ORDER BY 절을 따로 명시하지 않으면 데이터는 임의의 순서대로 출력됨
- 컬럼명을 명시할 수 있고, 순서를 통해 SELECT 절의 컬럼을 지시할 수 있음

### 순서

- ASC: 오름차순(기본)
- DESC: 내림차순

### NULL

- NULL 값은 ORACLE에선 최대값으로 치지만 SQL Server에서는 최소값으로 침
- NULLS FIRST, NULLS LAST 옵션으로 NULL의 정렬상 순서를 변경할 수 있음