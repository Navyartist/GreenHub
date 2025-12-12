
# 오늘 미션: 세상에 없는 자판기 만들기
#   함수: 자판기 그 자체
#   매개변수(입력) : 돈넣는곳
#   리턴 : 상품배출구
#   프린트: print() 자판기 화면에 불이 들어오는 것

# 대륙, 번호를 고르면 해당 번호에 지정된 대륙 소속의 나라 이름을 뱉는 함수


def countryMachine(continent): 
    def select_country():
        if continent == '북아메리카':
            print(continent + "에는 캐나다가 있습니다.")
        elif continent == '남아메리카':
            print(continent + "에는 칠레가 있습니다.")
        elif continent == '아프리카':
            print(continent + "에는 이집트가 있습니다.")
        elif continent == '아시아':
            print(continent + "에는 한국이 있습니다.")
        elif continent == '유럽':
            print(continent + "에는 영국이 있습니다.")
        elif continent == '오세아니아':
            print(continent + "에는 호주가 있습니다.")
    return select_country()

