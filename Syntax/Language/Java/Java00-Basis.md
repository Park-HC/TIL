## why java?

- 전자정부 프레임워크
  - 국책 사업에서 호환성을 위해 java spring을 기반으로 전산시스템을 만듦
  - 국가의 영향을 받는 많은 기업들 역시 java를 사용함
- JVM
  - 자바 바이트코드를 실행할 수 있는 주체
  - 플랫폼에 독립적이며 모든 자바 가상 머신은 자바 가상 머신 규격에 정의된 대로 자바 바이트코드를 실행

## 첫 코드

```java
System.out.print("string");
// string
System.out.println("string");
// string
//

System.out.printf("%d \n", 10); //정수(10진수)
System.out.printf("%o \n", 10); //정수(8진수)
System.out.printf("%x \n", 10); //정수(16진수)

System.out.print("4d \n", 10); //4칸 확보후 오른쪽부터 차지
System.out.print("-4d \n", 10); //4칸 확보후 왼쪽부터 차지
System.out.print("04d \n", 10); //4칸 확보후 오른쪽부터 차지(빈공간은 0)

System.out.printf("%f \n", 10.1); //실수
System.out.printf("%.2f \n", 10.1); //실수(소수점 둘째자리까지)

System.out.printf("%s \n", "홍승길"); //문자열
System.out.printf("%s의 나이는 %d 입니다", "홍승길", 26);
```



```
ctrl + shift + c
# 블록된 부분 주석처리

ctrl + shift + f
# 전체 정렬
```

