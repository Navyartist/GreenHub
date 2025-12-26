from bookshelf import bookShelf


책꽂이A = bookShelf("A")
책꽂이B = bookShelf("B")

리스트 = []
리스트.append(책꽂이A)
리스트.append(책꽂이B)

# 사용할_것 = input(f"어느 책꽂이를 사용하시겠어요?: {리스트}")

while(1):
    기능선택 = input("사용할 기능을 선택하세요. [책꽂기]: 1번, [책검색]: 2번, [책정보 바꾸기]: 3번, [책 치우기]: 4번, [종료]: 5번.\n")
    if 기능선택 == '1':
        책꽂이A.책꽂기()
    elif 기능선택 == '2':
        책꽂이A.책검색()
    elif 기능선택 == '3':
        책꽂이A.책정보_바꾸기()
    elif 기능선택 == '4':
        책꽂이A.책_치우기()
    elif 기능선택 == '5':
        print("종료합니다.")
        break
    print('=' * 60)

