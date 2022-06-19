## DB 설계

### ERD

- 협업 동료들과 프로젝트의 스펙을 커뮤니케이션 오류 없이 이해할 수 있으며, 프로젝트의 스펙을 정의



#### 인덱스

- 추가적인 쓰기 작업과 저장 공간을 활용하여 데이터베이스 테이블의 검색 속도를 향상시키기 이한 자료구조





## Mysql과 MariaDB 사용 이유

- DB 시장에서 사용할 수 있는 최초의 오픈 DB 중 하나
- 가장 널리 사용되는 RDBMS
- 오픈소스 라이선스지만 상업적 이용시 상업용 라이선스 구입 필요
- MySQL 창시자 몬티 와이드니어가 만든 프로젝트가 MariaDB
- 두 DB의 성능 차이는 별로 없음
- MariaDB와 MySQL의 호환성은 매우 높다
- AWS의 Amazon Aurora와 교체 사용하기 용이
- MariaDB은 상용 버전이 별도로 없음
- Mysql은 레퍼런스 많음



## 데이터 import 방법

- `Mysql workbench`, `mysql load data` 쿼리 등 사용
- 도로명 주소 -> addr 테이블 테이블로 import
- 보건복지부 선별진료소 -> medical 테이블로 import