<h1-costom># FULL STACK // Back/Front/DB 연결 (ORM 방식)</h1-costom>

---

## 1. 전체 구조 예시

#### 1) BackEnd
```py
projectForder/
    backend/
        main.py          # FastAPI 앱 시작점, CORS, 라우터 연결
        database.py      # DB 연결 설정 (engine, SessionLocal, Base, get_db)
        models.py        # SQLAlchemy ORM 모델 (테이블 매핑)
        schemas.py       # Pydantic 스키마 (요청/응답용)
        routers/
              notice.py      # /notices 관련 API (공지 CRUD)
```

#### 2) FrontEnd
```py
projectForder/
    frontend/
        src/
            App.jsx
            main.jsx
            api/
                client.js    # 공통 API 클라이언트 (fetch 래핑)
                notice.js    # 공지 API 모음 (CRUD 함수)
            pages/
                NoticePage.jsx  # 공지 페이지 (화면 + API 사용)
```

---

## 2. DB에 테이블 생성

```sql
CREATE TABLE IF NOT EXISTS t_test_notice (
    id SERIAL PRIMARY KEY,                 -- 각 공지의 고유 ID
    content TEXT NOT NULL,                 -- 공지 내용(문장)
    created_at TIMESTAMP DEFAULT NOW(),    -- 생성 시각
    updated_at TIMESTAMP                   -- 수정 시각 (처음엔 NULL, 수정 시 갱신)
);
```

---

## 3. BackEnd 공통 설정

#### 1) <lb-blue>backend / database.py</lb-blue> 생성

```py
# backend/database.py

"""
☆ 파일 설명 ☆
: DB 연결 관련 '공통 설정'을 모아두는 파일.

- 어떤 DB에 연결할지 (DATABASE_URL)
- SQLAlchemy 엔진/세션 설정
- Base (모든 ORM 모델의 부모)
- FastAPI에서 사용할 get_db() 의존성
"""

# ---------------------------------------------------------------

from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# ---------------------------------------------------------------

# 1) 어느 DB에 붙을지 URL로 정의
# 형식: postgresql+psycopg2://DB유저:비밀번호@호스트:포트/DB이름
# 여기서 비밀번호, DB 이름은 네 환경에 맞게 수정해야 한다.
DATABASE_URL = "postgresql+psycopg2://postgres:비밀번호@localhost:5432/DB이름"

# ---------------------------------------------------------------

# 2) 엔진(engine) 생성
# SQLAlchemy가 실제로 DB와 통신할 때 사용하는 핵심 객체.
# echo=True 로 두면 실행되는 SQL을 콘솔에 찍어주기 때문에 개발/디버깅할 때 유용하다.
# (나중에 시끄럽다면 False로 변경 가능)
engine = create_engine(DATABASE_URL, echo=True)

# ---------------------------------------------------------------

# 3) 세션 팩토리(SessionLocal) 생성 
# 실제 요청 처리 중에 DB와 대화할 때 사용하는 "세션(Session)"을 만들어주는 공장 같은 역할을 한다.
SessionLocal = sessionmaker(
    autocommit=False,   # 자동 커밋 안 함 (명시적으로 commit() 호출)
    autoflush=False,    # 자동 flush 안 함 (원할 때 flush/commit)
    bind=engine,        # 위에서 만든 engine 사용
)

# ---------------------------------------------------------------

# 4) Base 클래스 생성 
# 모든 ORM 모델(테이블 매핑 클래스)은 이 Base를 상속받아서 만든다.
Base = declarative_base()

# ---------------------------------------------------------------

# 5) FastAPI와 함께 쓸 get_db 의존성 
def get_db() -> Generator[Session, None, None]:
    """
    요청마다 DB 세션(Session)을 하나 열어주고,
    요청 처리가 끝나면 자동으로 닫아주는 함수.

    FastAPI의 Depends(get_db)와 함께 사용된다.
    """
    db = SessionLocal()
    try:
        yield db      # 이 구간에서 실제로 DB를 사용
    finally:
        db.close()    # 요청 처리 후 세션 정리
```

---

## 4. ORM 모델 정의

