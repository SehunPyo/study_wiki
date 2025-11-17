<h1-costom># React // React 문법</h1-costom>

---
## 시작 전...

#### ★ 중괄호 {} 를 이용한 표현식 ★

JSX의 내부에 {}를 작성하는 것은, "이 안에 있는 코드는 JavaScript이다." 라는 의미로 사용한다.  
변수, 함수 호출, 계산식 등 결과적으로 하나의 값인 JavaScript 표현식이라면 무엇이든 넣을 수 있다.  

---

## console 사용

#### 1) 진행 로그
```js
// 기본 구문
console.info(값);


// 예시
console.info('[Auth] 로그인 시작', { userId }); // 목적: 흐름의 시작/단계 표시 (문제 없음, 참고용)
```

#### 2) 콘솔에 값을 출력
```js
// 예시
console.log(값);


// 출력 값의 타입 확인 예시 (typeof를 앞에 작성)
console.log(typeof time, time)
```

#### 3) 콘솔에 의도적으로 주의 등 출력
```js
// 기본 구문
console.warn(내용);


//예시
// 1. 폴백(대체값 사용)
const locale = user.locale ?? 'ko-KR';
if (!user.locale) console.warn('[i18n] locale 미지정 → ko-KR로 대체');

// 2. 부분 실패(전체는 계속)
const results = await Promise.allSettled(tasks);
if (results.some(r => r.status === 'rejected')) {
  console.warn('[Batch] 일부 항목 실패, 나머지 진행', results);
}

// 3. 성능 임계 접근
if (elapsed > 300 && elapsed < 1000) {
  console.warn(`[Perf] 응답 지연 경고: ${elapsed}ms`);
}
```

#### 4) 실패/중단/error 시 출력
```js
// 기본 구문
console.error(값);


// 예시
try {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`HTTP ${res.status}`);
} catch (e) {
  console.error('[API] 요청 실패', e); // 사용자 영향/중단 상황
}
```

#### 5) 콘솔에 주석 로그 출력
```js
// [예시] "유저 목록 가져오기" 작업 하나를 콘솔에 (시작~끝, 시간, 중간 문제 여부, 최종 데이터) 형태로 기록한다. 

// ▼ 콘솔에서 접힌 블록 시작(한 덩어리로 묶어서 보기 좋게)
console.groupCollapsed('[GET /users]');

// 작업 시작 시간 기록(끝에서 걸린 시간 자동 계산됨)
console.time('[GET /users]');

// 지금 어떤 값으로 요청하는지 남김
console.info('요청 시작', { page, limit });

try {
  // 1) 서버에 요청 보냄
  const res = await fetch(url);

  // 2) 응답이 정상인지 확인 (HTTP 상태코드: 200~299면 정상)
  if (!res.ok) {
    // 400번대: 내가 보낸 값/상태가 부족하거나 잘못된 경우가 많음
    // → "지금은 계속할 수는 있지만 정상은 아님"이라서 경고로 남김
    if (res.status < 500) {
      console.warn('정상 아님(400대) → 계속 진행', res.status);
      // 필요하면 여기서 기본값으로 처리(폴백) 같은 걸 해도 됨
    } else {
      // 500번대: 서버 쪽 문제 → 보통 계속 못 함, 에러로 처리
      throw new Error('서버 오류');
    }
  }

  // 3) 응답 본문을 자바스크립트에서 쓰기 좋게 바꿈
  //    (JSON 텍스트 → 객체/배열로 "변환")
  const data = await res.json();

  // 4) 우리가 기대한 모양인지 가볍게 확인 (여기선 “배열” 기대)
  if (!Array.isArray(data)) {
    // 모양 이상하지만 화면을 완전히 망치지 않도록
    // 안전한 값(빈 배열)로 바꿔서 계속 진행
    console.warn('데이터 모양이 예상과 다름 → 빈 목록으로 대체');
    return [];
  }

  // 5) 결과를 표로 보여주기(콘솔에서 한눈에 확인하기 좋음)
  console.table(data);

} catch (e) {
  // 6) 위에서 에러가 나면 여기로 떨어짐 → 실패 기록
  console.error('요청 실패', e);

} finally {
  // 7) 걸린 시간 출력(위 time과 짝)
  console.timeEnd('[GET /users]');
  // ▲ 접힌 블록 닫기
  console.groupEnd();
}
```

---

