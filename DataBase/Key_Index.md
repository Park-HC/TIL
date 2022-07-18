## index와 Primary Key

- 일반적인 DBMS에서 PK는 자동으로 Index 적용됨
- PK는 개념적인 값
  - 여러 Tuple 중 유일한 Tuple임을 보장
  - 실제 값이 존쟂하지만 PK라고 **물리적으로 저장되지 않음**
- Index는 Tuple의 유일성을 보장하지 않음
  - 단지 테이블에서 Tuple을 보다 빨리 찾기 위한 도구
  - index를 컬럼에 걸면 그 컬럼을 기준으로 새로운 자료 구조(Binary-tree 등)을 생성해 별도의 디스크 공간에 저장

### 예시

- 만약 이름이 철수인 사람을 찾는다면?
- Index가 이름에 걸리지 않아있을 경우
  - 테이블의 모든 Tuple을 가져와 일일이 이름을 비교하며 Tuple을 찾음
- Index가 이름에 걸려 있을 경우
  - Index로 생성된 별도의 자료 구조에서 철수를 찾고 이에 해당하는 Tuple을 가져옴
  - 별도의 자료 구조는 이름을 기준으로 정렬되어 있기에 모든 자료를 검색하지 않아도 됨
