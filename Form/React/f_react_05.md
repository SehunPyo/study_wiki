<h1-costom># React // 화면에 여러 컴포넌트 사용</h1-costom>

---

## 1. 프로젝트 폴더 구조 확인

- "Node/npm", "개발환경설정" 메뉴를 참고하여 설치 후 진행

프로젝트 폴더 구조 예시

```
my-react-app
    > node_modules/
    > public/
    > src/
        >> components/
            >>> TopBar.jsx
            >>> SideBar.jsx
            >>> Content.jsx
        >> App.css
        >> App.jsx
        >> index.css
        >> main.jsx
    > index.html
    > package.json
    > ...
```

---

## 2. 각 컴포넌트 생성

#### 1) 컴포넌트 파일 생성(src/components/ 안에 새로운 파일 생성)

<br>

<txtcolor-blue>예시)  </txtcolor-blue>

- <label-blue>상단 바</label-blue> : src/components/TopBar.jsx
- <label-blue>사이드 바</label-blue> : src/components/SideBar.jsx
- <label-blue>메인 콘텐츠</label-blue> : src/components/Content.jsx

```js
상단바 [TopBar.jsx]


// 1. 'TopBar'라는 이름의 함수형 컴포넌트 생성
function TopBar() {
  return <header>상단 메뉴 바 (TopBar.jsx)</header>;
}


// 2. 다른 파일에서 사용할 수 있도록 내보내기
export default TopBar;
```

```js
사이드바 [SideBar.jsx]


function SideBar() {
  return (
    <nav>
      <ul>
        <li>메뉴1</li>
        <li>메뉴2</li>
        <li>(SideBar.jsx)</li>
      </ul>
    </nav>
  );
}

export default SideBar;
```

```js
메인 콘텐츠 [Content.jsx]


function Content() {
  return (
    <main>
      <h2>메인 콘텐츠입니다.</h2>
      <p>(Content.jsx)</p>
    </main>
  );
}

export default Content;
```

---

## 3. 메인 화면에서 컴포넌트 불러오기
```js
// 1. 각 컴포넌트를 해당 파일 경로에서 가져오기
import TopBar from './components/TopBar';
import SideBar from './components/SideBar';
import Content from './components/Content';
import './App.css'; // 화면 레이아웃을 위한 CSS 파일

// 2. App 컴포넌트 (작업대)
function App() {
  // 3. 컴포넌트들을 조립하여 화면에 렌더링할 JSX 반환
  return (
    <div className="container">
      {/* TopBar 컴포넌트 렌더링 */}
      <TopBar />
      <div className="wrapper">
        {/* SideBar 컴포넌트 렌더링 */}
        <SideBar />
        {/* Content 컴포넌트 렌더링 */}
        <Content />
      </div>
    </div>
  );
}

// 4. App 컴포넌트 내보내기
export default App;
```

---

## 4. CSS로 스타일 추가하기
JSX만으로는 컴포넌트들이 화면에 나열될 뿐, 원하는 위치에 배치되지 않기 때문에, CSS를 사용하여 각 컴포넌트의 위치와 모양을 지정한다.

```css
/* 전체 컨테이너 */
.container {
  display: flex;
  flex-direction: column;
}


/* 사이드바와 콘텐츠를 감싸는 래퍼 */
.wrapper {
  display: flex;
  flex-direction: row;
}


/* 각 컴포넌트의 영역을 구분하기 위한 간단한 스타일 */
header, nav, main {
  border: 1px solid #ccc;
  padding: 1rem;
  margin: 0.5rem;
}


nav {
  width: 150px;
}


main {
  flex-grow: 1; /* 남은 공간을 모두 차지하도록 설정 */
}
```