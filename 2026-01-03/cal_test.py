from datetime import datetime

class myclass:
    def __init__(self):
        self.events_data = [
            {
                '이벤트명': '반갑다', 
                '연': 2025, '월': 8, '일': 1,
                '남은일수': 'D-365'
            }
        ]
        self.title = '초기화'
        self.y = 2022
        self.m = 5
        self.d = 12

    def add(self):
        
        self.title = 'h2'
        self.y = 2026
        self.m = 3
        self.d = 15
        days_text = self.cal()
        self.new_data = {'이벤트명': self.title, '연': self.y, '월': self.m, '일': self.d, '남은일수': days_text}
        
        print(self.events_data)
        self.events_data.append(self.new_data)
        print(self.events_data)
    
    def cal(self):
        y = self.y
        m = self.m
        d = self.d
        target_date = datetime(y, m, d)
        today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        diff = (target_date - today).days # 차이값: 인트
        
        if diff > 0:
            result = f"D-{abs(diff)}"
        elif diff < 0:
            result = f"D+{abs(diff)}"
        else:# diff가 0
            result = "D-Day (오늘)"
        return result
    

myc = myclass()
myc.add()