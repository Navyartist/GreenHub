# create
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))\

file_path = os.path.join(current_dir, 'data.json')


def 책꽂기():
    도서명 = input("책이름을 입력하세요: ")
    작가 = input("작가를 입력하세요: ")
    출판사 = input("출판사를 입력하세요: ")
    태그 = input("태그를 입력하세요: ")

    새책 = {"도서명" : 도서명, "작가" : 작가, "출판사" : 출판사, "태그" : 태그}

    파일경로 = file_path

    if os.path.exists(파일경로):
        with open(파일경로, 'r', encoding='utf-8') as f:
            try:
                책_리스트 = json.load(f)
            except json.JSONDecodeError:
                책_리스트 = []
            # "책 리스트를 읽어. 근데 책 리스트가 없으면은 에러가 날 수 있어!"
    else: # "파일이 아예 없으면 새로 만들거야."
        책_리스트 = []

    책_리스트.append(새책)

    with open(파일경로, 'w', encoding='utf-8') as f:
        # json.dump(데이터, 파일객체, 들여쓰기, 한글깨짐방지)
        json.dump(책_리스트, f, indent=4, ensure_ascii=False)
        print(f"도서명 {도서명}: 정보를 JSON 파일에 저장 완료!")

def 책검색():
    필드 = input("뭘로 검색하실래요? [도서명] [작가] [출판사] [태그]")

    검색단어 = input("검색어를 입력하세요: ")

    파일경로 = file_path

    with open(파일경로, 'r', encoding='utf-8') as f:
        모든책 = json.load(f)

        # 책정보 필터링
        검색결과 = [책 for 책 in 모든책 if 검색단어 in 책[필드]]

        if 검색결과:
            print(f"\n--- '{검색단어}' 검색 결과 ---")
            for 책 in 검색결과:
                print(f"도서명: {책['도서명']} | 작가: {책['작가']} | 출판사: {책['출판사']} | 태그: {책['태그']}")
        else:
            print("찾으시는 책이 없습니다.")


기능선택 = input("사용할 기능을 선택하세요. [책꽂기]:1번, [책검색]:2번")

if 기능선택 == '1':
        책꽂기()
elif 기능선택 == '2':
        책검색()


# def 책정리
# def 책치우기