#### 1) <lb-blue>backend / models.py</lb-blue> 생성

<txt-blue>SQLAlchemy ORM 모델을 정의하는 파일</txt-blue>  
: "ORM 모델"이란, 파이썬 클래스와 DB 테이블을 1:1로 매핑해주는 클래스이다.

```py
# backend/models.py

"""
  - DB에는 실제 테이블(t_test_notice)이 있고
  - 파이썬에는 이 테이블을 표현하는 클래스(Notice)가 존재한다.

  우리가 코드에서 Notice 클래스를 사용하면,
  직접 SQL 문자열("SELECT ...", "INSERT ...")을 쓰지 않고도 DB에 저장된 공지 데이터를 객체처럼 다룰 수 있게 된다.

  ※ 테이블이 추가될 때마다, 이 파일에 클래스가 하나씩 늘어나는 구조라고 생각하면 된다.
"""

# ---------------------------------------------------------------

# SQLAlchemy에서 테이블 컬럼 생성에 필요한 타입 및 함수 모음(func) 호출
from sqlalchemy import Column, Integer, Text, DateTime, func 

# 같은 패키지 안에 있는 Base(모든 모델의 부모)중 database.py에서 작성된 모든 항목 호출
from .database import Base

# ---------------------------------------------------------------

class Notice(Base):
    """
    예시) t_test_notice 테이블을 나타내는 ORM 모델 클래스.

    이 클래스의 각 속성(Column)은 실제 DB 테이블의 컬럼과 연결된다.
    - id         : t_test_notice.id
    - content    : t_test_notice.content
    - created_at : t_test_notice.created_at
    - updated_at : t_test_notice.updated_at

    코드에서 Notice를 사용하면 예를 들어 이런 식으로 쓸 수 있다:
      - 새 공지 추가: notice = Notice(content="내용"); db.add(notice)
      - 공지 목록 조회: db.query(Notice).all()
      - 특정 공지 수정: notice.content = "수정"; db.commit()
    """

    # __tablename__ : 이 모델이 매핑될 실제 DB 테이블 이름
    # 주의: 여기 적는 이름은 DB에 존재하는 테이블 이름과 정확히 같아야 한다.
    __tablename__ = "t_test_notice"

    # ------------------------------------------------------------------
    # id 컬럼
    # ------------------------------------------------------------------
    id = Column(
        Integer,           # 정수형 컬럼 (PostgreSQL의 integer 타입)
        primary_key=True,  # 이 컬럼을 테이블의 기본키(PK)로 사용
        index=True,        # 이 컬럼에 인덱스를 추가 (id로 조회할 때 성능 향상)
    )


    # ------------------------------------------------------------------
    # content 컬럼
    # ------------------------------------------------------------------
    content = Column(
        Text,              # 길이 제한이 없는 문자열(TEXT) 타입
        nullable=False     # 내용이 비어있는(NULL) 공지는 허용하지 않음
    )


    # ------------------------------------------------------------------
    # created_at 컬럼 (레코드가 "처음 생성된 시각" 기록용)
    # ------------------------------------------------------------------
    created_at = Column(
        DateTime(timezone=True), # 시간대 정보를 포함하는 DATETIME 타입을 사용한다.
        
        server_default=func.now(),
        # INSERT 시점에, 우리가 created_at 값을 지정하지 않았을 경우 DB 서버가 자동으로 NOW() (현재 시각)를 기본값으로 채워준다.
        
        nullable=False, # NULL 값을 허용하지 않는다는 의미
    )


    # ------------------------------------------------------------------
    # updated_at 컬럼 (레코드가 "마지막으로 수정된 시각" 기록용)
    # ------------------------------------------------------------------
    updated_at = Column(
        DateTime(timezone=True), # 시간대 정보를 포함하는 DATETIME 타입을 사용한다.

        onupdate=func.now(),
        # 이 행이 UPDATE 될 때마다, 해당 시점의 DB 서버 현재 시간으로 이 컬럼을 자동 갱신해준다.

        nullable=True,
        # 1. INSERT 시점에는 아직 수정 이력이 없으므로, updated_at이 NULL이어도 허용한다.
        # 2. 첫 INSERT 이후, 실제로 수정(UPDATE)이 발생했을 때 처음으로 값이 들어간다.
        # 3. 만약 "처음 생성 시점부터 updated_at에도 값을 채우고 싶다"면?
        #    : server_default=func.now() 를 같이 넣고 nullable=False로 바꾸는 패턴도 있다.
    )
```

