# 엔티티(entity): 한 명의 사람을 나타내는 데이터 단위
# 객체(object): Python에서 생성된 딕셔너리 객체
# 초기화(init): 변수를 처음 생성하고 값을 설정하는 과정
me = {
    "name": "Camel", # 속성/필드(property/field): 엔티티가 가진 데이터 항목
    "age": 23,
    "home": "Daejeon"
}
you = ["Cat", 30, "Seoul"]
another = {
    1: "Dog",
    2: 5,
    3: "Busan"
}
any = {
    "1": "Rabbit",
    "2": 2,
    "3": "Incheon"
}

# me의 name print하기
print(me["name"])
print(you[0]) # key와 인덱스(index)의 차이점
# key: **객체(딕셔너리)**에서 각 항목을 식별하는 **문자열**
# 인덱스: **배열(리스트)**에서 각 항목의 위치를 나타내는 **숫자**
print(another[1])
print(any["1"])


# 할당(assignment): 기존 속성의 값을 새로운 값으로 변경
me["name"] = "Dog" # 할당 연산자 (assignment operator): =
# 이항 연산자 (binary operator): 두 개의 피연산자를 필요로 하는 연산자. ex: +, -, *, /
# 단항 연산자 (unary operator): 하나의 피연산자를 필요로 하는 연산자. ex: -, not

# me의 name 다시 print하기
print(me["name"], me["age"], me["home"])

# 데이터 접근표기법: 점 표기법(dot notation) vs 대괄호 표기법(bracket notation)
# 점 표기법: 객체.속성명
# 대괄호 표기법: 객체["속성명"]

# 인덱스란: 리스트나 문자열에서 각 항목의 위치를 나타내는 숫자
# - 배열의 시작 위치를 나타내는 포인터 개념
# 인덱스는 0부터 시작: 왜?
# Digit(자릿수 문제): 자릿수 계산을 0부터 시작하는 것이 컴퓨터 과학에서 더 효율적이기 때문
# 메모리 주소 계산 문제: 0부터 시작하면 메모리 주소 계산이 더 간단해짐
# 0부터 시작하는 이유