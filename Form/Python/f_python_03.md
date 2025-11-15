<h1-costom># Python // 응용 라이브러리</h1-costom>

---

## 1. 난수 (random)
: 개발자가 지정한 범위 혹은 값 내에서 랜덤한 값을 생성  

<label-red>random.random()</label-red> : 0.0 이상 1.0 미만 실수 반환  
<label-red>random.randint(a, b)</label-red> : a이상 b이하의 정수 반환  
<label-red>random.choice(seq)</label-red> : 시퀀스(리스트, 문자열 등)에서 임의 요소 하나 반환  
<label-red>random.shuffle(seq)</label-red> : 리스트 요소 순서 섞기  
<label-red>random.sample(seq, n)</label-red> : 중복 없이 n개 반환  

```python
# random.randint()

import random                 # ① random 모듈을 불러옴

num = random.randint(1, 10)   # ② 1~10 사이의 랜덤 정수를 변수 num에 저장
print(num)                    # ③ num을 출력
```

```python
# random.choice()

import random                        # ① random 모듈을 불러옴

choices = ["사과", "바나나", "포도"]  # ② 리스트 생성
print(random.choice(choices))        # ③ 리스트에서 랜덤으로 하나 출력
```

```python
# random.shuffle()

import random                        # ① random 모듈을 불러옴

random.shuffle(choices)              # ② 리스트 순서 섞기
print(choices)                       # ③ 섞인 리스트 출력
```

```python
# random.sample()

import random                        # ① random 모듈을 불러옴

choices = ["사과", "바나나", "포도"]  # ② 리스트 생성
print(random.sample(choices, 2))     # ③ 리스트에서 중복 없이 2개 출력
```

---

## 2. 날짜 (datetime)
: 날짜와 시간 정보를 확인·계산·형식화

<label-red>datetime.now()</label-red> : 현재 날짜·시간 반환  
<label-red>datetime.today()</label-red> : 오늘 날짜 반환  
<label-red>timedelta(days, hours, ...)</label-red> : 날짜·시간 간격 계산  
<label-red>datetime.strftime(format)</label-red> : 지정한 datetime 객체를 문자열로 변환  
<label-red>datetime.strptime(format)</label-red> : 지정한 문자열을 datetime 객체로 변환  

<label-blue>(format) 종류</label-blue>  
<sub-title>%Y</sub-title> : 4자리 연도 (e.g., 2024)  
<sub-title>%m</sub-title> : 2자리 월 (01 ~ 12)  
<sub-title>%d</sub-title> : 2자리 일 (01 ~ 31)  
<sub-title>%H</sub-title> : 24시간 형식의 시 (00 ~ 23)  
<sub-title>%M</sub-title> : 분 (00 ~ 59)  
<sub-title>%S</sub-title> : 초 (00 ~ 59)  


```python
# datetime.now()

from datetime import datetime       # ① datetime 모듈에서 datetime 클래스를 불러옴

now = datetime.now()                # ② 현재 날짜·시간을 가져옴
print(now)                          # ③ 출력 (예: 2025-10-24 09:30:15)
```

```python
# datetime.strftime()

from datetime import datetime          # ① datetime 모듈 불러옴

now = datetime.now()                   # ② 현재 날짜·시간
print(now.strftime("%Y-%m-%d %H:%M"))  # ③ 원하는 형식으로 출력
```

```python
# timedelta()

from datetime import datetime, timedelta  # ① datetime과 timedelta 불러옴

today = datetime.today()                  # ② 오늘 날짜
yesterday = today - timedelta(days=1)     # ③ 하루 전 계산
print("어제:", yesterday)
```

---

## 3. 시간 (time)
: 시간 지연, 현재 시간 측정  

<label-red>time.sleep(sec)</label-red> : 지정 시간(초) 동안 대기  
<label-red>time.time()</label-red> : 현재 시간(초 단위)  
<label-red>time.ctime()</label-red> : 현재 시각 문자열 반환  

```python
# time.sleep()

import time

print("시작")
time.sleep(2) # 2초간 대기
print("끝")
```

```python
# time.ctime()

import time

print(time.ctime()) # 현재 시각 문자열 반환
```

---

## 4. 운영체제 기능 (os)
: 운영체제(파일, 폴더, 경로) 제어

<label-red>os.getcwd()</label-red> : 현재 작업 경로 반환  
<label-red>os.listdir(path)</label-red> : 지정 경로 내 파일·폴더 목록 반환  
<label-red>os.mkdir(path)</label-red> : 새 폴더 생성  
<label-red>os.remove(file)</label-red> : 파일 삭제  
<label-red>os.rename(src, dst)</label-red> : 파일/폴더 이름 변경  

```python
# os.getcwd()

import os

print(os.getcwd())          # 현재 경로 출력
```

```python
# os.mkdir(), os.listdir()

import os

os.mkdir("test")            # 'test' 폴더 생성
print(os.listdir("."))      # 현재 폴더 내용 확인
```

```python
# os.rename(), os.remove()

import os

os.rename("test.txt", "new.txt")  # 파일 이름 변경
os.remove("new.txt")              # 파일 삭제
```

---

## 5. 패턴 (re)
: 문자열에서 특정 패턴을 찾거나 치환할 때 사용하는 정규표현식(Regular Expression) 모듈  
[정규식은 문자열에서 숫자, 문자, 기호 등의 규칙적인 형태를 찾아내는 강력한 도구]  