---

## 5. 요청 / 응답 스키마

#### 1) <lb-blue>backend / schemas.py</lb-blue> 생성

<txt-blue>DB랑 연결되기 전, models.py와 주고받을 데이터의 Pydantic 스키마를 정의하는 파일</txt-blue>  
: 클라이언트 ⇆ 서버로 오고가는 JSON(request body)의 구조/타입을 정의하고 검증한다.  

```py
# backend/schemas.py

"""
이 파일은 여러 도메인(Notice, User, Post 등)에 대한
Pydantic 스키마들을 모아두는 곳이다.

패턴은 항상 같다:

- <이름>Base     : 공통 필드
- <이름>Create   : 생성 시 요청(request body)
- <이름>Update   : 수정 시 요청(request body)
- <이름>Read     : 응답(response body, DB에서 읽은 값들 포함)

예)
- Notice 테이블  → NoticeBase, NoticeCreate, NoticeUpdate, NoticeRead
- User 테이블    → UserBase, UserCreate, UserUpdate, UserRead
- Post 테이블    → PostBase, PostCreate, PostUpdate, PostRead

즉, 각 테이블(혹은 리소스)마다 "자기 전용 스키마 묶음"을 가진다고 보면 된다.
"""

# ---------------------------------------------------------------

from datetime import datetime
from pydantic import BaseModel

# 예시 ) 클라이언트가 입력/수정이 가능한 content, item, age, name 컬럼이 있는 상황


# 1) 공통 필드 정의용 베이스 ----------------------------

class NoticeBase(BaseModel):
    """
    클라이언트가 생성/수정 시 공통으로 입력하는 필드들.
    (공통 입력 필드 템플릿)
    """
    content: str
    item: str
    age: int
    name: str


# 2) 생성 요청용 스키마 ---------------------------------

class NoticeCreate(NoticeBase): # (NoticeBase)를 작성함으로 NoticeBase 클래스에 작성된 값을 상속받아 사용한다는 의미
    """
    새 Notice를 생성할 때 사용하는 스키마.
    - 현재는 NoticeBase에 있는 필드만 그대로 사용하므로 추가 필드 없음.
    """
    pass


# 3) 수정 요청용 스키마 ---------------------------------

class NoticeUpdate(BaseModel):
    """
    기존 Notice를 수정할 때 사용하는 스키마.
    - 부분 수정을 허용하기 위해 모든 필드를 Optional로 작성하면, 보낸 값만 변경, 안 보낸 값은 그대로 유지한다.
    """
    content: Optional[str] = None
    item   : Optional[str] = None
    name   : Optional[str] = None
    age    : Optional[int] = None


# 4) 응답용 스키마 -------------------------------------

class NoticeRead(BaseModel):
    """
    클라이언트에게 돌려줄 Notice 응답 스키마.
    - DB에서 읽은 레코드를 이 형태로 변환해서 반환.
    """
    content    : str
    item       : str
    name       : str
    age        : int
    id         : int
    created_at : datetime
    updated_at : datetime | None = None

    class Config:
        orm_mode = True
        # SQLAlchemy 모델(Notice)을 바로 스키마 형태로 변환할 수 있음.
```

---

## 5. 라우터(엔드포인트) 정의

#### 1) <lb-blue>backend / routers</lb-blue> 폴더 생성 후, 그 안에 <lb-blue>notice.py</lb-blue> 생성

<label-blue>라우터</label-blue> : 여러 엔드포인트(URL + 메서드)를 한 군데로 묶고, 들어온 요청을 어떤 함수로 보낼지 결정하는 객체  
<label-blue>엔드포인트</label-blue> : 클라이언트가 실제로 호출하는 ‘URL + HTTP 메서드 + 처리 함수’ 한 세트