## 1. JSX (JavaScript XML)의 개념

<label-blue>1-1</label-blue> JSX는 JavaScript를 확장한 문법으로, UI가 어떻게 보일 것인가를 직관적으로 표현할 수 있게 한다.  
<label-blue>1-2</label-blue> 브라우저는 JSX를 직접 이해하지 못하기 때문에 JSX가 실행되기 전, 바벨(Babel)이라는 도구를 사용하여,  
JSX를 브라우저가 이해할 수 있는 순수한 JavaScript(React.createElemet(...) 함수 호출) 형태로 변환한다.

```js
// JSX 코드 예시
const element = <h1 className="greeting">Hello, world!</h1>;


// 바벨이 변환한 JavaScript 코드 (실제 동작)
const element = React.createElement('h1', { className: 'greeting' }, 'Hello, world!');
```

---

## 2. 태그는 하나만 사용

JSX는 반드시 하나의 부모 요소로 감싸서 내보내야 하는 규칙이 있다.

```js
// 잘못된 예시

function App() {
  return (
    <h1>제목</h1>
    <p>내용</p> // <h1>과 <p>가 동등한 레벨에 있어 에러 발생
  );
}
```

```js
// 올바른 예시 1) 가장 일반적인 해결 방법이지만, 불필요한 div 태그가 실제 HTML 구조에 추가될 수 있음.

function App() {
  return (
    <div>
      <h1>제목</h1>
      <p>내용</p>
    </div>
  );
}
```

```js
// 올바른 예시 2) 실제 DOM에는 아무런 흔적을 남기지 않고 여러 요소를 그룹화하고 싶을 때 사용하는 권장 방식.
import React from 'react'; // Fragment를 사용하려면 import 필요

function App() {
  return (
    <React.Fragment> // 또는 간단히 <>
      <h1>제목</h1>
      <p>내용</p>
    </React.Fragment> // 또는 </>
  );
}

// 혹은

function App() {
  return (
    <>
      <h1>제목</h1>
      <p>내용</p>
    </>
  );
}
```

---

## 3. 변수, 계산식(연산)
<txtcolor-blue>리액트에서 변수를 선언할 때는 중괄호 안에 자바스크립트를 작성하고, 사용할 때는 { }안에 변수명을 넣는다.</txtcolor-blue>

1) 리액트의 컴포넌트 함수 안에서 만드는 변수는 모두 자바스크립트 변수이다.  
2) 변수를 선언할 때는 <label-blue>const</label-blue> 혹은 <label-blue>let</label-blue> 으로 선언한다.  

#### ★ const와 let의 차이 ★

<label-red>const</label-red> : 한 번 값을 정하면 그 변수명에는 다른 값을 다시 넣을 수 없음

```js
const age = 31;
age = 32;  // ❌ 에러 (재할당 불가)
```

```js
const user = { name: "솔" };
user.name = "또리"; // ✅ 가능 (객체 안의 내용은 수정 가능)
```

<label-red>let</label-red> : 값을 정하더라도 다른 값으로 변경 가능

```js
let count = 0;
count = count + 1; // ✅ 재할당 가능
```

하지만 계속해서 바뀌는 값(입력 값, 카운트 등)은, let으로 작성하면 화면에서 바뀌지 않기 때문에 <label-blue>useState</label-blue>로 관리해야 함.

```js
// 나쁜 예 (변수는 바뀌지만 화면은 그대로)
let count = 0;

function App() {
  function handleClick() {
    count = count + 1;  // 렌더링 안 됨
  }

  return <button onClick={handleClick}>{count}</button>;
}
```

<br>
<br>


#### 변수 사용 방법

```js
// 예시

function App() {

  // 변수 선언
  const 이름 = "홍길동";
  const 가격 = 1500;
  const 수량 = 3;

  return (
    <>

      // 변수 사용
      <h1>이름: {이름}</h1>
      <p>가격 : {가격}원</p>
      <p>수량 : {수량}개</p>
      <p>총 금액: {가격 * 수량}원</p>

    </>
  );
}

export default App;
```

3) JSX에서 { } 안에는 <label-red>값을 만들어내는 표현식</label-red>만 사용할 수 있다.  

