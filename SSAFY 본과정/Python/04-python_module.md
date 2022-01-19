# 모듈

## 모듈과 패키지

### 정의

- 모듈
  - 특정 기능을 하는 코드를 파이썬 파일(.py) 단위로 작성한 것
- 패키지
  - 특정 기능과 관련된 여러 모듈의 집합
  - 패키지 안에는 또 다른 서브 패키지를 포함

### 불러오기

```python
import moudle
from module import var, function, Class
from module import *

from package import module
from package.module import var, function, Class
```



## 파이썬 표준 라이브러리

- 파이썬에 기본적으로 설치된 모듈과 내장함수

- https://docs.python.org/ko/3.9/library/index.html



### 파이썬 패키지 관리자(pip)

- PyPI에 저장된 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템
- 설치 명령어

```bash
$ pip install SomePackage
$ pip install SomePackage==1.05
$ pip install 'SomePackage>=1.04'
```

- 삭제 명령어

> 없그레이드 시 과거 버전을 자동으로 지워줌

```bash
$ pip uninstall SomePackage
```

- 패키지 목록 및 특정 패키지 정보

```bash
$ pip list
$ pip show SomePackage
```

- 패키지 freeze
  - 설치된 패키지의 비슷한 목록을 만들지만, pip install에서 활용되는 형식으로 출력
  - 해당 목록을 requirements.txt(관습)으로 만들어 관리함

```bash
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```



## 사용자 모듈과 패키지

- 사용자 모듈

```python
# check.py
def odd(n):
    return bool(n % 2)

def even(n):
    return not bool(n % 2)
```

```python
import check
dir(check)
check.odd(3)
check.even(3)
```



- 사용자 패키지
  - 모든 폴더에 `__init__.py`를 만들어 패키지로 인식



## 가상환경

### 필요성

- 외부 패키지와 모듈 사용시 모두 pip 통해 설치
- 복수의 프로젝트 진행시 필요 버전이 상이할 수 있음
- 이 경우 가상환경을 통해 프로젝트별 독립적인 패키지를 관리할 수 있음

### venv

- 가상환경을 만들고 관리하는데 사용되는 모듈
- 특정 디렉토리에 가상 환경 만들고, 고유한 파이썬 패키지 집합을 가질 수 있음

### 명령어

```bash
# 생성
$ python -m venv <폴더명>

# 활성화/비활성화
$ source <폴더명>/bin/activate  # bash의 경우
$ deactivate

```

