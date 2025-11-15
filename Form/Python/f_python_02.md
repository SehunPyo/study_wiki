<h1-costom># Python // 기초  문법</h1-costom>

Python을 사용할 때는 들여쓰기가 중요. <label-red>Tab이나 스페이스바를 네 번</label-red> 누른 공백이 필요함.
```python
if True:
print("들여쓰기 안 했어요!")  # 오류 발생
```
```python
if True:
    print("들여쓰기 했어요!")  # 정상 작동
```

---

## 1. 출력 (print)
: 터미널 혹은 화면에 코드의 결과를 출력  
<label-red>문법</label-red> : print(값)  
```python
print("안녕하세요!")
```

---

## 2. 변수
: 값을 저장  
<label-red>문법</label-red> : 변수명 = 값  
- 문자열 변수는 값을 " 혹은 ' 으로 감싸주어야 함  
```python
name = "솔이"  
```

- 숫자 변수는 숫자만 입력
```ptrhon
age = 30
```

---

## 3. 리스트
: 여러 개의 값을 저장하여 사용  
<label-red>문법</label-red> : 리스트명 = [값1, 값2, 값3]
```python
fruits = ["사과", "배", "포도"]
print(fruits[0])
```

---

## 4. 조건문 (if)
: 조건에 따라 코드의 흐름 제어  
<label-red>문법</label-red> :  
if 조건 :  
  실행할 코드

```python
if age >= 20 :
    print("성인입니다")
else :
    print("미성년자입니다")
```
---

## 5. 반복문 (for/while)
: 여러 번 같은 동작을 수행

<label-red>문법 [for문]</label-red> : 정해진 횟수나 순서가 있는 반복  
for 변수 in 리스트:  
      실행할 코드

```python
fruits = ["사과", "바나나", "포도"]
for f in fruits:
    print(f)
```

<label-red>문법 [while문]</label-red> : 조건이 참일 때 계속 반복  
while 조건:  
    실행할 코드

```python
count = 0
while count < 3:
    print("반복", count)
    count += 1
```

---

## 6. 함수 (def)
: 특정 동작을 묶어서 재사용

<label-red>문법</label-red> :  
def 함수명(매개변수):  
    실행할 코드

- def : “함수를 정의한다”는 예약어 (고정)
- greet : 함수 이름 (내가 정하는 부분)
- (name) : 매개변수 (받을 값의 이름)

```python
def greet(name):
    print("안녕, " + name + "!")

greet("솔이")
```

---

## 7. 딕셔너리
: 키(key)-값(value) 쌍으로 저장

<label-red>문법</label-red> : dict명 = {"키": "값"}  
```python
user = {"이름": "솔이", "나이": 30}
print(user["이름"])
```

---

## 8. 입력 (input)
: 사용자로부터 값 입력받기

<label-red>문법</label-red> : input("메시지")  
```python
name = input("이름을 입력하세요: ")
print("안녕하세요, " + name + "!")
```

---

## 9. 주석
: 코드에 설명을 남김 (실행되지 않음)  

<label-red>문법</label-red> : # 주석 내용  
```python
# 여기는 이름을 출력하는 코드입니다.
```