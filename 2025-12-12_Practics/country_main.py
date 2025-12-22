import src.vendingMachine as machine

def run():
    print("대륙 이름을 적으세요.\n입력 가능한 대륙: 북아메리카, 남아메리카, 아프리카, 아시아, 유럽, 오세아니아")
    continent = input()

    try:
        country = machine.returnCountry(continent)
        result = f"{continent}에는 {country}(이)가 있습니다."
        print(result)
    except ValueError as e:
        # 에러 메시지를 사용자에게 출력
        print(f"오류: {e}")
        # sys.exit()를 사용하지 않고 프로그램이 자연스럽게 종료됩니다.

if __name__ == "__main__":
    run()