```js
// 사용 가능
- 변수 : {name}, {age} 등
- 계산식 : {price * count}, {a + b}, {num + "살"} 등
- 함수 호출 결과 : {getUserName()}, {format(price)} 등
- 삼항 연산자 : {isLogin ? "로그인완료" : "로그인필요"} 등
- 배열 map 결과 : list.map(...) [결과가 엘리먼트 배열이면 그대로 렌더링]

// 사용 불가능
- if (...){...}, for (...){...} 등
: 문장을 직접적으로 사용 불가. JSX밖에서 미리 계산해두거나 삼항/논리연산자로 바꿔서 사용 필요
```

---

## 4. 함수

<txtcolor-blue>JSX 안에서 <b>{함수이름()}</b>처럼 함수를 호출하면, 그 함수가 <b>return한 값</b>이 화면에 표시된다.</txtcolor-blue>

1) 함수도 결국 자바스크립트 코드이므로, 컴포넌트 함수 안/밖에서 만들 수 있다.  
2) JSX에서 {myFunction()}처럼 호출하면, **그 결과(리턴 값)**가 그대로 출력된다.  
3) 화면에 쓸 함수는 가능한 한 <label-blue>“값을 계산해서 돌려주는 것”</label-blue> 위주로 만든다. (console.log 전용 함수는 화면에 안 나옴)

```js
// 예시

function App() {

  const 이름 = "홍길동";
  const 가격 = 1500;
  const 수량 = 3;

  // 1) 총 금액을 계산해서 돌려주는 함수
  function getTotalPrice() {
    return 가격 * 수량;
  }

  // 2) 문장을 만들어서 돌려주는 함수
  function getMessage() {
    return `${이름}님의 총 금액은 ${getTotalPrice()}원입니다.`;
  }

  return (
    <>
      <h1>이름: {이름}</h1>
      <p>가격: {가격}원</p>
      <p>수량: {수량}개</p>

      {/* 함수 호출 결과 사용 */}
      <p>총 금액: {getTotalPrice()}원</p>
      <p>{getMessage()}</p>
    </>
  );
}

export default App;
```

```js
// 사용 가능 (모두 "값을 만들어내는 표현식")
{getUserName()}
{formatPrice(가격)}
{makeTitle(user)}
{isLogin() ? "로그인완료" : "로그인필요"}

// 주의
// 화면에 보여줄 자리가 아닌데 console.log만 하는 함수 호출 → 화면에는 아무것도 안 보임
// 너무 복잡하고 무거운 계산은 JSX 안에서 직접 쓰지 말고,
// 위 예시처럼 함수/변수로 미리 분리하는 것이 좋다.
```

---

## 5. 화살표 함수
<txtcolor-blue>화살표 함수는 함수 표현식을 더 짧게 쓰는 문법이다.</txtcolor-blue>

#### 1. 기본 문법
```js
// 화살표 함수 사용 전
const double = function(x){
  return x * 2;
}

const result = double(3);
```

```js
// 화살표 함수 사용
const double = x => x * 2;

const result = double(3);
```

```js
// 매개변수 2개 이상 (괄호 필수)
const add = (a, b) => a + b;

const result = add(5, 3);
```



---

## 6. 조건부(삼항 연산자, && 연산자)

조건부 렌더링 : <txtcolor-blue>특정 조건에 따라 “보여줄지 말지”, “어떤 내용을 보여줄지” 결정하는 것</txtcolor-blue>  

#### 1) 삼항 연산자 사용 (조건 ? 값1 : 값 2) 
: 조건이 참이면 앞의 값, 거짓이면 뒤의 값을 선택해서 렌더링한다.

```js
// 문법

{조건 ? 값1 : 값 2}
```

```js
// 예시: 로그인 상태에 따라 다른 문구 보여주기

function App() {
  const isLogin = true;  // 또는 false
  const isAge = 31

  return (
    <>
      <h1>홈 화면</h1>
      <p>
        {isLogin ? "로그인 되었습니다 ✅" : "로그인이 필요합니다 🔐"}
        {isAge === 31 ? "나이가 많네요." : "나이가 적네요."}
      </p>
    </>
  );
}

export default App;
```

- <txtcolor-blue>{isLogin ? "로그인 되었습니다" : "로그인이 필요합니다"}</txtcolor-blue> 자체가 하나의 <label-red>값을 만들어내는 표현식</label-red>이기 때문에 JSX에서 사용 가능
- 두 가지 경우 중 반드시 하나는 보여줘야 할 때 사용하기 좋다.

---

## 7. 리스트(Map + Key)

