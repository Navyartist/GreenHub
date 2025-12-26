# create
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
# __file__ : 이 파일명 (bookshelf.py)
# 지금 실행하고 있는 파일의 처음부터 끝까지의 경로를 뱉고(os.path.abspath(__file__)) 그 실행하고 있는 파일의 이름은 빼라(dirname)

file_path = os.path.join(current_dir, 'data.json')
# 진짜 쓸 파일패스(파일경로)
    # 앞서 만든 current_dir에 운영체제 따라 알아서 \, / 사이에 넣어 'data.json'이랑 합쳐줌(join) = 최종 파일패스
    # 나중에 여러 파일, 다양한 경로에 있는 파일들 한꺼번에 데이터 수정할 때 편할듯
# os 라이브러리기반

# CREATE : 책꽂이에 새로 산 책을 꽂는다
def 책꽂기():
    도서명 = input("책이름을 입력하세요: ")
    작가 = input("작가를 입력하세요: ")
    출판사 = input("출판사를 입력하세요: ")
    태그 = input("태그를 입력하세요: ")

    새책 = {"도서명" : 도서명, "작가" : 작가, "출판사" : 출판사, "태그" : 태그}

    파일경로 = file_path

    if os.path.exists(파일경로): # 파일 있으면(exists) 열어 (with open문 실행)
        with open(파일경로, 'r', encoding='utf-8') as f: # f는 파일과 내 파이썬 코드를 연결해주는 일종의 '빨대(straw)' 꼭 f일 필요 없고 straw, 통로등 이름붙여도 됨, 중요한건 with - as 구조. with ~ as '빨대': 일때, 이 with ~ as 사이 안에서만 파일 열어서 이 빨대(straw, f)로 지정한 파일('파일경로'로 지정한 파일)이랑 파이썬 코드를 연결해라, 는 뜻
            try:
                책_리스트 = json.load(f) # 해당 파일(통로 f에 이어져있는 목적지=파일) json 데이터 다 읽어와~(load)
            except json.JSONDecodeError: # 안 읽히면(json형식[=문법] 제대로 못지킨 데이터가 있다든가 해서 decode가 안되면)
                책_리스트 = []
            # "책 리스트를 읽어. 근데 책 리스트가 없으면은 에러가 날 수 있어!"
    else: # "파일이 아예 없으면 새로 만들거야."
        책_리스트 = []

    책_리스트.append(새책)

    with open(파일경로, 'w', encoding='utf-8') as f:
        # json.dump(파일에 새로 쓸 데이터[='책_리스트'], 파일객체[통로(빨대)], 들여쓰기[관련된 1,2,3,4등의 옵션지정. 숫자 클수록 들여쓰기 칸(공백) 늘어남. 4가 보통 쓰임], 한글깨짐방지[ascii code 그대로 적용할거냐? 아니.(=false)]))
        json.dump(책_리스트, f, indent=4, ensure_ascii=False)

        #json.dump 함수가 내부적으로 하는 진짜 중요한 프로세스가 하나 더 있어요.

        # "직렬화(Serialization)"

        # 파이썬 세상에 살고 있는 리스트나 딕셔너리는 사실 메모리 속에 복잡하게 얽혀 있는 '객체' 상태입니다. 이걸 파일(JSON)이라는 외부 세상으로 보내려면 **"글자(String) 형태"**로 줄을 세워야 하죠.

        # json.dump는 이 줄 세우기(직렬화)와 전송(통로로 보내기)을 동시에 해주는 함수인 셈입니다.
        print(f"도서명 {도서명}: 정보를 JSON 파일에 저장 완료!")

