# Width, Height Auto

> https://oursmalljoy.com/css-width-auto-height-auto-%EA%B8%B0%EB%B3%B8%EA%B0%9C%EB%85%90-%EC%9E%98%EB%AA%BB-%EC%83%9D%EA%B0%81%ED%95%98%EA%B3%A0-%EC%9E%88%EB%8A%94-%EA%B2%83%EB%93%A4/

## 개요

- 내용물의 크기에 맞혀 자동 크기 조절이 된다는 의미
- width나 height 값을 설정할지 않았을 때 기본적으로 auot 속성 값이 들어감
- 하지만 block 형식에서는 자동 조절되지 않음
  - iniline 요소는 크기 설정할 수 없어서 의미 ㅇ벗음



## 각 포지션에서의 의미

- Inline-Block에서는 자식 요소들 크기에 자동으로 맞춤
- Block에서는 height는 auto, width는 가상의 내용물 너비에 맞춰서 적용됨



## top

- 부모요소가 height: auto면 자식요소의 top: %를 사용할 수 없음
- 가로 방향으로는 특정한 값이 설정되지만 세로 방향으로는 특정한 값이 설정되지 않음
  - 따라서 top의 경우 부모 요소가 특정한 height 값을 가지고 있지 않은 것으로 받아들여져 좌표를 계산할 수 없음



# Overflow

- 요소 내 컨텐츠가 너무 커 요소 내에서 모두 보여주기 힘들 때 그것을 어떻게 보여줄지를 지정
- 기본적으로 컨텐츠를 포함하고 있는 요소의 크기가 고정되어 있지 않다면 컨텐츠를 모두 포함할 수 있도록 요소의 크기가 커짐(width, height: auto)
- 크기가 조정되어 있다면 overflow 프로퍼티에 지정된 값에 따라 보여짐



## 종류

1.  visible
   - 기본 값
   - 넘칠 경우 컨텐츠가 상자 밖으로 보여짐
2. hidden
   - 넘치는 부분은 잘려서 보여지지 않음
3. scroll
   - 스크롤바가 추가되어 스크롤 할 수 있음
4. auto
   - 컨텐츠 량에 따라 스크롤바를 추가할지 자동으로 결정

5. initial
   - 기본값으로 설정
6. inherit
   - 부모 요소의 속성값을 상속받음



# Position

## static

- 기본값
- HTML 문서 상 원래 있어야 하는 위치에 배치
- top, left, bottom, right 등 속성값은 무시됨



## relative

- 요소를 원래위치(static) 기준으로 상대적으로 배치해줌



## absolute

- static이 아닌 첫번째 상위 요소를 기준으로 설정
  - static이 아닌 요소가 없다면 최상위의 body 요소가 배치 기준이 됨
- 보통 부모요소를 relative로 설정하고 그것을 기준으로 top, left 등을 쓸 때 사용
- absolute로 쓰인 요소는 다른 요소들과 더 이상 상호작용하지 않음(static에서 없는 요소로 치고 넘어감)



## fixed

- 화면 특정 위치에 고정
- 배치 기준은 viewport(브라우저 전체화면)



## sticky

- fixed에 스크롤링 효과가 첨가됨