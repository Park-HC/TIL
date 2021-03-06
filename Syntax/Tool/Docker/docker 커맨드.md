# docker 커맨드

## 설치 확인

```bash
$ docker version
```





## 생성

```bash
# jenkins 생성
$ docker run -d -p 9090:8080 -p 50000:50000 -v /var/jenkins:/var/jenkins_home -v /var/run/docker.sock:/var/run/docker.sock --name jenkins -u root jenkins/jenkins:lts-jdk11
```



## 컨테이너

```bash
# 컨테이너 로그 확인
$ docker logs <container_id or names>

# 동작 중인 컨테이너 확인
$ docker ps

# 정지된 컨테이너 확인
$ docker ps -a

# 컨테이너 삭제
$ docker rm [컨테이너id]

# 여러개 삭제
$ docker rm [컨테이너id], [컨테이너id]

# 컨테이너 모두 삭제
$ docker rm `docker ps -a -q`
```



## 이미지

```bash
# 현재 이미지 확인
$ docker images

# 이미지 삭제
$ docker rmi [이미지id]

# 컨테이너를 삭제하기 전 이미지를 삭제할 경우
$ docker rmi -f [이미지id]
```





## run

```bash
$ docker run (<옵션>) <이미지 식별자> (<명령어>) (<인자>)
```

### 옵션

| 옵션  | 설명                                                   |
| ----- | ------------------------------------------------------ |
| -d    | detached mode<br />백그라운드 모드                     |
| -p    | 호스트와 컨테이너의 포트를 연결(포워딩)                |
| -v    | 호스트와 컨테이너의 디렉토리를 연결(마운트)            |
| -e    | 컨테이너 내에서 사용할 환경변수 설정                   |
| -name | 컨테이너 이름 설정                                     |
| -rm   | 프로세스 종료시 컨테이너 자동 제거                     |
| -it   | -i와 -t를 동시에 사용한 것으로 터미널 입력을 위한 옵션 |
| -link | 컨테이너 연결[컨테이너명:별칭]                         |





- https://subicura.com/2017/01/19/docker-guide-for-beginners-2.html
