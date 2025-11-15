<h1-costom># React // 새로운 화면 추가</h1-costom>

---

## 1. 프로젝트 폴더 구조 확인

- "Node/npm", "개발환경설정" 메뉴를 참고하여 설치 후 진행

프로젝트 폴더 구조 예시
```
my-react-app
    > node_modules/
    > public/
    > src/
        >> assets/
        >> App.css
        >> App.jsx
        >> index.css
        >> main.jsx
    > index.html
    > package.json
    > package-lock.json
    > .gitgnore
    > README.md
    > vite.config.js
```

---

## 2. 메인화면 수정

Vite + React 서버를 실행하면 보이는 화면은 <label-gray>src/App.jsx</label-gray> 파일  

#### <txtcolor-blue>Main.jsx가 있지만 App.jsx가 메인화면이 되는 이유</txtcolor-blue>  

<br>

1) Main.jsx는 컴퓨터의 본체, App.jsx는 화면의 역할을 한다. 배경화면을 바꾸고 싶다면 화면 설정을 바꾸면 되는 것과 같다.  
2) 메인 화면 외 다른 화면을 추가하고 싶으면, App.jsx에 연결하면 된다. 바탕화면에 아이콘을 추가하는 것과 같다.

- Main.jsx = 전역 Provider/Router/상태관리 도입 • 교체 등의 설정을 할 때 건드림
- App.jsx = 레이아웃 수정, 페이지 추가 및 전환 로직 등 '보이는 것'을 작업할 때 건드림

---

## 3. 새로운 페이지(컴포넌트) 생성

#### 3-1. 새로운 화면이 될 파일 생성 (src/ 안에 새로운 파일을 생성)
```
src/Home.jsx
```

#### 3-2. 새로운 화면의 내용 작성 (Home.jsx)

```py
# 1. 'Home'이라는 함수형 컴포넌트 생성
function Home() {
  return <h2>홈 화면입니다 🏠 (Home.jsx)</h2>;
}

# 2. 'Home' 내용 내보내기
export default Home;
```

#### 3-3. App.jsx에서 불러오기

```py
# 1. Home 컴포넌트를 './Home' 파일에서 가져오기
import Home from './Home';

# 2. App이라는 이름의 함수형 컴포넌트 생성 (애플리케이션의 최상위 컴포넌트 역할)
function App() {
  # 3. 컴포넌트가 화면에 렌더링할 JSX(JavaScript XML)를 반환
  return (
    <>
      <h1>홈 화면 입니다. (App.jsx)</h1>
      # 4. 위에서 가져온 Home 컴포넌트 렌더링
      <Home />
    </>
  );
}

# 5. App 컴포넌트를 다른 파일에서 가져와 사용할 수 있도록 기본(default)으로 내보내기
export default App;
```
