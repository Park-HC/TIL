## 1.  app 설치

## 2. 프로젝트 root 밑에 Dockerfile 생성

- `Dockerfile` 대소문자까지 똑같아야 실행됨

  ```bash
  # build stage
  FROM node:lts-alpine as build-stage
  WORKDIR /app
  COPY package*.json ./
  RUN npm install --production  # vue-cli 문제가 발생할 경우 RUN npm install로 함
  COPY . .
  RUN npm run build
  
  # production stage
  FROM nginx:stable-alpine as production-stage
  COPY --from=build-stage /app/dist /usr/share/nginx/html
  EXPOSE 80
  CMD ["nginx", "-g", "daemon off;"]
  ```

  

## 3. `docker image build`

```bash
$ docker build -t vue-app
```

- Dockerfile 위치에서 실행

```bash
$ docker images
```

- image 확인



## 4. `docker container` 실행

```bash
$ docker run -it -p 8080:80 --rm --name --name vue-app-1 vue-app
# -t나 -r에 대해 오류 발생 가능 그 경우, 일단 해당 명령어를 제거(-it -> -i, --rm -> --m)
```



## 5. Vue.js app에 접속하고 확인



- https://jeomn.tistory.com/38

- https://kdeon.tistory.com/6