```py
# backend/routers/notice.py

"""
공지(Notice)에 대한 HTTP API 라우터 + 엔드포인트 모음.

여기서 정의하는 것은 전부 'HTTP API' 이고,
실제로 DB와 통신하는 로직은 ORM(models.Notice) + Session(db)을 이용한다.

이 라우터가 담당하는 기능(엔드포인트):
- GET    /notices        : 전체 공지 목록 조회
- GET    /notices/{id}   : 특정 공지 한 개 조회
- POST   /notices        : 새 공지 생성
- PUT    /notices/{id}   : 기존 공지 수정
- DELETE /notices/{id}   : 공지 삭제
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from ..database import get_db
from .. import models, schemas

# 스키마 역할 정리:
# - schemas.NoticeCreate : 새 공지 생성 시, 요청 body 구조
# - schemas.NoticeUpdate : 공지 수정 시, 요청 body 구조
# - schemas.NoticeRead   : 공지 조회/생성/수정 후, 응답 body 구조

# 용어 정리:
# - payload 파라미터      : 클라이언트가 보낸 요청 body를 담는 변수 이름
#                          (FastAPI가 JSON -> Pydantic 모델로 자동 변환 후 주입)
# - response_model 옵션  : 이 엔드포인트가 어떤 형태의 응답 스키마를 반환하는지 지정
#                          → 응답 검증 + 필드 필터링 + /docs 문서화에 사용

# APIRouter : 공지 관련 엔드포인트들을 한 그룹으로 묶어주는 "라우터" 객체
router = APIRouter(
    prefix="/notices",   # 이 라우터 안의 모든 엔드포인트 URL 앞에 /notices 가 붙는다.
    tags=["notices"],    # 문서화(/docs)에서 이 라우터 그룹 이름
)


# 1) 전체 목록 조회 -------------------------------------

@router.get("/", response_model=List[schemas.NoticeRead])
def list_notices(db: Session = Depends(get_db)):
    """
    모든 공지를 최신순(id 내림차순)으로 돌려주는 엔드포인트.

    - 메서드 / URL : GET /notices
    - 요청 body   : 없음
    - 응답 body   : NoticeRead 리스트
    - 사용 예     : 프론트의 '공지 목록 페이지'에서 호출
    """
    notices = db.query(models.Notice).order_by(models.Notice.id.desc()).all()
    return notices


# 2) 하나만 조회 ----------------------------------------

@router.get("/{notice_id}", response_model=schemas.NoticeRead)
def get_notice(notice_id: int, db: Session = Depends(get_db)):
    """
    특정 id의 공지를 하나 조회하는 엔드포인트.

    - 메서드 / URL : GET /notices/{notice_id}
    - 요청 body   : 없음
    - 응답 body   : 해당 공지의 NoticeRead
    - 사용 예     : 프론트의 '공지 상세 보기 페이지' 등에서 호출
    """
    notice = db.query(models.Notice).get(notice_id)
    if not notice:
        # 해당 id가 없으면 404 Not Found 반환
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Notice not found",
        )
    return notice


# 3) 새 공지 생성 ---------------------------------------

@router.post("/", response_model=schemas.NoticeRead, status_code=status.HTTP_201_CREATED)
def create_notice(payload: schemas.NoticeCreate, db: Session = Depends(get_db)):
    """
    새 공지를 하나 생성하는 엔드포인트.

    - 메서드 / URL : POST /notices
    - 요청 body   : NoticeCreate (예: { "content": "..." })
    - 응답 body   : 생성된 공지의 NoticeRead (id, created_at 등 포함)
    """
    notice = models.Notice(content=payload.content)
    db.add(notice)
    db.commit()
    db.refresh(notice)  # DB에서 갱신된 값(id, created_at 등)을 다시 읽어오기
    return notice


# 4) 공지 수정(업데이트) ---------------------------------

@router.put("/{notice_id}", response_model=schemas.NoticeRead)
def update_notice(
    notice_id: int,
    payload: schemas.NoticeUpdate,
    db: Session = Depends(get_db),
):
    """
    특정 공지의 내용을 수정하는 엔드포인트.

    - 메서드 / URL : PUT /notices/{notice_id}
    - 요청 body   : NoticeUpdate (예: { "content": "새 내용" })
    - 응답 body   : 수정이 완료된 공지의 최종 상태를 담은 NoticeRead

    ※ 요청은 "수정용 스키마(NoticeUpdate)"로 받지만,
       응답은 "읽기용 스키마(NoticeRead)"로 보내
       프론트가 수정 후 최종 데이터를 바로 화면에 반영할 수 있게 한다.
    """
    notice = db.query(models.Notice).get(notice_id)
    if not notice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Notice not found",
        )

    # 현재는 content만 수정하지만, 필요하다면 다른 필드도 여기서 함께 수정 가능
    notice.content = payload.content

    db.commit()
    db.refresh(notice)
    return notice


# 5) 공지 삭제 ------------------------------------------

@router.delete("/{notice_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_notice(notice_id: int, db: Session = Depends(get_db)):
    """
    특정 공지를 삭제하는 엔드포인트.

    - 메서드 / URL : DELETE /notices/{notice_id}
    - 요청 body   : 없음
    - 응답 body   : 없음 (204 No Content)
    """
    notice = db.query(models.Notice).get(notice_id)
    if not notice:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Notice not found",
        )

    db.delete(notice)
    db.commit()
    # 204 응답에는 body가 없으므로 return 값을 명시하지 않는다.

```

