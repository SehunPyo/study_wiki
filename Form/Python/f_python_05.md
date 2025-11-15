<h1-costom># Python // JSON</h1-costom>

<label-red>정의</label-red> : 데이터를 구조화 하여 텍스트로 표현하는 포맷  
<label-red>확장자</label-red> : 파일명.json  
<label-red>용도</label-red> : 서버와 클라이언트 간의 데이터 교환, 설정파일, 데이터 저장 등  
<label-red>형식</label-red> : key : value 형식으로 딕셔너리와 유사

---

## 1. 기본 구조
```python
{
  "이름": "솔이",
  "나이": 24,
  "취미": ["코딩", "게임", "음악"],
  "학생": true
}
```
: 위 데이터를 Python에서는 dict, list, str, int, float, bool, None 형태로 변환 가능

---

## 2. json 모듈
```python
import json
```
| 함수                     | 설명            | 변환 방향 |
| ---------------------- | ------------- | ----- |
| `json.dump(obj, file)` | 객체 → JSON 파일  | 저장    |
| `json.load(file)`      | JSON 파일 → 객체  | 불러오기  |
| `json.dumps(obj)`      | 객체 → JSON 문자열 | 변환    |
| `json.loads(str)`      | JSON 문자열 → 객체 | 변환    |

---

## 기본 예제 01 : json 파일 생성 후 출력

<label-red>with 문</label-red> : 파일을 열고, 블록이 끝나면 자동으로 close()를 호출하여 안전하게 닫음  
<label-red>모드</label-red> : "w"는 쓰기 모드로 파일이 없으면 생성, 있으면 내용을 덮어씀. "r"는 읽기 모드  
<label-red>encoding="utf-8"</label-red> : 한글이 포함된 텍스트를 깨짐 없이 저장하기 위한 인코딩 지정  
<label-red>obj</label-red> : object(객체)의 줄임말  

<label-red>ensure_ascii=False</label-red> : 비ASCII 문자(한글 등)를 \uXXXX 이스케이프 대신 원문 그대로 저장  
<label-red>indent</label-red> : 들여쓰기(Pretty print). 숫자가 클수록 들여쓰기 폭이 넓어짐  

```python
import json

data = {"이름": "솔이", "나이": 24, "취미": ["코딩", "게임"]}  

# 01. JSON 파일로 저장
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)


# 02. JSON 파일에서 불러오기
with open("user.json", "r", encoding="utf-8") as f:
    # json.load(file): 파일로부터 JSON 텍스트를 읽어 파이썬 객체로 역직렬화(파싱).
    obj = json.load(f)

# 파싱된 파이썬 객체 출력(딕셔너리 형태)
print(obj)
```

```
# 결과 (json)
{
  "이름": "솔이",
  "나이": 24,
  "취미": [
    "코딩",
    "게임"
  ]
}


# 결과 (terminal)
{'이름': '솔이', '나이': 24, '취미': ['코딩', '게임']}
```

---

## 기본 예제 02 : JSON 문자열 변환 (dumps / loads)

<label-red>json.dumps()</label-red> : 파이썬 객체를 JSON 형식의 “문자열”로 변환  
<label-red>json.loads()</label-red> : JSON 형식의 “문자열”을 다시 파이썬 객체로 변환  
<label-red>ensure_ascii=False</label-red> : 한글을 유니코드 이스케이프(\uXXXX) 대신 원문 그대로 표현  
<label-red>obj</label-red> : object(객체)의 줄임말로, JSON 문자열을 파싱해 얻은 파이썬 객체  

```python
import json  # JSON 텍스트 ↔ 파이썬 객체 변환용 내장 모듈

data = {"과일": "사과", "개수": 3}  # 직렬화 가능한 파이썬 객체 (dict, list, str, int 등)

# 01. 객체 → JSON 문자열
# json.dumps(obj, ...): 'obj'를 JSON 형식의 문자열(str)로 변환 (파일에 직접 쓰지 않음)
text = json.dumps(data, ensure_ascii=False)
print(text)

# 02. JSON 문자열 → 파이썬 객체
# json.loads(str): JSON 문자열을 읽어 파이썬 객체(딕셔너리 등)로 변환
obj = json.loads(text)

# 파싱된 딕셔너리에서 키 접근
print(obj["과일"])
```

```
# 결과 (JSON 문자열)
{"과일": "사과", "개수": 3}


# 결과 (terminal)
사과
```