<txtcolor-blue>배열 데이터를 화면에 표시하려면 각 항목을 JSX 엘리먼트로 변환한 배열을 반환해야 한다. 이를 위해 <label-blue>map</label-blue>을 사용하고, 각 항목에는 <label-blue>key</label-blue>라는 고유·안정 식별자를 지정한다.</txtcolor-blue>  

- <label-blue>map</label-blue> : array.map((item, index) => JSX) 형태로 데이터 → 엘리먼트 변환
- <label-blue>key</label-blue> : 리액트가 리스트 항목을 식별하기 위한 내부용 식별자(화면에 표시되지 않음)
- <label-red>중요</label-red> : key는 같은 리스트 범위 내에서 고유하고 렌더마다 바뀌지 않아야 함(가능하면 id 사용)

```js
// 문자열 배열 예시

function App() {
  const fruits = ["사과", "배", "귤"];

  return (
    <ul>
      {fruits.map((fruit) => (
        <li key={fruit}>{fruit}</li>
        // key={fruit}  : 식별자(내부용, 화면 X)
        // {fruit}      : 화면에 표시될 텍스트
      ))}
    </ul>
  );
}
export default App;
```

```js
// (권장) 객체 배열 + 고유 id

function App() {
  const users = [
    { id: 101, name: "솔" },
    { id: 102, name: "또리" },
  ];

  return (
    <ul>
      {users.map((u) => (
        <li key={u.id}>{u.name}</li> // 가장 안전한 key = 변하지 않는 id
      ))}
    </ul>
  );
}
export default App;
```

#### 1) 조건식 렌더링 (filter / 조건부)
```js

// 1) 먼저 걸러내기
{todos
  .filter((t) => !t.done)
  .map((t) => <li key={t.id}>{t.title}</li>)}


// 2) map 안에서 조건부
{todos.map((t) =>
  t.done ? null : <li key={t.id}>{t.title}</li>
)}
```

#### 2) 컴포넌트로 구분
```js
function TodoItem({ todo }) {
  return <li>{todo.title}</li>;
}

function App() {
  const todos = [{ id: 1, title: "코드" }, { id: 2, title: "테스트" }];

  return (
    <ul>
      {todos.map((t) => (
        <TodoItem key={t.id} todo={t} />   {/* ✔ key는 여기! */}
      ))}
    </ul>
  );
}
```

#### 3) 형제 요소 여러 개를 반환해야 할 때 (Fragment + key)
```js
function App() {
  
  const rows = [
    { id: "a1", name: "사과", price: 1000 },
    { id: "b2", name: "배",   price: 1500 },
  ];

  return (
    <ul>
      {rows.map((r) => (
        <React.Fragment key={r.id}>
          <li>{r.name}</li>
          <li>{r.price}원</li>
        </React.Fragment>
      ))}
    </ul>
  );
}
```

#### 4) 빈 목록 처리 (Empty State)
```js
function App() {
  const items = [];

  return (
    <>
      {items.length === 0 ? (
        <p>항목이 없습니다.</p>
      ) : (
        <ul>
          {items.map((it) => (
            <li key={it.id}>{it.name}</li>
          ))}
        </ul>
      )}
    </>
  );
}
```

---

## 8. 반복문 (for, while 등)

#### 1) for (횟수와 인덱스가 명확할 때)
```js
// 기본 문법
for (초기식; 조건식; 증감식) {
  // 반복 코드
}

// 예시
for (let i = 0; i < 3; i++) {
  console.log(i);
}

// i 출력
function result() {
  let last = null;
  fot (let i = 0; i < 3; i++) {
    last = i;
  }
  return last;
}
```

#### 2) while (조건이 참인동안 반복)
```js
// 기본 문법
while (조건식) {
  // 반복 코드
}
```

```js
// 예시
let n = 3;

while (n > 0) {
  console.log(n); // 3, 2, 1
  n--;
}
```

---

## 9. 인라인 스타일 (Inline Style)

<txtcolor-blue>JSX에서 style은 문자열이 아니라 자바스크립트 객체를 받는다. CSS 속성은 camelCase로 작성하고, 값은 문자열 또는 숫자(px 생략)를 쓴다.</txtcolor-blue>

#### 1) 기본 문법 (객체)

