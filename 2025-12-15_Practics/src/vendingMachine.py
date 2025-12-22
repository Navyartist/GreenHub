# test
# 파이썬 내장 라이브러리 뭐 있는지 조사하기
# 처음보는 함수를 그냥 사용해본다
#   딕셔너리이름.get(가져올 값의 key 이름)
#   random.choice(리스트이름)
#   sys.exit("CLI에 출력할 메시지")
# 리턴 없는/있는 함수 구분 연습

# 오늘 미션: 세상에 없는 자판기 만들기
#   함수: 자판기 그 자체
#   매개변수(입력) : 돈넣는곳
#   리턴 : 상품배출구
#   프린트: print() 자판기 화면에 불이 들어오는 것

import random

class TravelVendingMachine():
    def __init__(self): # 생성된 객체 자기 자신을 가리키는 문자 self, 없으면 그냥 지역변수가 되어서 클래스에선 필수
        self.__countries_data = {
            "북아메리카": ['미국', '캐나다', '멕시코', '쿠바', '자메이카'],
            "남아메리카": ['브라질', '아르헨티나', '페루', '칠레', '콜롬비아'],
            "아프리카": ['이집트', '남아프리카 공화국', '나이지리아', '케냐', '모로코'],
            "아시아": ['대한민국', '중국', '일본', '인도', '베트남'],
            "유럽": ['프랑스', '독일', '영국', '이탈리아', '스페인'],
            "오세아니아": ['호주', '뉴질랜드', '피지', '파푸아뉴기니', '사모아']
        }

    def get_random_country(self, userSelect):
        # 데이터 검증 (데이터가 내부에 있는지 확인)
        if userSelect not in self.__countries_data: # userSelect가 self.__countries_data에 없다.
            # sys.exit 대신 예외를 던져서 호출하는 쪽이 처리하게 합니다.
            raise ValueError(f"'{userSelect}'은(는) 없는 대륙입니다.") # 예외처리
        
        # 해당 대륙의 리스트를 가져와 랜덤 선택
        countries = self.__countries_data[userSelect]
        return random.choice(countries)

# 대륙 목록만 보여주는 친절한 기능 추가
    def get_available_continents(self):
        return ", ".join(self.__countries_data.keys())
    # {구분자}.join({리스트명}): 매개변수로 들어온 ['a', 'b', 'c'] 이런 식의 리스트를 'abc'의 문자열로 합쳐서 반환
    # {딕셔너리명}.keys(): dictionary 자료형에서 key 부분만 빼와 모은 리스트를 반환



# ------------------------------------------------------------------

    # 대륙 선택 후 나라 리스트 설정: 방법 2가지
    # def continentsMatching(userSelect):
    #     item = {
    #         "북아메리카": north_america,
    #         "남아메리카": south_america,
    #         "아프리카": africa,
    #         "아시아": asia,
    #         "유럽": europe,
    #         "오세아니아": oceania
    #     }
    #     # if userSelect in item:
    #     #     item_list = item.get(userSelect)
    #     #     return item_list
    #     # else:
    #     #     sys.exit("해당하는 대륙이 없음.")
        
    #     if userSelect not in item:
    #         # 호출자(returnCountry 또는 메인)에게 오류 처리 책임을 넘김
    #         raise ValueError("해당하는 대륙이 목록에 없습니다.")
    #     return item[userSelect]
        
    # # def definition_item(userSelect):
    #     if userSelect == '북아메리카':
    #         item = north_america
    #     elif userSelect == '남아메리카':
    #         item = south_america
    #     elif userSelect == '아프리카':
    #         item = africa
    #     elif userSelect == '아시아':
    #         item = asia
    #     elif userSelect == '유럽':
    #         item = europe
    #     elif userSelect == '오세아니아':
    #         item = oceania
    #     return item

    # def returnCountry(userSelect):
    #     country_list = continentsMatching(userSelect)
    #     country = random.choice(country_list)
    #     return country