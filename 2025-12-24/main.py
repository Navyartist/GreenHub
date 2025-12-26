from bookshelf import bookShelf


최근구매 = bookShelf("A")
사고싶은책 = bookShelf("B")

shelves = []
shelves.append(최근구매)
shelves.append(사고싶은책)

names = [s.shelf_name for s in shelves]
names2 = ', '.join(names)

select_shelf = input(f"사용할 책꽂이를 골라주세요. 현재 등록되어 있는 책꽂이 목록: [{names2}]\n")

for shelf in shelves:
    if shelf.shelf_name == select_shelf:
        target_shelf = shelf
        break
    else:
        print("일치하는 책꽂이 이름이 없어요.")
        # 아래 WHILE문 실행 안 되고 프로그램 종료할 수 있게 만들어주는 방법?

while(target_shelf != ""):
    기능선택 = input("사용할 기능을 선택하세요. [책꽂기]: 1번, [책검색]: 2번, [책정보 바꾸기]: 3번, [책 치우기]: 4번, [종료]: 5번.\n")
    if 기능선택 == '1':
        target_shelf.책꽂기()
    elif 기능선택 == '2':
        target_shelf.책검색()
    elif 기능선택 == '3':
        target_shelf.책정보_바꾸기()
    elif 기능선택 == '4':
        target_shelf.책_치우기()
    elif 기능선택 == '5':
        print("종료합니다.")
        break
    print('=' * 60)