```js

export default function App() {
  return (
    <>
      {/* color: 문자열, fontSize: 숫자(= px) */}
      <p style={{ color: "tomato", fontSize: 16 }}>빨간 글자 16px</p>

      {/* 하이픈(-) → camelCase */}
      <div style={{ backgroundColor: "#f5f5f5", borderTopLeftRadius: 12 }}>
        배경색 + 좌상단 라운드 12px
      </div>

      {/* 여러 속성 한번에 */}
      <div style={{ padding: 12, marginTop: 8, textAlign: "center" }}>
        패딩/마진/정렬
      </div>
    </>
  );
}
```

#### 2) 변수로 관리
```js
export default function App() {
  const card = {
    padding: 16,
    backgroundColor: "#fff",
    border: "1px solid #e5e7eb",
    borderRadius: 12,
  };

  return <div style={card}>카드</div>;
}
```

#### 3) 동적 계산 (숫자/문자열 섞어 사용)
```js
export default function App() {
  const level = 3;
  const size = 12 + level * 2;                 // 숫자는 px 자동
  const w = `${level * 40}px`;                 // 문자열로 단위 직접 지정

  return (
    <div
      style={{
        fontSize: size,                         // 18px
        width: w,                               // "120px"
        transform: `translateX(${level * 5}px)`,
      }}
    >
      동적 스타일
    </div>
  );
}
```

#### 4) 조건부 스타일
```js
export default function App() {
  const isError = true;
  const isActive = false;

  return (
    <>
      <p style={{ color: isError ? "crimson" : "black" }}>에러 색상</p>
      <p style={{ textDecoration: isActive ? "underline" : undefined }}>
        활성일 때만 밑줄
      </p>
    </>
  );
}

// 주의 : style={{ color: isError && "red" }}처럼 &&를 쓰면 false가 들어갈 수 있음. 없애고 싶으면 undefined로 사용
```

#### 5) 스타일 함께 사용 (전개 연산자)

<label-blue>...값</label-blue> 형태로 배열/이터러블을 펼치거나, 객체의 속성을 펼쳐서 새 배열/객체를 만든다.

##### 5-1) 전개 연산자 사용
```js
const a = [1, 2];
const b = [3, 4];

// 합치기
const c = [...a, ...b];
console.log(c); // [1, 2, 3, 4]

// 복사하기(얕은 복사)
const copy = [...a];
console.log(copy); // [1, 2]
```

##### 5-2) 여러 전개 연산자 동시에 사용
```js
const base = { x: 1, y: 2 };
const extra = { y: 99, z: 3 };

// 병합(같은 키가 겹치면 뒤에 있는 값이 앞의 값을 덮어쓴다.)
const merged = { ...base, ...extra };
console.log(merged); // { x: 1, y: 99, z: 3 }
```

##### 5-3) 스타일 & 조건부 함께 사용
```js
export default function App() {
  const base = { padding: 8, borderRadius: 8 };
  const primary = { backgroundColor: "#2563eb", color: "#fff" };
  const danger = { backgroundColor: "#dc2626", color: "#fff" };

  const dangerMode = false;

  return (
    <button style={{ ...base, ...(dangerMode ? danger : primary) }}>
      버튼
    </button>
  );
}
```

##### 5-4) 여러 스타일 동시에 사용
```js
const base   = { padding: 8, borderRadius: 8 };
const sizeLg = { fontSize: 18, padding: 12 };
const primary= { backgroundColor: "#2563eb", color: "#fff" };

<button style={{ ...base, ...sizeLg, ...primary }}>세 가지 합침</button>
```



---

## 10. 숫자 포맷

<txtcolor-blue>숫자를 사람 읽기 형식으로 바꿀 때는 <label-blue>toLocaleString</label-blue> 또는 <label-blue>Intl.NumberFormat</label-blue>을 사용한다.</txtcolor-blue>

#### 1) 천 단위 구분 (로케일 자동)
```js
// 로케일은 설정된 환경으로 자동 지정된다.
(1234567.89).toLocaleString(); // "1,234,567.89"


// 로케일 변경 예시
(1234567.89).toLocaleString('ko-KR');
(1234567.89).toLocaleString('en-US');
(1234567.89).toLocaleString('de-DE');
```


#### 2) 소수 자리수 지정
- <label-blue>minimumFractionDigits</label-blue> : 최소 소수 자릿수를 지정. 자릿수가 모자라면 0을 채움
- <label-blue>maximumFractionDigits</label-blue> : 최대 소수 자릿수를 지정. 지정한 자리수 이상부터 반올림 적용

