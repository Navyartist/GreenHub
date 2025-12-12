
# # def hello_world():
# #     print("Hello World")

# # hello_world()

# # # 주석: ai 에이전트가 근거로 쓰기도 함. 습관화하기
# # # 주석 쓰기, 코드 쓰기... 

# # # 내 이름 name 변수로 입력받아서 출력하기
# # # name = input("Enter your name: ")
# # # print("Hello, " + name + "!")

# # # age = input("Enter your age: ")
# # # print("You are " + age + " years old.")

# # # height = float(input("Enter your height in meters: "))
# # # print("You are " + str(height) + " meters tall.")  

# 이름만 = ["김철수", "김영희", "민수", "지영"]
# 우리반 = {
#     "반장" : {
#         "이름" : 이름만[0],
#         "나이" : 10
#     },
#     "부반장": {
#         "이름" : "영희",
#         "나이" : 10
#     },
#     "학생수": 30,
#     "과목": ["수학", "과학", "영어", "역사"]
# }

# print(우리반["반장"]["이름"]) # 반장 이름 출력
# # print(이름만[0])
# # print(이름만[1])
# print(우리반["과목"][2])  # 영어 출력

# for 이름 in 이름만:
#     print(이름)

# for 우리과목 in 우리반["과목"]:
#     print(우리과목)


# if 우리반["학생수"] > 25:
#     print("학생수가 많아요")
# elif 우리반["학생수"] == 25:
#     print("학생수가 적당해요")
# else:
#     print("학생수가 적어요")


# # def greet(name, age):
# #     result = f"안녕하세요, 제 이름은 {name}이고, 나이는 {age}살입니다."
# #     return result

# # greeting = greet(우리반["반장"]["이름"], 우리반["반장"]["나이"])
# # print(greeting)

# n = 1
# num = []
# l = []
# # n은 반복할 수, num 리스트는 입력받은 출석번호를 저장할 리스트,
# # l 리스트는 결석한 학생의 출석번호를 저장할 리스트
# # n번의 입력을 받아 받은 값을 num 리스트에 추가한다
# while n < 5:
#     num.append(int(input()))
#     n += 1

# print(f"{num}")
# # num 리스트에 저장된 출석번호를 정렬한다
# num.sort()
# print(f"{num}")

# n = 1
# # 리스트 내부의 최고값까지 반복
# # n과, num 리스트에 들어가 있는 출석번호(item)를 인덱스 0부터 비교
# # 두 값이 같지 않으면 n을 l이라는 새 리스트에 추가하고,
# # n을 1 증가시킨다
# for item in num: 
#     while n < max(num):
#         if n == item:
#             break
#         else:
#             l.append(n)
#             n += 1
#     n += 1

# print(f"{l}")