<label-red>re.findall(pattern, string)</label-red> : 문자열 전체에서 모든 일치 결과를 리스트로 반환  
<label-red>re.search(pattern, string)</label-red> : 첫 번째 일치 결과만 반환 (매치 객체 반환)  
<label-red>re.match(pattern, string)</label-red> : 문자열 시작 부분만 검사  
<label-red>re.sub(pattern, repl, string)</label-red> : 일치하는 부분을 다른 문자열로 치환  

#### 5-1. 파이썬 정규표현식(re) 기초 패턴표

<br>

| 패턴 | 의미 | 예시 패턴 | 매칭 예시 (O/X) | 설명 |
| :-- | :--- | :--- | :--- | :--- |
| `.` | 임의의 문자 1개 | `a.c` | `abc`(O), `a!c`(O), `ac`(X) | `a`와 `c` 사이에 **아무 문자나 딱 1개** 있으면 됩니다. |
| `\d` | 숫자 1개 (0~9) | `User\d` | `User1`(O), `User9`(O), `UserA`(X) | `User` 뒤에 **숫자가 하나** 나와야 합니다. |
| `\w` | 문자/숫자/밑줄(\_) 1개 | `\w_id` | `a_id`(O), `1_id`(O), `!_id`(X) | 한글, 영문, 숫자, `_` 중 하나가 `_id` 앞에 와야 합니다. (특수문자 제외) |
| `\s` | 공백 문자 1개 | `hello\sworld` | `hello world`(O), `helloworld`(X) | 단어 사이에 띄어쓰기(스페이스, 탭 등)가 하나 있어야 합니다. |
| `^` | 문자열의 시작 | `^Hello` | `Hello world`(O), `Say Hello`(X) | 문장이 무조건 "Hello"로 **시작**해야 합니다. |
| `$` | 문자열의 끝 | `end$` | `The end`(O), `ending`(X) | 문장이 무조건 "end"로 **끝나야** 합니다. |
| `[]` | 문자 집합 중 하나 | `[abc]` | `apple`의 **a**, `banana`의 **b**, `cat`의 **c** | 대괄호 안에 있는 문자(`a` 또는 `b` 또는 `c`) 중 **하나**만 있으면 매칭됩니다. |
| `[^]` | 문자 집합 제외 | `[^0-9]` | `a`(O), `!`(O), `1`(X) | 대괄호 안의 `^`는 **NOT**을 의미합니다. 숫자가 **아닌** 모든 것과 매칭됩니다. |
| `\|` | 또는 (OR) | `apple\|banana` | `apple`(O), `banana`(O), `grape`(X) | `apple` **또는** `banana` 둘 중 하나만 있으면 됩니다. |
| `()` | 그룹 | `(ab)+` | `ab`(O), `ababab`(O), `a`(X) | `ab`를 **한 덩어리**로 묶습니다. `ab`가 한 번 이상 반복되어야 합니다. |
| `*` | 0번 이상 반복 | `a*b` | `b`(O), `ab`(O), `aaab`(O) | `b` 앞에 `a`가 **없어도 되고**, 여러 개 있어도 됩니다. |
| `+` | 1번 이상 반복 | `a+b` | `ab`(O), `aaab`(O), `b`(X) | `b` 앞에 `a`가 **최소 한 개**는 무조건 있어야 합니다. |
| `?` | 있거나 없거나 (0 또는 1회) | `colou?r` | `color`(O), `colour`(O) | `u`가 **있어도 되고 없어도** 매칭됩니다. (미국식/영국식 철자 모두 찾을 때 유용) |
| `{n}` | 정확히 n번 반복 | `\d{3}` | `123`(O), `010`(O), `12`(X) | 숫자가 **정확히 3개** 연속으로 나와야 합니다. |


#### 5-2. 정규식 옵션 (flags)

<br>

| 옵션                       | 의미                            | 예시                                |
| ------------------------ | ----------------------------- | --------------------------------- |
| `re.IGNORECASE` (`re.I`) | 대소문자 구분 없이 검색                 | `re.findall("apple", text, re.I)` |
| `re.MULTILINE` (`re.M`)  | 여러 줄(`\n`)에서도 줄마다 `^`, `$` 적용 |                                   |
| `re.DOTALL` (`re.S`)     | `.`이 줄바꿈 문자까지 포함              |                                   |


```python
# re.findall()

import re

text = "전화번호: 010-1234-5678, 회사번호: 02-987-6543"

# 패턴: 숫자 2~3개 + 하이픈 + 숫자 3~4개 + 하이픈 + 숫자 4개
pattern = r"\d{2,3}-\d{3,4}-\d{4}"

print(re.findall(pattern, text))


# 결과
['010-1234-5678', '02-987-6543']
```

```python
# re.search()

import re

text = "오늘 날짜는 2025-10-27 입니다."

match = re.search(r"\d{4}-\d{2}-\d{2}", text)
if match:
    print("찾은 날짜:", match.group())


# 결과
찾은 날짜: 2025-10-27
```

```python
# re.sub()

import re

text = "apple banana apple"
print(re.sub("apple", "orange", text))


# 결과
orange banana orange
```

```python
# re.split()
import re

text = "사과, 배, 포도, 복숭아"
print(re.split(r",\s*", text))


# 결과
['사과', '배', '포도', '복숭아']
```