# READING : 책의 데이터를 모두 불러와 읽고 원하는 책을 검색한다.
def 책검색():
    필드 = input("뭘로 검색하실래요? [도서명] [작가] [출판사] [태그]\n")
    # 할일: 사용자가 없는 필드를 쓰면 오류났다며 함수 종료시키는 루틴 추가

    검색단어 = input("검색어를 입력하세요: ")

    파일경로 = file_path

    with open(파일경로, 'r', encoding='utf-8') as f:
        모든책 = json.load(f)

        # 책정보 필터링
        검색결과 = [책 for 책 in 모든책 if 검색단어 in 책[필드]] # '검색결과' 변수의 자료형은 리스트
        # json.load(f)로 불러온 데이터('모든책') 안에서 if 책[필드]가 지정한 검색단어를 포함하는(in이라서) 경우의 리스트 요소만 가져온다

        if 검색결과: # 검색결과로 처리한 데이터('모든책'에서 가져온 리스트요소)가 있을때
            print(f"\n--- '{검색단어}' 검색 결과 ---")
            for 책 in 검색결과: # 이건 그냥 print, 출력처리
                print(f"도서명: {책['도서명']} | 작가: {책['작가']} | 출판사: {책['출판사']} | 태그: {책['태그']}")
        else:
            print("찾으시는 책이 없습니다.")

# UPDATE : 수정을 원하는 책 정보가 있으면 찾아서 정보를 수정한다.
def 책정보_바꾸기():
    파일경로 = file_path
    with open(파일경로, 'r', encoding='utf-8') as f:
        책_리스트 = json.load(f)
    
    바꿀책이름 = input("수정할 책의 도서명을 입력하세요: ")

    책찾음 = False
    for 책 in 책_리스트:
        if 책['도서명'] == 바꿀책이름:
            print(f"---도서 정보---\n도서명: {책['도서명']} | 작가: {책['작가']} | 출판사: {책['출판사']} | 태그: {책['태그']}")
            책['도서명'] = input("책이름을 입력하세요: ")
            책['작가'] = input("작가를 입력하세요: ")
            책['출판사'] = input("출판사를 입력하세요: ")
            책['태그'] = input("태그를 입력하세요: ")
            책찾음 = True
            break

    if 책찾음:
        with open(파일경로, 'w', encoding='utf-8') as f:
            json.dump(책_리스트, f, indent=4, ensure_ascii=False)
        print("수정이 완료되었습니다.")
    else:
        print("해당 책을 찾을 수 없습니다.")

# DELETE : 치우고 싶은 책을 데이터파일에서 지운다.
def 책_치우기():
    파일경로 = file_path

    with open(파일경로, 'r', encoding='utf-8') as f:
        책_리스트 = json.load(f)

    치울_책 = input("삭제할 책의 제목을 입력하세요: ")

    책_찾기 = None
    for 책 in 책_리스트:
        if 책['도서명'] == 치울_책:
            책_찾기 = 책
            break

    if 책_찾기:
        책_리스트.remove(책_찾기)
        print(f"[{치울_책}]을 책꽂이에서 치웁니다.")

        with open(파일경로, 'w', encoding='utf-8') as f:
            json.dump(책_리스트, f, indent=4, ensure_ascii=False)
        print("책을 치웠습니다!")
    else:
        print("책을 찾지 못했습니다.")

기능선택 = input("사용할 기능을 선택하세요. [책꽂기]: 1번, [책검색]: 2번, [책정보 바꾸기]: 3번, [책 치우기]: 4번.\n")

if 기능선택 == '1':
    책꽂기()
elif 기능선택 == '2':
    책검색()
elif 기능선택 == '3':
    책정보_바꾸기()
elif 기능선택 == '4':
    책_치우기()

# 할일: 사용자가 종료하고 싶을 때까지 무한루프하는 기능
# 책정보 바꾸기()
#   책이름이 너무 길거나 복잡하면 쓰기가 힘든데, 수정할 책을 선택할 때 ISBN같은 고유코드를 사용해야 할까? +이름이 똑같은 책일때도 문제, 책치우기 메서드에도 같은 맥락
# 이 코드에 class 쓰려면?
# 태그를 여러개 쓰고 싶음