# 사진, 링크 첨부 가이드

---

### 1. 사진 첨부

```
작성 방법
![대체 텍스트](경로)

예시
![숭랑이](Source/Images/Sample/Sample.jpg)     
```

<<결과>>  
![숭랑이](Source/Images/Sample/Sample.jpg)     

---

### 2. 사진 크기 조절

마크다운 문법에는 크기 조절 기능이 없기 때문에 크기 조절이 필요한 경우 HTML으로 작성해야합니다.

```html
작성 방법
<img src="경로" alt="대체 텍스트" width="100">

예시
<img src="Source/Images/Sample/Sample.jpg" alt="숭랑이" width="200">  
```

<<결과>>  
<img src="Source/Images/Sample/Sample.jpg" alt="숭랑이" width="100">

---

### 3. 사진에 링크 넣기

#### 3-1 ) 내부 문서로 이동

```
작성 방법
[![대체텍스트](이미지경로)](문서 경로)

예시
[![숭랑이](Source/Images/Sample/Sample.jpg)](Guide.md)
```

<<결과>>  
[![숭랑이](Source/Images/Sample/Sample.jpg)](Guide.md)


#### 3-2 ) 외부 링크로 이동

```
작성 방법
[![대체텍스트](이미지경로)](링크 경로)

예시
[![숭랑이](Source/Images/Sample/Sample.jpg)](https://www.google.com)
```

<<결과>>  
[![숭랑이](Source/Images/Sample/Sample.jpg)](https://www.google.com)

---

### 4. 외부 링크 첨부

```
작성 방법
[보여줄 글자](링크)

예시
[구글로 이동](https://www.google.com)
```

<<결과>>  
[구글로 이동](https://www.google.com)