<h1-costom># React // React 개발환경 설정 및 시작</h1-costom>

---

## 1. Node.js 설치 여부 확인

터미널 또는 PowerShell에서 다음 명령으로 node, npm 버전 확인
```py
node -v
npm -v
```

---

## 2. Vite로 리액트 프로젝트 생성

터미널에 다음 명령으로 프로젝트 폴더 생성
```py
# Vite 최신 버전으로, React 템플릿 기반의 새로운 프로젝트를 my-react-app 폴더에 생성

npm create vite@latest my-react-app -- --template react
```

<label-blue>1</label-blue> npm create vite@latest
- npm : Node.js 패키지 관리자 (Node 설치 시 함께 제공)
- create vite : Vite 프로젝트 생성 도구 실행
- @latest : 최신 버전을 사용하겠다는 의미

<label-blue>2</label-blue> my-react-app
- 새로운 프로젝트(폴더)의 이름

<label-blue>3</label-blue> -- --template react
- -- : npm 명령어의 옵션과 create-vite 옵션 구분
- --template react : Vite의 템플릿 중 React를 사용

<br>

#### 터미널에 표시되는 Yes or No 메세지의 의미

##### 2-1. <txtcolor-blue>Use rolldown-vite (experimental)?</txtcolor-blue>  
: Vite에서 채택하려는 차세대 번들러인 Rolldown(러스트 기반 번들러)를 사용해보겠냐는 의미.  
- Vite는 개발 서버에서는 빠른 ES모듈 기반 접근방식을 쓰고, 빌드(프로덕션)에서는 현재는 Rollup를 내부적으로 활용
- Rolldown은 ‘러스트(Rust)로 새로 만든 번들러’로, Rollup과 호환되면서 더 빠르고 효율적인 빌드가 목표

##### 2-2. <txtcolor-blue>Install with npm and start now?</txtcolor-blue>
: <label-blue>create-vite</label-blue> 명령으로 Vite가 프로젝트를 생성하면, 폴더 구조만 만들어지고 아직 node_modules(패키지 설치)는 안되어있는 상태.
- npm install, npm run dev를 자동으로 진행하겠냐는 의미

---

## 3. 프로젝트 폴더로 경로 이동

터미널에 다음 명령으로 프로젝트 폴더로 경로를 변경 (2-2에서 yes과정을 하지 않은 경우 진행)  
```
cd my-react-app
```
- my-react-app을 생성한 프로젝트 폴더 이름으로 변경  

---

## 4. 패키지 설치

터미널에 다음 명령으로 npm 패키지 설치 <label-gray>(2-2에서 yes과정을 하지 않은 경우 진행)</label-gray>  
```
npm install
```

---

## 5. 서버 실행

터미널에 다음 명령으로 npm 서버 실행
```
npm run dev 또는 npm start
```
- npm start는 package.json파일의 "stripts"에 "start": "vite" 형식이 작성되어 있어야 함