```js
// 소수점 이하를 2자리까지 표시하되, 부족하면 0을 채우고, 많으면 반올림한다.

(12.3456).toLocaleString('ko-KR', { minimumFractionDigits: 2, maximumFractionDigits: 2 }); // "12.35"
```
```js
// 예시

(12).toLocaleString('ko-KR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
// "12.00"  (부족하니 0 채움)

(12.3).toLocaleString('ko-KR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
// "12.30"  (부족하니 0 채움)

(12.3456).toLocaleString('ko-KR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
// "12.35"  (세 번째 자리에서 반올림)

(12.349).toLocaleString('ko-KR', { minimumFractionDigits: 2, maximumFractionDigits: 2 });
// "12.35"  (반올림)
```


#### 3) 통화
- <label-blue>{ style: 'currency', currency: 'KRW' }</label-blue> 는 숫자를 “통화 형식”으로 표시하라는 뜻
- <label-blue>currency</label-blue> 에 지정한 통화(KRW, USD 등)의 기호/표기 규칙을 적용

```js
// 예시
(99000).toLocaleString('ko-KR', { style: 'currency', currency: 'KRW' }); // "₩99,000"
(99000).toLocaleString('en-US', { style: 'currency', currency: 'USD' }); // "$99,000.00"


// style, currency 변경 예시
(153000).toLocaleString('ko-KR', { style: 'currency', currency: 'KRW' }); // "₩153,000"
(1530).toLocaleString('en-US', { style: 'currency', currency: 'USD' }); // "$1,530.00"
(1530).toLocaleString('en-GB', { style: 'currency', currency: 'GBP' }); // "£1,530.00"
```


#### 4) 통화와 소수 자리수 지정 함께 사용
```js
(153000).toLocaleString('ko-KR', {
  style: 'currency',
  currency: 'KRW',
  minimumFractionDigits: 0,
  maximumFractionDigits: 0,
});  
// "₩153,000"  (KRW는 보통 소수 없음, 여기선 0자리로 고정)

(1530).toLocaleString('en-US', {
  style: 'currency',
  currency: 'USD',
  minimumFractionDigits: 2,
  maximumFractionDigits: 2,
});
// "$1,530.00"
```


#### 5) 퍼센트 (%)
```js
(0.256).toLocaleString('ko-KR', { style: 'percent', minimumFractionDigits: 1 }); // "25.6%"
```


#### 6) 짧은 표기
```js
(12300).toLocaleString('ko-KR', { notation: 'compact' });                         // "1.2만"
(12300000).toLocaleString('en', { notation: 'compact' });                         // "12.3M"
(15300).toLocaleString('ko-KR', { notation: 'compact', compactDisplay: 'long' }); // "1.53만"
```


#### 맞춤 포맷 재사용
1. <label-red>Intl.NumberFormat 인스턴스(포맷터)</label-red> 를 생성 (이름 상관 없음)  
2. <label-red>.format(값)</label-red> 형태로 사용

```js
// 예시

// 포맷터 생성
const moneyKR = new Intl.NumberFormat('ko-KR', { style: 'currency', currency: 'KRW' });

// .format(값) 형식으로 사용
moneyKR.format(9876543); // "₩9,876,543"
```

---

## 11. 날짜 포맷

<txtcolor-blue>날짜/시간을 문자열로 바꾸려면 <label-blue>toLocaleString</label-blue> 또는 <label-blue>Intl.DateTimeFormat</label-blue>을 사용한다. 시간대는 <label-blue>timeZone</label-blue> 옵션으로 지정.</txtcolor-blue>

#### 1) 날짜+시간 (YYYY.MM.DD HH:mm:ss, 24시간제)
```js
// 예시 : "2025. 11. 13. 07:30:00"

const d = new Date();         // 현재 시각 지정(밀리초 타임스탬프 포함)

const text = d.toLocaleString('ko-KR', {
  timeZone: 'Asia/Seoul',     // 표시 기준 시간대(한국 시간)
  year    : 'numeric',        // 2025
  month   : '2-digit',        // 01~12 (두 자리)
  day     : '2-digit',        // 01~31 (두 자리)
  hour    : '2-digit',        // 00~23 (두 자리)
  minute  : '2-digit',        // 00~59 (두 자리)
  second  : '2-digit',        // 00~59 (두 자리)
  hour12  : false,            // 24시간제 (true면 오전/오후)
});

console.log(text);              // text에 들어간 값만 보기
console.log(typeof text, text); // text의 타입 형태와 값 함께 보기
```

