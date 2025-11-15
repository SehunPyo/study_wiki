<h1-costom># Python // Python 상식</h1-costom>

---

## 1. 로컬 실행

터미널에 특정 파일의 코드 결과를 출력하는 명령어는 ```python 파일명.py```

---

## 2. 자료형 (Data Type)

<label-red>숫자형</label-red> : int, float [1, 2, 3, 3.14 ...]  
<label-red>문자열</label-red> : str ["안녕", '반가워']  
<label-red>불린</label-red> : bool [True, False]  
<label-red>리스트</label-red> [1, 2, 3]  
<label-red>딕셔너리</label-red> : key : value ["이름" : "솔이"]

---

## 3. 논리 연산자 (and/or/not)
<label-red>a > b</label-red> : a가 b보다 큰가  
<label-red>a == b</label-red> : a와 b가 같은가  
<label-red>not</label-red> : 반댓값  
<label-red>and</label-red> : 둘 다 참인가  
<label-red>or</label-red> : 둘 중 하나라도 참인가

---

## 4. 불린 (True/False)
: 참/거짓으로 조건 판단, 비교, 논리 연산 등에 사용  
[파이썬이 내부적으로 정의한 고정 값으로, 반드시 대문자로 시작]

- 비교 연산

```python
a = 10
b = 5

print(a > b)   # True
print(a == b)  # False
print(a != b)  # True
```

- 조건문 활용

```python
is_raining = True
if is_raining:
    print("우산을 챙기세요!")
else:
    print("날씨가 맑아요.")
```

- 논리 연산자 (and/or/not)

```python
hungry = True
sleepy = False

print(hungry and sleepy)  # 둘 다 참이어야 True → False
print(hungry or sleepy)   # 둘 중 하나만 참이어도 True → True
print(not hungry)         # True → False 로 반전
```

---

## 5. 임포트 (import)
#### 5-1) import와 from import의 차이점

파이썬 내부 구조를 단순히 표현하면 아래와 같다.
```scss
datetime (모듈)
 ┣ datetime  (클래스)
 ┣ timedelta (클래스)
 ┗ timezone  (클래스)
```  

가독성과 편의성을 위해 접근하려는 모듈 혹은 클래스에 따라 작성하는 것이 좋다.
```python
import moduleName # 전체 모듈 접근
from moduleName import className # 특정 클래스에 접근
from moduleName import className, className # 여러 클래스에 접근
```  

• • •

#### 5-2) import만 사용하는 경우
<label-red>import</label-red> : 이미 만들어진 기능 묶음 (module)이 있다면 모두 가져와서 사용  
: 때문에 ModuleName.ClassName 형태로 접근해야함. (모듈 안에 클래스가 있기 때문)  

```python
# 예시

import datetime

now = datetime.datetime.now()
print(now)
```  

• • •

#### 5-3) import와 from 함께 사용
<label-red>from</label-red> : 특정 모듈 안에있는 특정 클래스만 가져와서 사용
: 모듈명 없이 클래스나 함수를 바로 접근 가능.

```python
# 예시

from datetime import datetime

now = datetime.now()
print(now)
```  

• • •

#### 5-4) Module 내부 클래스 확인하기
```python
import moduleName
print(dir(moduleName))
```

---

