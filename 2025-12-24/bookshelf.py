# create
import json
import os

current_dir = os.path.dirname(os.path.abspath(__file__))\

file_path = os.path.join(current_dir, 'data.json')


def 책꽂기(새책):
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



도서명 = input("책이름을 입력하세요: ")
작가 = input("작가를 입력하세요: ")
출판사 = input("출판사를 입력하세요: ")

새책_정보 = {"도서명" : 도서명, "작가" : 작가, "출판사" : 출판사}
책꽂기(새책_정보)

# def 책읽기
# def 책정리
# def 책치우기