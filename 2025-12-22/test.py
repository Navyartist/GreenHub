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

class Member():
    def __init__(self, name, age, home): # 생성된 객체 자기 자신을 가리키는 문자 self, 없으면 그냥 지역변수가 되어서 클래스에선 필수
        self.name = name
        self.age = age
        self.home = home

test = Member("고양이", 126, "대전")
print(test)