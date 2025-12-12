# main.py
from smartParking import ParkingSystem

# ParkingSystem 객체 생성 (최대 용량: 5대)
parking = ParkingSystem(max_capacity=5)

# === 입차 처리 ===
print("=== 입차 처리 ===")
result, message = parking.process_entry("서울123", entry_time=0)
print(f"결과: {result}, 메시지: {message}")

result, message = parking.process_entry("부산456", entry_time=10)
print(f"결과: {result}, 메시지: {message}")

result, message = parking.process_entry("대구789", entry_time=20)
print(f"결과: {result}, 메시지: {message}")

# === 출차 및 요금 계산 ===
print("\n=== 출차 및 요금 계산 ===")
result, fee_info = parking.calculate_fee("서울123", exit_time=50)
if result:
    print(f"서울123 - 주차시간: {fee_info['duration']}분, 요금: {fee_info['fee']}원")

result, fee_info = parking.calculate_fee("부산456", exit_time=65)
if result:
    print(f"부산456 - 주차시간: {fee_info['duration']}분, 요금: {fee_info['fee']}원")

# === 출차 처리 ===
print("\n=== 출차 처리 ===")
result, message = parking.process_exit("서울123")
print(f"결과: {result}, 메시지: {message}")

result, message = parking.process_exit("부산456")
print(f"결과: {result}, 메시지: {message}")

# === 현재 주차 상태 ===
print(f"\n현재 주차된 차량: {list(parking.current_vehicles.keys())}")
print(f"남은 주차 공간: {parking.max_capacity - len(parking.current_vehicles)}대")
