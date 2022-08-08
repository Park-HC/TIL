# 응용

## little question

- first commit할 때 찍히는 root-commit은?
  - git에서 필수인 root를 뜻함
- master의 뜻은?
  - master brach를 뜻하는 스티커
- git log에서 빠져나오려면
  - press `Q`
- git checkout <commit 주소>
  - 그 시점을 불러옴
  - <주소> 대신 브랜치 이름을 넣으면 브랜치로 이동함(switch와 동일한 기능)
  - `git checkout -- .`를 입력하면 직전 상태로 되돌아옴
- git merge



## terminal tip

- `cd <tab> <tab> ` : cd 명령어를 수행할 수 있는 목록



## Merge의 3가지 가능성

1. Fast Forward merging

   - 합쳐

2. Auto merging

   - 스무스하게 두 개의 다른 내용 파일이 합쳐짐
   - vs code, pycharm 등에서 실행시 자동 메세지 생성
   - git bah에서 실행시 vim 편집기로 메세지 삽입해야 함

3. Manual merging

   - auto merging 실패

   ```
   <<<<<<< HEAD
   odka
   =======
   aaaaa
   >>>>>>> b
   ```

   - 직접 지워야 함
   - (master|MERGING)가 떠서 충돌 처리 전에는 commit 못함
   - git hub에서 resolve complete나 open in web ide 등으로 해결할 수 있음



## vim

- `vim <파일 이름>`: vim 편집기로 파일 이름 열기
  - `$ git commit`만 입력했을 때 등 자동 실행될 때가 있음
    - commit 메세지를 여러 줄로 쓸 때 유용
- `i`: 파일 삽입 모드
- `esc`: 일반 모드
- `:wq` `:x`: 저장 후 vim 편집기 종료
- `:q!`: 강제 종료(수정 사항 반영 안 됨)



## 되돌리기

```bash
// package.json 파일을 마지막으로 pull 받았을 때로 돌려 놓는다
$ git checkout -- package.json
```

