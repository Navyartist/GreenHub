# create
import json
import os


current_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(current_dir, 'bookData.json')


class 책:
    def __init__(self, 도서명, 작가, 출판사):
        self.도서명 = 도서명
        self.작가 = 작가
        self.출판사 = 출판사

def 책꽂기():
    bookName = input("책이름을 입력하세요: ")
    author = input("작가를 입력하세요: ")
    publisher = input("출판사를 입력하세요: ")
    book = 책(bookName, author, publisher)
    bookInfo = {
        'bookName' : f"{bookName}",
        'author' : f"{author}",
        'publisher' : f"{publisher}"
    }
    with open(file_path, 'a', encoding='utf-8') as f:
        # json.dump(데이터, 파일객체, 들여쓰기, 한글깨짐방지)
        json.dump(bookInfo, f, indent=4, ensure_ascii=False)
        print(f"도서명 {bookName}: 정보를 JSON 파일에 저장 완료")

책꽂기()

# def 책읽기
# def 책정리
# def 책치우기