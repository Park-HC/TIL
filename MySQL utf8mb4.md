# MySQL utf8mb4

- 이모지 같은 글자들은 utf8 인코딩 시 글자 당 최대 4bytes까지 필요함
- 기존 MySQL의 utf8 필드는 3bytes까지 지원
- 그렇기에 utf8mb4 설정을 해야 제대로 저장이 됨

## collation 설정

- database에서 문자열을 정렬할 때 어떤 문자들이 먼저 올지를 결정하는 기준
- utf8mb4_general_ci 이 기본값
  - 비 라틴어 언어들에 대해서는 정렬이 조금 어색함
  - utf8mb4_unicode_ci가 약간 느린 대신 정렬이 정확한 편



```mysql
SHOW GLOBAL VARIABLES WHERE Variable_name LIKE 'character\_set\_%' OR Variable_name LIKE 'collation%';
/* 환경 변수들의 collation 설정을 확인 */
```



# Spring Bean

## Bean

- Spring IoC 컨테이너가 관리하는 자바 객체
- new 연산자로 생성되지 않으며 `ApplicationContext.getBean()`로 얻을 수 있음
- 즉, ApplicationContext에서 만들어져 담아진 객체



## 등록 방법

### Component Scan

- `@ComponentScan` 어노테이션과 `@Component` 어노테이션을 사용해 빈을 등록
- `@ComponentScan`은 어느 지점부터 컴포넌트를 찾으라고 알려줌
- `@Component`는 실제로 찾아서 빈으로 등록할 클래스

#### 라이프 사이클 콜백

- Spring IoC 컨테이너로 IoC 컨테이너를 만들고 그 안에 빈을 등록할 때 사용하는 인터페이스들을 라이프 사이클 콜백이라고 부름



### 빈 설정파일에 직접 빈을 등록

- XML 혹은 자바 설정 파일로 작성 가능





# IntelliJ + Maria DB

## 연동

- Database 탭, +, Data Source, Maria DB 클릭
- 드라이브 파일이 없는 경우 드라이브 다운
- IP, 포트, 계정과 비밀번호 입력 후 **Test Connection** 클릭
- connection 성공하면 apply, ok 클릭



## Gradle 사용시(JPA)

### build.gradle

```
dependencies {
 implementation 'org.springframework.boot:spring-boot-starter-web'
 implementation 'org.springframework.boot:spring-boot-starter-data-jpa'
 runtimeOnly 'org.mariadb.jdbc:mariadb-java-client:2.7.4'
 compileOnly 'org.projectlombok:lombok'
 annotationProcessor 'org.projectlombok:lombok'
 testImplementation('org.springframework.boot:spring-boot-starter-test') {
  exclude group: 'org.junit.vintage', module: 'junit-vintage-engine'
 }
}
```

- `runtimeOnly`: 실행 시점에 필요



### application.properties

```
spring.datasource.driver-class-name=org.mariadb.jdbc.Driver
spring.datasource.url=jdbc:mariadb://localhost:3306/DB명
spring.datasource.username=userName
spring.datasource.password=password

#update the schema with the given values.
spring.jpa.hibernate.ddl-auto=update
#To beautify or pretty print the SQL
spring.jpa.properties.hibernate.format_sql=true
#show sql
spring.jpa.properties.hibernate.show-sql=true
#show parameter binding
logging.level.org.hibernate.type.descriptor.sql=DEBUG

logging.level.org.hibernate.SQL=DEBUG
```



## Error?

### cannot resolve class or package 'mariadb'

- File -> Invlidate Caches / Restart... 를 실행 후 IntelliJ IDEA를 재시작



### Syntax Error: Error: PostCSS received undefined instead of CSS string

- `npm rebuild node-sass`



# ERD 작성 프로그램

## vertabelo