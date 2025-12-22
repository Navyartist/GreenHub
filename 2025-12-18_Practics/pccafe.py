pcCafe = {
    '음식' : ["라면", "과자", "음료수", "햄버거", "볶음밥" ]
    }

# * 카페에 있는 음식 목록 '조회'하기
for foodIndex in range(len(pcCafe["음식"])): # print시 range(0, 5) 0~5까지 순회하거나 모아서 리스트로 저장하거나. join을 활용했을수도
    print(foodIndex, pcCafe['음식'][foodIndex]) # 0 라면\n 1 과자\n ...

userChoice = input("먹고싶은 음식은? ") # CLI 용 입력도구
# 만약에 인풋에 입력된 값이 pc카페에 있는 음식이 아니라면, 죄송하지만 준비중입니다. 나중에는 추가할께요.
# 배열에 있는 항목이라면 5분내로 준비해서 드리겠습니다.
if userChoice in pcCafe['음식']:
    print("5분내로 준비해드리겠습니다.")
else:
    user_yes_no = ""
    print("죄송하지만 그 음식은 준비중입니다.")
    user_yes_no = input("하지만, 제가 내일 준비할까요? (네/아니요) ")
    if user_yes_no == '네':
        print("네. 음식을 추가하겠습니다.")
        pcCafe["음식"].append(f"{userChoice}")
    else:
        print("네, 알겠습니다.")

#* 1. 카페 음식 정의하기
#* 2. 카페 음식 조회하기
#* 3. 사용자에게 음식 뭐 먹을건지 묻기
#* 4. 사용자가 선택한 음식이 카페에 있는지 확인하기
#* 5. 음식이 있으면 준비하겠다고 알리기
#* 6. 음식이 없으면 그 음식을 내일 준비해놓을지 묻기

# 입력-> 진행-> 출력

# sig = False
# for index in range(len(pcCafe["음식"])):
#     if userChoice == pcCafe['음식'][index]:
#         sig = True
#         break

# if sig == True:
#     print("5분내로 준비해드리겠습니다.")
# else:
#     user_yes_no = ""
#     print("죄송하지만 그 음식은 준비중입니다.")
#     user_yes_no = input("하지만, 제가 내일 준비할까요? (네/아니요) ")
#     if user_yes_no == '네':
#         pcCafe["음식"].append(f"{userChoice}")
#     else:
#         print("네, 알겠습니다.")

# 표준입력/출력방식 Standard in, Standard out / stdin stdout