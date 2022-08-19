# WebRTC

## 개요

- 서버를 최대한 거치지 않고 P2P로 브라우저나 단말 간에 데이터를 주고받는 기술의 웹 표준
- WebRTC는 표준임과 동시에 표준을 구현한 오픈소스 프로젝트의 이름
- 웹에서 실시간 미디어 스트림을 송수신할 수 있는 유일한 표준
- 유일한 P2P 표준



## 특징

- 웹에서 사용할 수 있는 유일한 P2P 기술
  - 각각의 기기가 서버 도움 없이 연결되기 위해 연결을 도와주는 서버(Signaling)과 P2P 연결이 불가능한 상황을 대비한 릴레이 서버(TURN)가 필요
- UDP 기반 스트리밍 기술

- 다양한 활용
  - 1:1 방식
    - 카카오톡 보이스톡 등 전화 기능
    - 영어 전화 및 의료 상담
  - 1:N 방송 서비스
    - 낮은 지연시간으로 생방송 서비스에 이용
    - 대량 접속 환경에서도 낮은 지연 시간을 보장
  - N:N 회의형 서비스
    - 화상회의
    - 클럽하우스 서비스



## 어려움

### 네트워크 환경에 따른 품질의 불확실성

- UDP 기반 RTP 프로토콜을 사용해 내부에서 품질 보정을 하지만 보장까지 하지는 않음
  - 음질 등 사용자 간 품질 평가 차이가 큰 분야는 이에 대한 조사 또한 필요함
- 네트워크가 불안정한 모빌리티 환경 또한 감안해야 함
  - 문제 재현의 어려움
  - 논리적 코드만으로 상황 유추하기 어려움



### 고난이도의 미디어 처리 영역

```
Video/Audio Input => 미디어 편집 => 보안
=> 송출 => 시그널링/보안 => Origin			// WebRTC 관여
=> 믹싱 => 녹화 => 트랜스 코딩
=> Edge => 수신							// WebRTC 관여
```

- WebRTC는 클라이언트에서 미디어에 변화를 많이 줌
- 미디어를 다루는 엔지니어, 모바일 플랫폼의 입출력 미디어 장치에 대한 경험을 가진 엔지니어도 필요함
- 채팅이나 화면효과, 그외 사용자의 여러가지 이벤트 등을 실시간으로 전파하고 공유할 수 있는 서버가 꼭 갖춰져야 함



### 대용량 처리 및 클라우드

- WebRTC 미디어 서버는 WebRTC 기반의 미디어 스트림을 중개 및 분배하는 역할을 하는 서버가 필요





## CPaaS

- WebRTC 응용 서비스에서 성공을 결정하는 핵심은 콘텐츠
- 즉, WebRTC 같은 매우 전문화된 기술은 클라우드 기업에 맡기는 CPaaS 방법을 활용 가능
