# 기명 함수 (Named Function)
def greet_Return(name):
    result = "Hello, " + name + "!"
    return result

# print(value)    # 출력: Hello, Alice!
# return 함수: 값을 반환하는 함수

def greet_nonReturn(name): # return문 없음 : 반환값이 any -> none (함수명에 마우스 오버로 확인)
   print("Hello, " + name + "!")
   # return "return-none" # 주석 박으면 자동으로 none 리턴, 터미널에 출력

# 인간의 내장과 같은 함수의 필수 3요소: 입력(매개변수등), 논리/알고리즘이 들어간 기능과 기능의 실행, 출력(산출물)


def routine():
    def 일어나기(time):
        시간 = time
        return 시간
    
    def 옷입기(상의, 하의, 아우터):
        옷 = { "상의" : 상의,
             "하의" : 하의,
             "아우터" : 아우터
             }
        return 옷
        