#### 2) 날짜만 (YYYY.MM.DD)
```js
// 예시 : "2025. 11. 13."

const d = new Date();

const text = d.toLocaleDateString('ko-KR', {
  timeZone: 'Asia/Seoul',
  year : 'numeric',
  month: '2-digit',
  day  : '2-digit',
});

console.log(text); // "2025. 11. 13."
```

#### 3) 시간만 (HH:mm:ss, 24시간제)
```js
// 예시 : "07:30:00"

const d = new Date();

const text = d.toLocaleTimeString('ko-KR', {
  timeZone: 'Asia/Seoul',
  hour  : '2-digit',
  minute: '2-digit',
  second: '2-digit',
  hour12: false, // 24시간제
});

console.log(text); // "07:30:00"
```

#### 4) 요일 포함
<label-blue>weekday: 'short'</label-blue> : "목" 같은 짧은 요일  
<label-blue>weekday: 'long'</label-blue> : "목요일" 같은 긴 요일

```js
// 예시 : "2025. 11. 13. (목)"

const d = new Date();

const text = d.toLocaleDateString('ko-KR', {
  timeZone: 'Asia/Seoul',
  year   : 'numeric',
  month  : '2-digit',
  day    : '2-digit',
  weekday: 'short', // "목"
});

console.log(text); // "2025. 11. 13. 목"  (괄호 넣고 싶으면 문자열로 직접 추가)
```
```js
// 예시 : "목요일 07:30"

const d = new Date();

const text = d.toLocaleString('ko-KR', {
  timeZone: 'Asia/Seoul',
  weekday: 'long',   // "목요일"
  hour   : '2-digit',
  minute : '2-digit',
  hour12 : false,
});

console.log(text); // "목요일 07:30"
```

#### 5) 다른 로케일 날짜 포맷
```js
const d = new Date('2025-11-13T07:30:00Z');

// 한국
d.toLocaleString('ko-KR', { timeZone: 'Asia/Seoul' });
// 예: "2025. 11. 13. 16:30:00"

// 미국(월/일/년)
d.toLocaleString('en-US', { timeZone: 'America/New_York' });
// 예: "11/13/2025, 02:30:00"

// 독일(일.월.년)
d.toLocaleString('de-DE', { timeZone: 'Europe/Berlin' });
// 예: "13.11.2025, 15:30:00"
```

#### 맞춤 포맷 재사용
<label-red>Intl.DateTimeFormat 인스턴스(포맷터)</label-red>를 한 번 생성  
여러 곳에서 <label-red>.format(Date)</label-red> 형태로 재사용

```js
// 공통 포맷터 만들기 (한국 날짜+시간)
const dateTimeKR = new Intl.DateTimeFormat('ko-KR', {
  timeZone: 'Asia/Seoul',
  year   : 'numeric',
  month  : '2-digit',
  day    : '2-digit',
  hour   : '2-digit',
  minute : '2-digit',
  second : '2-digit',
  hour12 : false,
});

// 날짜만 포맷하는 포맷터
const dateOnlyKR = new Intl.DateTimeFormat('ko-KR', {
  timeZone: 'Asia/Seoul',
  year : 'numeric',
  month: '2-digit',
  day  : '2-digit',
});

const d = new Date('2025-11-13T07:30:00Z');

console.log(dateTimeKR.format(d)); // "2025. 11. 13. 16:30:00"
console.log(dateOnlyKR.format(d)); // "2025. 11. 13."
```
```js
// 함수로 감싸서 사용하기

function formatDateTimeKR(value) {
  const d = value instanceof Date ? value : new Date(value);
  return dateTimeKR.format(d);
}

console.log(formatDateTimeKR('2025-11-13T07:30:00Z'));
```

---

## 12. 속성(Attribute) 작성

#### 1) 속성이란?
HTML를 예로 들자면 아래와 같다.

```html
<input type="text" placeholder="이름"/>
```
- <label-blue>input</label-blue> : 태그 이름
- <label-blue>type="text"</label-blue> : 속성
- <label-blue>placeholder</label-blue> : 속성

즉, 속성은 <txtcolor-red>태그에 붙히는 옵션/설정</txtcolor-red>을 의미한다.