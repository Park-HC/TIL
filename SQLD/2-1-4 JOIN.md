# JOIN

- 각기 다른 테이블을 한 번에 보여줄 때 쓰이는 쿼리
- SQL 중 가장 많은 비중을 차지함
- JOIN되는 테이블들에 모두 존재하는 컬럼은 반드시 컬럼 명 앞에 테이블 명이나 Alias를 붙어 구분해야 함

## EQUI JOIN

- Equal 조건으로 JOIN하는 것

## NON EQUI JOIN

- Equal 외 조건(BETWEEN, > 등)으로 JOIN하는 것

## OUTER JOIN

- JOIN 조건에 만족하지 않는 행들도 출력
- 출력되는 테이블의 반대편 테이블 옆에 (+) 기호를 붙여 작성



# STANDARD JOIN

- 표준 조인
- 모든 SQL 언어에서 사용 가능

## INNER JOIN

`FROM ~ INNER JOIN ~ ON ~~~`

- JOIN 조건에 충족되는 데이터만 출력됨

## OUTER JOIN

### LEFT OUTER JOIN

`FROM ~ LEFT OUTER JOIN ~ ON ~~~`

`WHERE ~~ (연산자) ~~(+)`와 동일

### RIGHT OUTER JOIN

`FROM ~ RIGHT OUTER JOIN ~ ON ~~~`

### FULL OUTER JOIN

- LEFT OUTER JOIN + RIGHT OUTER JOIN - 중복값



## NATURAL JOIN

- 각 테이블의 같은 이름을 가진 컬럼들이 모두 동일한 데이터를 가지고 있을 경우 JOIN 되는 방식
- **ON 사용 불가능**
- SQL Server에서는 지원하지 않음
- USING을 사용하여 비교할 컬럼을 지정할 수 있음
  - 단, 이 때 **SELECT에서** USING에 사용된 컬럼에 **별도의 테이블명이나 별칭을 붙여선 안 됨**



## CROSS JOIN

- 조합할 수 있는 모든 경우를 출력
- `FROM ~ CROSS JOIN ~` 혹은 `FROM ~, ~`로 표현 가능
- `WHERE` 사용 가능



## HASH JOIN

- 인덱스가 없는 두 개의 테이블에 사용
- Equal join에서만 사용 가능
- 대량의 데이터 처리에 사용
- 작은 테이블을 MEMORY에 올리는 선행 테이블로 씀



## NESTED LOOP JOIN

- 중첩된 반복문과 유사한 방식으로 조인을 수행하는 방식