---

## 6. FastAPI 앱 시작점 정의

#### 1) <lb-blue>backend / main.py</lb-blue> 생성

```py
# backend/main.py

"""
FastAPI 앱의 시작점.

역할:
- DB 초기화(Base.metadata.create_all)
- FastAPI 인스턴스 생성
- CORS 설정
- 라우터(routers.notice) 등록
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .database import Base, engine
from .routers import notice


# 1) (선택 사항) 테이블 생성 ----------------------------
# models.py 에서 정의한 Base를 이용해, DB에 테이블이 없으면 생성한다.
# 이미 DB에서 직접 CREATE TABLE을 해놨다면 이 줄이 크게 의미 있진 않지만,
# 안전하게 둬도 문제 되진 않는다.
Base.metadata.create_all(bind=engine)


# 2) FastAPI 앱 인스턴스 생성 ---------------------------

app = FastAPI(
    title="Notice API",
    description="t_test_notice 공지 CRUD 예제",
)


# 3) CORS 설정 -----------------------------------------
# - 프론트(React) 개발 서버 주소에서 오는 요청을 허용해야 한다.
# - 지금은 개발 편의를 위해 * 로 열어두었고,
#   나중에는 구체적인 origin으로 좁히는 것이 좋다.

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],         # 예: ["http://localhost:5174"] 처럼 변경 가능
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 4) 라우터 등록 ---------------------------------------

# /notices 관련 엔드포인트들을 앱에 연결
app.include_router(notice.router)
```

#### 2) 백엔드 실행

```bash
cd backend
venv\Scripts\activate # 가상환경 활성화 
uvicorn main:app --reload --port 8000
```

#### 3) 브라우저 실행

```bash
http://127.0.0.1:8000/docs 
에 접속하여 /notices 관련 엔드포인트들(목록/생성/조회/수정/삭제)이 보이면 성공.
```

---

## 7. 프론트 : 공통 API 클라이언트 생성

#### 1) <lb-blue>frontend / src / api / client.js</lb-blue> 생성

```js
// src/api/client.js

/**
 * 공통 HTTP 클라이언트.
 * - 기본 백엔드 주소(BASE_URL)를 한 곳에서 관리
 * - fetch를 래핑해서 공통 헤더/에러 처리 담당
 *
 * 장점:
 * - 나중에 백엔드 주소가 바뀌어도 이 파일만 수정하면 됨.
 * - 모든 API 요청이 동일한 형식/에러 처리를 공유.
 */

const BASE_URL = "http://127.0.0.1:8000"; // FastAPI 서버 주소

export async function request(path, options = {}) {
  // path 예: "/notices", "/notices/1" 등
  const url = BASE_URL + path;

  const defaultHeaders = {
    "Content-Type": "application/json",
  };

  const response = await fetch(url, {
    // options에 method, headers, body 등을 넣을 수 있음
    ...options,
    headers: {
      ...defaultHeaders,
      ...(options.headers || {}),
    },
  });

  // 응답 코드가 200~299 가 아니면 에러로 처리
  if (!response.ok) {
    const text = await response.text();
    throw new Error(`API Error ${response.status}: ${text}`);
  }

  // 204 No Content 같은 경우에는 body가 없으므로 null 반환
  if (response.status === 204) {
    return null;
  }

  // 나머지는 JSON이라고 가정하고 파싱
  return response.json();
}
```

