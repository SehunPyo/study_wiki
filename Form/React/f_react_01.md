<h1-costom># React // Node.js / npm</h1-costom>

---

## 요약

| 항목           | 역할                 | 예시                 |
| ------------ | ------------------ | ------------------ |
| Node.js      | JS 실행 환경 (런타임)     | node server.js     |
| npm          | 패키지(라이브러리) 관리 도구   | npm install axios  |
| package.json | 프로젝트 설정 파일         | dependencies 목록 포함 |
| npm install  | dependencies 자동 설치 | node_modules 생성    |

---

## Node와 npm을 사용하는 이유
: 코드에 없는 기능(예: 웹서버, DB연결, 암호화 등)을 다른 개발자들이 만들어 둔 라이브러리(패키지)로 불러와 효율적으로 사용하기 위함  

```bash
- 설치 : npm install
- 삭제 : npm uninstall
- 업데이트 : npm update
- 실행 : npm run start
```

---

## 1. Node.js
: 자바스크립트를 브라우저 밖에서도 실행할 수 있게 해주는 런타임 환경  

1) 원래 JavaScript는 웹 브라우저 안에서만 동작  
2) 하지만 Node.js를 사용함으로 서버나 로컬 환경에서도 JavaScript를 실행할 수 있음  

```py
예 )

# app.js파일을 브라우저 없이 실행
node app.js 
```

---

## 2. npm
: Nopde.js 용 패키지 관리자 (Node Package Manager)  

1) Node.js를 설치하면 자동으로 함께 설치됨  
2) 오픈소스 라이브러리(React, Express, Lodash등 )(패키지)를 쉽게 설치하고 관리함  

---

## 3. npm install
: 프로젝트에 필요한 라이브러리를 설치하는 명령어  

#### 3-1) 어떻게 설치할까?
1. 보통 Node 프로젝트 폴터에는 <label-red>package.json</label-red> 이라는 파일이 존재  
2. 그 안에는 프로젝트에서 사용할 라이브러리 목록이 들어있다  

```json
예 )

{
  "dependencies": {
    "react": "^18.3.0",
    "axios": "^1.7.5"
  }
}
```
3. 이 상태에서 터미널에 <label-blue>npm install</label-blue>를 입력 :  
    3-1. npm이 <label-red>package.json을 읽음</label-red>  
    3-2. react, axios 같은 라이브러리를 자동으로 설치
    3-3. 설치 결과는 <label-orange>node_modules</label-orange> 폴더에 들어감  

