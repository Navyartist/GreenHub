# smartParking.py

class ParkingSystem:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.current_vehicles = {}  # {차번호: 입차시간(분)}
        self.parking_fee = 1000  # 1000원
        self.time_unit = 30  # 30분 단위
    
    # A-1. 입차 가능 여부 확인
    def check_entry_available(self):
        return len(self.current_vehicles) < self.max_capacity
    
    # A-2. 입차 처리
    def process_entry(self, car_number, entry_time):
        if not self.check_entry_available():
            return False, "주차장이 만차입니다."
        self.current_vehicles[car_number] = entry_time
        return True, f"{car_number} 입차 완료. 입차시간: {entry_time}분"
    
    # B-1. 출차시간 반환 및 B-2. 정산금액 산정
    def calculate_fee(self, car_number, exit_time):
        if car_number not in self.current_vehicles:
            return False, "입차 기록이 없습니다."
        
        entry_time = self.current_vehicles[car_number]
        parking_duration = exit_time - entry_time
        
        if parking_duration <= 0:
            return False, "출차시간이 입차시간보다 빠릅니다."
        
        units = (parking_duration + self.time_unit - 1) // self.time_unit
        fee = units * self.parking_fee
        
        return True, {"duration": parking_duration, "fee": fee}
    
    # C-1. 사용자의 정산 여부 확인
    def check_payment_status(self, car_number):
        return car_number in self.current_vehicles
    
    # C-2. 출차 처리
    def process_exit(self, car_number):
        if car_number not in self.current_vehicles:
            return False, "입차 기록이 없습니다."
        
        del self.current_vehicles[car_number]
        return True, f"{car_number} 출차 완료. 남은 주차 공간: {self.max_capacity - len(self.current_vehicles)}"