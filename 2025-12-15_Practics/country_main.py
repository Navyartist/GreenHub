# 만든 모듈(파일)을 불러옵니다.
from src.vendingMachine import TravelVendingMachine

def run():
    # 1. 자판기 객체 생성 (인스턴스화)
    machine = TravelVendingMachine()

    print("가고싶은 대륙의 랜덤한 여행지로 날려주는 자판기입니다.")
    print(f"입력 가능한 대륙: {machine.get_available_continents()}")
    
    continent_input = input("대륙 이름을 입력하세요: ")

    try:
        # 2. 자판기 기능을 사용하여 결과 받기
        country = machine.get_random_country(continent_input)
        
        # 3. 결과 출력
        print("-" * 30)
        print(f"🎉 당첨! 당신의 여행지는 [{country}]입니다.")
        print("-" * 30)

    except ValueError as e:
        # 자판기에서 보낸 에러 메시지를 여기서 처리
        print(f"🚨 오류 발생: {e}")
        print("올바른 대륙 이름을 입력해주세요.")

if __name__ == "__main__":
    run()

# ------------------------------------------------------------------

# import src.country_machine as machine

# def run():
#     print("대륙 이름을 적으세요.\n입력 가능한 대륙: 북아메리카, 남아메리카, 아프리카, 아시아, 유럽, 오세아니아")
#     continent = input()

#     try:
#         country = machine.returnCountry(continent)
#         result = f"{continent}에는 {country}(이)가 있습니다."
#         print(result)
#     except ValueError as e:
#         # 에러 메시지를 사용자에게 출력
#         print(f"오류: {e}")
#         # sys.exit()를 사용하지 않고 프로그램이 자연스럽게 종료됩니다.

# if __name__ == "__main__":
#     run()