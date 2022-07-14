+ 게임 하나라도 완전히 완성하는 것이 중요함



## User

- UserExp, UserLevel
  - Exp가 결정되면 Level이 결정되니 UserLevel 컬럼은 필요 없다
- User logout data
  - 유저가 로그아웃을 누른게 아니라 창을 끈 경우는 시간을 제대로 알 수가 없다
  - 현재 접속 여부도 알 수 없음...
- User Game date
  - 정규화
    - GameRoom과 관련성이 높음
    - GameRoom과 조인해 유저 참석 데이터로 알 수 있음



## GameRoom

- GameRoomLocked
  - 게임 룸의 공개 타입
  - 컬럼 명이 정확하지 않음
- GameRoomMemberCnt
  - 정규화
  - Users와 join을 통해 알 수 있음

- GameRoomSerialNum
  - 방코드 검색으로 들어갈 수 있는 코드 값(문자)
  - Varchar 형식이므로 PK로는 부적절함



## UserFriends

- FriendAccept
  - Accept만 보낸 경우
  - 받은 유저가 Accept한 경우
  - 받은 유저가 Deny한 경우
  - Ture, False, Null로 표현 가능

