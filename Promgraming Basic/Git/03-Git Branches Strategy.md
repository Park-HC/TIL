# Git Branches

## 브랜치 전략

### 정의

- 여러 개발자가 협업하는 환경에서 git 저장소를 효과적으로 활용하기 위한 work-flow
- 브랜치 생성에 규칙을 만들어 협업을 원만하게 함
- 브랜치의 생성, 삭제, 병합이 자유로운 git의 유연한 구조를 활용하여 다양한 방식으로 소스 관리를 할 수 있음



### git-flow

- 5가지 브랜치를 이용해 운연하는 브랜치 전략

- 2개의 메인 브랜치와 역할을 완료하면 사라지는 3개의 보조 브랜치로 구성

#### 메인 브랜치

- 항상 유지됨
- master: 제품으로 출시될 수 있는 브랜치
- develop: 다음 출시 버전을 개발하는 브랜치

#### 보조 브랜치

- merge 되면 삭제
- feature: 기능을 개발하는 브랜치
- release: 이번 출시 버전을 준비하는 브랜치
- hotfix: 출시 버전에서 발생한 버그를 수정하는 브랜치



#### 개발 플로우

1. develop 브랜치로부터 본인이 개발한 기능을 위한 feature 브랜치 생성
2. feature 브랜치에서 작업하다 기능이 완성되면 delvelop 브랜치에 merge
3. 이번 배포 버전의 기능들이 develop에 모두 merge 뙜으면 QA를 위해 release 브랜치 생성
4. release 브랜치에서 오류 발생시 realse 브랜치 내에서 수정
5. QA가 끝났다면 해당 버전 배포를 위해 master 브랜치로 merge함
6. bugfix가 있었다면 해당 내용 반영을 위해 develop 브랜치에도 merge
7. 만약 제품(master)에서 버그 발생시 hotfix 브랜치 생성하고 bugfix
8. bugfix가 끝났다면 develop와 master 브랜치에 각각 merge



#### 특징

1. 주기적으로 배포를 하는 서비스에 적합
2. 가장 유명한 전략
3. IDE가 지원됨



### github-flow

- master 브랜치와 Pull Request를 활용하는 단순한 브랜치 전략

- 메인 브랜치는 제품이 release되는 master 하나만 존재
- 어떠한 목적으로 보조 브랜치를 생성했는지 제목에 명시
- 커밋 메시지도 상세하게
- 기능/버그 fix 등이 끝나면 pull request
- 이상이 없는지 pull을 검토
- 리뷰가 끝나면 실제 서버에 배포
- 이상이 없다면 master에 merge 후 push, 즉시 배포(배포 자동화 권장)
- 코드의 지속적 통합(CI) 지속적 배포(CD)가 이루어짐