---

## 8. 공지 전용 API 래퍼 생성

#### 1) <lb-blue>frontend / src / api / notice.js</lb-blue> 생성

```js
// src/api/notice.js

/**
 * 공지(Notice)와 관련된 API 함수 모음.
 *
 * 이 파일은 "어떤 URL로, 어떤 method로, 어떤 body를 보내는지"만 알고 있고,
 * 화면(컴포넌트)은 단지 noticeApi.list(), noticeApi.create(...) 같은
 * 함수를 부르는 것만 신경 쓰면 된다.
 */

import { request } from "./client";

export const noticeApi = {
  // 전체 공지 목록 조회: GET /notices
  list() {
    return request("/notices");
  },

  // 하나 조회: GET /notices/{id}
  get(id) {
    return request(`/notices/${id}`);
  },

  // 새 공지 생성: POST /notices
  create(content) {
    return request("/notices", {
      method: "POST",
      body: JSON.stringify({ content }),
    });
  },

  // 공지 수정: PUT /notices/{id}
  update(id, content) {
    return request(`/notices/${id}`, {
      method: "PUT",
      body: JSON.stringify({ content }),
    });
  },

  // 공지 삭제: DELETE /notices/{id}
  remove(id) {
    return request(`/notices/${id}`, {
      method: "DELETE",
    });
  },
};
```

---

## 9. 공지 화면 페이지 생성

#### 1) <lb-blue>frontend / src / page / NoticePage.jsx</lb-blue> 생성

