# What is pyd

## .py .pyc .pyd

1. .py
   - 파이썬 소스 코드 파일
2. .pyc
   - 파이썬 소스를 컴파일해서 생성된 파이트 코드
   - 성능 향상 효과가 크지 않음
3. .pyo
   - pyc를 최적화한 파일
4. .pyd
   - 파이썬을 사용해 windows dll로 만들어진 C 모듈
   - 파이썬이 C모듈 사용하거나 그 반대 가능함(파이썬은 C에서 파생)
5. .pyw
   - window용 python 스크립트
   - pythonw.exe로 실행됨
6. .pyx
   - c 혹은 c++로 변환될 Cython src

출처: https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=wonjinho81&logNo=220551935772



## then... what is Cython?

### cpython

- C 언어로 파이썬을 구현한 것
- python을 한줄 한줄 읽으며 cpu가 이해하게 하는 인터프린터



### cython

- 멀티프로세스라 낮은 성능이란 단점을 극복한 언어
- c언어에 python 문법을 사용(c++과 유사)

출처: https://yomangstartup.tistory.com/108



## Wait, what is DLL?

### Dynamic Link Library

- 실행 파일에서 라이브러리의 기능을 사용할 경우 참조하게 되는(동적 연결) 라이브러리
- 컴파일 시간이 줆
- 타사 프로그램에 애드온 기능을 제공할 때 소스 코드를 숨길 수 있음
- 개발환경의 통일 없이 모듈별로 작업 가능
- 소스 코드 관리에 용이
- 로딩 시간이 길어 짐
- 하나의 DLL에 충돌이 생기면 수많은 프로그램이 오류를 뱉을 수 있음



### 애드온?

- Add-on, 플러그인과 유사한 개념
- 추가 기능을 위한 컴퓨터 프로그램 모듈 혹은 장치