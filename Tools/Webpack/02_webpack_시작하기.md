# 환경 세팅

## 설치

```bash
$ npm init -y
$ npm install webpack --save-dev
$ npm install --save-dev webpack-cli  # 웹팩 v4 이후 버젼일 경우 CLI도 설치해야 함

$ .\node_modules\.bin\webpack -v  # 설치 성공 확인
```



## js 설정 파일

- Webpack을 만들 최상위 경로에 webpack.config.js 를 만들어야 함

```javascript
module.exports={
    entry : './src/test.js',
    output: {
        filename : 'bundle.js',
        path : path.resolve(__dirname + '/build')
    },
    mode : 'none'
}
```

| 구조    | 기능                                                         |
| ------- | ------------------------------------------------------------ |
| path    | 파일의 경로를 다루고 변경하는 유틸리티                       |
| output  | build 결과를 저장할 경로                                     |
| entry   | build의 대상이 될 파일                                       |
| Plug-In | build 된 bundle 파일을 동적으로 특정 html 페이지에 추가 할 수 있으며<br />build 시에 js, css, html 등의 파일을 난독화 및 압축 시킬 수 있음 |



## Loader

- js와 같이 하나의 bundle로 만들 수 있는 Loader

### Css/SaSS

```bash
$ npm install style-loader css-loader --save-dev
```

```javascript
// webpack.config.js

module.exports = {
   entry : './src/test.js',
    output: {
        filename : 'bundle.js',
        path : path.resolve(__dirname + '/build')
    },
    mode : 'none',
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          'style-loader',
          'css-loader'
        ]
      }
    ]
  }
};
```

- 번들링 해줄 loader 파일을 npm 패키지로 설치 후 정의하면 됨