```js
// src/pages/NoticePage.jsx

/**
 * 공지 관리 화면.
 *
 * 기능:
 * - 현재 DB에 저장된 공지 목록 조회
 * - 새 공지 추가
 * - 기존 공지 삭제
 * - 기존 공지 수정
 *
 * 여기서는 UI와 상태 관리만 담당하고,
 * 실제 데이터 요청은 noticeApi에 위임한다.
 */

import { useEffect, useState } from "react";
import { noticeApi } from "../api/notice";

function NoticePage() {
  // 전체 공지 목록
  const [notices, setNotices] = useState([]);

  // 새 공지 입력값
  const [newContent, setNewContent] = useState("");

  // 수정 중인 공지 (id, content)
  const [editingId, setEditingId] = useState(null);
  const [editingContent, setEditingContent] = useState("");

  const [loading, setLoading] = useState(false);

  // 1) 공지 목록 불러오기 --------------------------------
  const loadNotices = async () => {
    setLoading(true);
    try {
      const data = await noticeApi.list();
      setNotices(data);
    } catch (err) {
      console.error(err);
      alert("공지 목록을 불러오는 중 오류가 발생했습니다.");
    } finally {
      setLoading(false);
    }
  };

  // 컴포넌트 최초 렌더링 시 목록 한 번 가져오기
  useEffect(() => {
    loadNotices();
  }, []);

  // 2) 새 공지 추가 -------------------------------------
  const handleCreate = async () => {
    if (!newContent.trim()) {
      alert("내용을 입력해 주세요.");
      return;
    }
    setLoading(true);
    try {
      await noticeApi.create(newContent.trim());
      setNewContent("");   // 입력창 비우기
      await loadNotices(); // 목록 새로고침
    } catch (err) {
      console.error(err);
      alert("공지 추가 중 오류가 발생했습니다.");
    } finally {
      setLoading(false);
    }
  };

  // 3) 공지 삭제 ----------------------------------------
  const handleDelete = async (id) => {
    if (!window.confirm("정말 삭제할까요?")) return;
    setLoading(true);
    try {
      await noticeApi.remove(id);
      await loadNotices();
    } catch (err) {
      console.error(err);
      alert("공지 삭제 중 오류가 발생했습니다.");
    } finally {
      setLoading(false);
    }
  };

  // 4) 수정 모드 진입 -----------------------------------
  const startEdit = (notice) => {
    setEditingId(notice.id);
    setEditingContent(notice.content);
  };

  // 5) 수정 취소 ----------------------------------------
  const cancelEdit = () => {
    setEditingId(null);
    setEditingContent("");
  };

  // 6) 수정 저장 ----------------------------------------
  const saveEdit = async () => {
    if (!editingContent.trim()) {
      alert("내용을 입력해 주세요.");
      return;
    }
    setLoading(true);
    try {
      await noticeApi.update(editingId, editingContent.trim());
      cancelEdit();
      await loadNotices();
    } catch (err) {
      console.error(err);
      alert("공지 수정 중 오류가 발생했습니다.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: 800, margin: "0 auto", padding: 24 }}>
      <h1>공지 관리 (t_test_notice)</h1>

      {/* 새 공지 작성 영역 */}
      <section style={{ marginBottom: 32 }}>
        <h2>새 공지 작성</h2>
        <textarea
          placeholder="공지 내용을 입력하세요"
          value={newContent}
          onChange={(e) => setNewContent(e.target.value)}
          rows={3}
          style={{ width: "100%", padding: 8 }}
        />
        <div style={{ marginTop: 8 }}>
          <button onClick={handleCreate} disabled={loading}>
            {loading ? "작업 중..." : "공지 추가"}
          </button>
        </div>
      </section>

      {/* 공지 목록 영역 */}
      <section>
        <h2>공지 목록</h2>
        {loading && <p>불러오는 중...</p>}
        {!loading && notices.length === 0 && <p>등록된 공지가 없습니다.</p>}

        <ul style={{ listStyle: "none", padding: 0 }}>
          {notices.map((notice) => (
            <li
              key={notice.id}
              style={{
                border: "1px solid #ddd",
                borderRadius: 4,
                padding: 12,
                marginBottom: 8,
              }}
            >
              {/* 수정 모드인지, 보기 모드인지에 따라 분기 */}
              {editingId === notice.id ? (
                <>
                  <textarea
                    value={editingContent}
                    onChange={(e) => setEditingContent(e.target.value)}
                    rows={3}
                    style={{ width: "100%", padding: 8 }}
                  />
                  <div style={{ marginTop: 8 }}>
                    <button onClick={saveEdit} disabled={loading}>
                      저장
                    </button>
                    <button
                      onClick={cancelEdit}
                      disabled={loading}
                      style={{ marginLeft: 8 }}
                    >
                      취소
                    </button>
                  </div>
                </>
              ) : (
                <>
                  <p style={{ whiteSpace: "pre-wrap", marginBottom: 8 }}>
                    {notice.content}
                  </p>
                  <small>
                    생성: {new Date(notice.created_at).toLocaleString()}
                    {notice.updated_at && (
                      <> / 수정: {new Date(notice.updated_at).toLocaleString()}</>
                    )}
                  </small>
                  <div style={{ marginTop: 8 }}>
                    <button onClick={() => startEdit(notice)}>수정</button>
                    <button
                      onClick={() => handleDelete(notice.id)}
                      style={{ marginLeft: 8 }}
                    >
                      삭제
                    </button>
                  </div>
                </>
              )}
            </li>
          ))}
        </ul>
      </section>
    </div>
  );
}

export default NoticePage;
```

---

## 10. App.jsx에서 NoticePage 연결

#### 1) <lb-blue>frontend / src / App.jsx</lb-blue> 수정

```js
// src/App.jsx
/**
 * 앱의 최상위 컴포넌트.
 * 지금은 NoticePage 하나만 보여주지만,
 * 나중에 라우터를 도입하면 여러 페이지를 연결할 수 있다.
 */

import NoticePage from "./pages/NoticePage";

function App() {
  return <NoticePage />;
}

export default App;
```