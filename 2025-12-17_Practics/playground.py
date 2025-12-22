
members = [
    {"name": "김수빈", "age": 24, "address": "서울시 마포구", "favorite": "마라탕", "dislike": "오이"},
    {"name": "고경명", "age": 29, "address": "경기도 성남시", "favorite": "냉삼", "dislike": "가지무침"},
    {"name": "박의천", "age": 26, "address": "서울시 강남구", "favorite": "오마카세", "dislike": "고수"},
    {"name": "유효현", "age": 31, "address": "경기도 수원시", "favorite": "치맥", "dislike": "브로콜리"},
    {"name": "김민우", "age": 22, "address": "인천시 부평구", "favorite": "하와이안피자", "dislike": "당근"},
    {"name": "이세한", "age": 27, "address": "서울시 송파구", "favorite": "수제버거", "dislike": "민트초코"},
    {"name": "김재형", "age": 33, "address": "경기도 용인시", "favorite": "돼지김치구이", "dislike": "생굴"},
    {"name": "김동찬", "age": 30, "address": "경기도 고양시", "favorite": "돈카츠", "dislike": "버섯"},
    {"name": "정승훈", "age": 28, "address": "서울시 관악구", "favorite": "로제파스타", "dislike": "순대간"},
    {"name": "박지수", "age": 23, "address": "경기도 안양시", "favorite": "불족발", "dislike": "번데기"},
    {"name": "송우인", "age": 32, "address": "서울시 영등포구", "favorite": "매운갈비찜", "dislike": "홍어"},
    {"name": "신재혁", "age": 29, "address": "인천시 연수구", "favorite": "돈코츠라멘", "dislike": "파인애플"},
    {"name": "손예진", "age": 24, "address": "서울시 종로구", "favorite": "타코", "dislike": "곱창"},
    {"name": "김노현", "age": 27, "address": "경기도 부천시", "favorite": "바지락칼국수", "dislike": "닭발"},
    {"name": "전민권", "age": 34, "address": "서울시 강동구", "favorite": "얼큰순대국", "dislike": "회"}
]

def presidentInfo():
    # 회장님 정보를 '회장' 변수에 똑같이 복사해서 가져오기
    president = members[0]
    print(president['favorite'])
    # members에서 맨 처음 있는 사람의 favorite을 가져오기
    # print(members[0]["favorite"])

# def b1_1('바뀐회장정보'):
#     return
#     # 회장이 바뀌면 자동으로 members리스트 맨 위로 올려주는 함수가 짜고 싶음

def latest_newMemberInfo():
    junior = members[-1] # 신입(맨 뒤 사람) 정보 입력
    print(f"신입 회원 이름: {junior['name']}, {junior['address']}")    

def updateAdress(index, newAdress): # 타겟 멤버 번호, 새로운 주소명
    targetMember = members[index-1]
    print(f"주소록 업데이트: {targetMember['name']}, {targetMember['address']}")
    targetMember['address'] = newAdress
    print(f"주소록 업데이트 완료: {targetMember['name']}, {targetMember['address']}")

def Membersdislike(index): # 타겟 멤버 번호
    print("편식을 그만둔 멤버 정보 업데이트: ")
    targetMember = members[index-1]
    print(targetMember['name'], targetMember['dislike'])
    targetMember['dislike'] = '없음'
    print("편식을 그만둔 멤버 정보 업데이트 완료: ")
    print(targetMember['name'], targetMember['dislike'])

def addMember(newMember): # 정보 구조체로 입력
    print(f"새로운 멤버 추가: {newMember['name']}")
    members.append(newMember)
    print('=' * 30)

# def countingMembers_v1():
    count = 0
    for i in range(len(members)):
        count += 1
    return count

def countingMembers():
    return len(members)

def allMemberName():
    print("===모든 모임 멤버 이름 출력===")
    for i in range(len(members)):
        print(members[i]['name'])

# 멤버스 리스트[0] = 멤버1명의 전체정보
# 방법1. 벙개리스트 = 멤버스 리스트와 같아야함 -> 이름, 주소만 뽑아 리턴
# 방법2. 멤버스 리스트에서 이름, 주소만 뽑아서 벙개리스트에 저장함 -> 벙개리스트 리턴
def Bunggae():
    # print(members[0]['address'][:2])
    BunggaeList = []
    BunggaeAddress = '서울'
    print(f"======{BunggaeAddress} 벙개 리스트======")
    for index in range(len(members)):
        if members[index]['address'][:2] == BunggaeAddress:
            BunggaeList.append(members[index])

    for index in range(len(BunggaeList)):
        print(BunggaeList[index]['name'],BunggaeList[index]['address'][4:])

def dislikeCucumber():
    dislikeFood = '오이'
    print(f"===비상: 식당메뉴에 [{dislikeFood}]===")
    for index in range(len(members)):
        if members[index]['dislike'] == dislikeFood:
            print(f"{members[index]['name']} <== {dislikeFood} 주의!!")

def seniorMembers():
    seniorAges = 30
    senior_table = []
    for index in range(len(members)):
        if members[index]['age'] >= seniorAges:
            senior_table.append(members[index]['name'])
    print(f"형님/누님 테이블 세팅: {senior_table}")

def main():
    presidentInfo()
    latest_newMemberInfo()
    updateAdress(3, '제주도 서귀포시')
    Membersdislike(5)
    print(f"현재 모임 총인원: {countingMembers()}")
    addMember({"name": "공욱재", "age": 32, "address": "서울시 영등포구", "favorite": "아이스 아메리카노", "dislike": "따뜻한 파인애플"})
    print("식당 예약 총인원 수: ")
    print(countingMembers())
    allMemberName()
    Bunggae()
    dislikeCucumber()
    seniorMembers()

if __name__ == "__main__":
    main()