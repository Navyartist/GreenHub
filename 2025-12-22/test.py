member = [
    {
        'name' : '고양이',
        'age' : 124,
        'home' : '대전'
    },
    {
        'name' : '개',
        'age' : 156,
        'home' : '대전'
    }
]

class Member:
    def __init__(self, name, age, home): # 생성된 객체 자기 자신을 가리키는 문자 self, 없으면 그냥 지역변수가 되어서 클래스에선 필수
        self.name = name
        self.age = age
        self.home = home
    # 클래스 내부에 들어가야함
    def __str__(self):
        return f"이름: {self.name}, 나이: {self.age}세, 사는곳: {self.home}시"

dogInfo = Member("개", 50, "서울")
print(dogInfo)
print(str(dogInfo))

dogMessage = f"--개 정보-- {dogInfo}"
print(dogMessage)

# CatInfo = __str__(Member("고양이", 126, "대전"))
# catMessage = str(CatInfo)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     # __str__ 메서드 정의
#     def __str__(self):
#         return f"이름: {self.name}, 나이: {self.age}세"

# # 객체 생성
# person1 = Person("홍길동", 30)

# # print() 호출 시 __str__ 메서드 사용
# print(person1)  # 출력: 이름: 홍길동, 나이: 30세

# # str() 함수 호출 시 __str__ 메서드 사용
# print(str(person1)) # 출력: 이름: 홍길동, 나이: 30세

# # 객체 자체를 출력 시 (f-string 등)
# message = f"정보: {person1}"
# print(message) # 출력: 정보: 이름: 홍길동, 나이: 30세

# # __str__이 없을 경우 (기본 출력)
# class Simple:
#     def __init__(self, value):
#         self.value = value

# s = Simple(10)
# print(s) # 출력: <__main__.Simple object at 0x...> (메모리 주소)
