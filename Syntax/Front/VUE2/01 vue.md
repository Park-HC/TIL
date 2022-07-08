# Vue

## vue란?

- 사용자 인터페이스를 만들기 위한 진보적인 JS 프레임워크
- 현대적 tool과 다양한 라이브러리를 통해 SPA(Single Page Application) 완벽 지원



### SPA란?

- 단일 페이지 어플리케이션
- 현재 페이지를 동적으로 렌더링하여 사용자와 소통하는 웹 애플리케이션
- 최초에 페이지만 다운로드, 이후 동적으로 DOM을 구성하는 단일 페이지 구성
- UX 향상
- 동작 원리 일부가 CSR 구조 따름



### CSR이란?

- Clinent Side Rendering
- 서버가 아니라 클라이언트에서 화면을 구성
- 처음엔 뼈대(데이터를 제외한 각종 리소스)를 받고 브라우저에서 동적으로 DOM 그림(클라이언트 데이터 요청)
- 서버와 클라이언트 간 트래픽이 감소하며 사용자 경험 증가
- SSR에 비해 전체 페이지 최종 렌더링 시점이 느려지며 SEO(검색 엔진 최적화)에 어려움 발생



### SSR이란?

- Server Side Rendering
- 서버에서 클라이언트에게 보여줄 페이지를 모두 구성하여 전달
- JS 이전 전통적인 렌더링 방식



### SEO란?

- Search Engine Optimization
- 검색엔진이 자료 수집하고 순위에 매기는 방식에 맞게 웹페이지 구성해 검색 결과의 상위에 노출될 수 있도록 하는 작업
- 인터넷 마케팅의 일종으로 타 사이트에서 인용되는 횟수를 늘리는 방향으로 최적화
- Vue, React 등은 이미 선별적 SEO 대응 기능이 있음



## Vanilla JS와 비교

- Vanilla JS는 한가지 정보를 수정한다면 이와 연관된 모든 코드를 수정해야 함
- Vue.js는 DOM의 필요한 정보를 DATA로 관리하며 여기서 data만 수정하면 자동으로 DOM 상 연관된 코드들이 수정됨



## MVVM Pattern

### Model

- js의 object
- `object === {key : value}`
- Model은 Vue Instance 내부에서 data란 이름으로 존재
- 이 data의 수정으로 View(DOM)가 반응

### View

- js의 DOM(HTML)
- data의 수정으로 바뀜

### ViewModel

- 모든 Vue Instance
- View와 Model 사이 Data와 DOM에 관련된 모든 일 처리