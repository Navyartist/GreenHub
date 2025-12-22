staff = [
    {"name": "김수빈", "position": "캐셔", "hourly_wage": 9860, "shift": "오전"},
    {"name": "고경명", "position": "재고관리", "hourly_wage": 10200, "shift": "오후"},
    {"name": "박의천", "position": "캐셔", "hourly_wage": 9860, "shift": "오후"},
    {"name": "유효현", "position": "매니저", "hourly_wage": 12500, "shift": "풀타임"},
    {"name": "김민우", "position": "진열", "hourly_wage": 9860, "shift": "오전"},
    {"name": "이세한", "position": "캐셔", "hourly_wage": 10000, "shift": "야간"},
    {"name": "김재형", "position": "배달", "hourly_wage": 11000, "shift": "오후"},
    {"name": "김동찬", "position": "진열", "hourly_wage": 9860, "shift": "야간"},
    {"name": "정승훈", "position": "캐셔", "hourly_wage": 9860, "shift": "오전"},
    {"name": "박지수", "position": "재고관리", "hourly_wage": 10200, "shift": "오전"},
    {"name": "송우인", "position": "배달", "hourly_wage": 11000, "shift": "풀타임"},
    {"name": "신재혁", "position": "캐셔", "hourly_wage": 10000, "shift": "오후"},
    {"name": "손예진", "position": "진열", "hourly_wage": 9860, "shift": "오전"},
    {"name": "김노현", "position": "캐셔", "hourly_wage": 9860, "shift": "야간"},
    {"name": "전민권", "position": "부매니저", "hourly_wage": 11500, "shift": "풀타임"}
]

products = [
    {"name": "신라면", "price": 1350, "stock": 50, "category": "라면"},
    {"name": "진라면", "price": 1200, "stock": 45, "category": "라면"},
    {"name": "삼다수", "price": 1000, "stock": 100, "category": "음료"},
    {"name": "코카콜라", "price": 1800, "stock": 30, "category": "음료"},
    {"name": "새우깡", "price": 1500, "stock": 25, "category": "과자"},
    {"name": "포카칩", "price": 1700, "stock": 20, "category": "과자"},
    {"name": "바나나우유", "price": 1400, "stock": 40, "category": "음료"},
    {"name": "삼각김밥", "price": 1200, "stock": 15, "category": "간편식"},
    {"name": "컵라면", "price": 1100, "stock": 60, "category": "라면"},
    {"name": "초코파이", "price": 4500, "stock": 18, "category": "과자"}
]

# 욱재마트 첫 출근

def registeredStaffName():
    name = input("이름을 입력하세요: ")
    print(f"{name}님, 욱재마트에 오신 것을 환영합니다!")

def productPrice():
    print("상품명을 입력하세요: ")
    productName = input()
    for index in range(len(products)):
        if productName == products[index]["name"]:
            print(f"{products[index]['name']}의 가격은 {products[index]['price']}원입니다.")
            break

def checkedStock():
    print("재고를 확인할 상품명을 입력해주세요. : ")
    productName = input()
    for index in range(len(products)):
        if productName == products[index]["name"]:
            print(f"{products[index]['name']}의 재고는 {products[index]['stock']}개입니다.")
            break

def casher():
    print("상품명을 입력하세요: ")
    productName = input()
    print("수량을 입력하세요: ")
    productQuantity = int(input())

    def totalcal():
        for index in range(len(products)):
            if productName == products[index]["name"]:
                totalprice = products[index]['price'] * productQuantity
        return totalprice
    print(f"{productName} {productQuantity}개의 가격은 {totalcal()}원입니다.")

def searchStaff():
    print("찾을 직원 이름: ")
    staffName = input()
    for index in range(len(staff)):
            if staffName == staff[index]["name"]:
                print(f"{staffName}님은 {staff[index]['position']}이며, {staff[index]['shift']} 근무입니다.")

def calSalary():
    staffName = input("직원 이름: ")
    workingHours = int(input("이번 달 근무시간: ")) # int 변환 지정 깜빡함.
    for index in range(len(staff)):
            if staffName == staff[index]["name"]:
                print(f"{staffName}님의 예상 급여는 {workingHours * staff[index]['hourly_wage']}원입니다.")

# 주어진 구조체의 구조: 리스트 내부 요소가 딕셔너리 자료형으로 이루어짐 (전체 코드 입장에서 봤을 때 3차원 배열)
def searchProductsByCategory():
    categoryName = input("카테고리를 입력하세요: ")
    print(f"[{categoryName}] 카테고리 상품 목록: ")
    for index in range(len(products)):
        if products[index].get('category') == categoryName:
            print(f"-{products[index]['name']}")

def saleEvent():
    discountProductName = input("할인할 상품명: ")
    discountRate = int(input("할인율(%): ")) # int 변환 까먹음
    for index in range(len(products)):
        if products[index].get('name') == discountProductName:
            productPrice = products[index]['price']
            discountPrice = (productPrice * (100 - discountRate) / 100)
            break
    print(f"{discountProductName} 원래 가격: {productPrice}원")
    print(f"{discountRate}% 할인 적용 가격: {discountPrice}원")

def searchStaff_hourly():
    searchShift = input("조회할 근무 시간대: ")
    print(f"[{searchShift}] 근무 직원: ")
    for index in range(len(staff)):
        if staff[index].get('shift') == '오전':
            print(f"-{staff[index]['name']}")

def outOfStock():
    기준수량 = int(input("기준 수량 입력하세요: ")) # int 변환 또 까먹음 3
    print("warning! 재고 부족 상품: ")
    for index in range(len(products)):
        if products[index]['stock'] <= 기준수량:
            print(f"-{products[index]['name']}: {products[index]['stock']}개")

def 영수증_출력기():
    영수증 = []
    최종금액 = 0
    for count in range(3):
        상품이름 = input(f"상품 {count+1} 이름: ")
        상품수량 = int(input(f"상품 {count+1} 수량: "))
        for index in range(len(products)):
            if products[index]['name'] == 상품이름:
                총액 = 상품수량 * products[index]['price']
                메시지 = f"{상품이름}*{상품수량} {총액}원"
                영수증.append(메시지)
                최종금액 += 총액
                break

    print("===")
    for count in range(3):
        print(영수증[count-1])
    print("===")
    print("합계", 최종금액, "원")

def main():
    registeredStaffName()
    productPrice()
    checkedStock()
    casher()
    searchStaff()
    calSalary()
    searchProductsByCategory()
    saleEvent()
    searchStaff_hourly()
    outOfStock()
    영수증_출력기()

if __name__ == "__main__":
    main()