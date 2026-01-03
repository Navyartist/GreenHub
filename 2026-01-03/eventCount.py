
import datetime
import tkinter as tk
import uuid

class EventApp:
    def __init__(self, root):
        self.root = root # self.~ :인스턴스 변수
        self.root.title("Python event Pad")
        self.root.geometry("500x600")
        
        self.events_data = [
            {
                "id": str(uuid.uuid4()), 
                "이벤트명": "첫 번째 이벤트", 
                "연": "2024", "월": "01", "일": "01",
                "남은일수": "D-365"
            }
        ]

        self.new_data = {'id': '', '이벤트명': '', '연': '', '월': '', '일': '', '남은일수': ''}
        self.newid = ''
        self.name_var = tk.StringVar(value=[ev['이벤트명'] for ev in self.events_data])

        # ! 메인 컨테이너
        self.main_container = tk.Label(self.root, text='메인 컨테이너', bg='yellow')
        self.main_container.pack(fill='both', expand=True)

        # ! 왼쪽 패널 (listbox)
        self.left_label = tk.Label(self.main_container, text='왼쪽패널', bg='green', width=150)
        self.left_label.pack(side='left', fill='y')
        self.listbox = tk.Listbox(self.left_label, listvariable=self.name_var, selectmode="single")
        self.listbox.bind('<<ListboxSelect>>', self.reading_event)
        self.listbox.pack(fill="both", expand=True, padx=5, pady=5)

        # ! 오른쪽 패널 (이벤트명, [yyyy, mm, dd], d-day 일수 [추가, 저장, 삭제, 수정])
        self.right_label = tk.Frame(self.main_container)
        self.right_label.pack(side='right', fill='both', expand=True)

        # ! 1. 우상단: 이벤트명
        self.title_entry = tk.Entry(self.right_label, text='타이틀 엔트리', font=(12))
        self.title_entry.pack(fill="x", padx=10, pady=5)
        self.date_frame = tk.Frame(self.right_label)
        self.date_frame.pack(fill="x", padx=10, pady=5)
        # ! 2. 우중앙: year, month, day
        self.y_entry = tk.Entry(self.date_frame, width=6)
        self.m_entry = tk.Entry(self.date_frame, width=4)
        self.d_entry = tk.Entry(self.date_frame, width=4)
        
        date_entry_config_grid = {'row': 0, 'sticky': 'w', 'pady': 5}
        self.y_entry.grid(column=0, **date_entry_config_grid)
        self.m_entry.grid(column=2,**date_entry_config_grid)
        self.d_entry.grid(column=4,**date_entry_config_grid)

        date_label_config_grid = {'row': 0, 'sticky': 'w', 'padx': (2, 10) }
        tk.Label(self.date_frame, text="년").grid(column=1, **date_label_config_grid)
        tk.Label(self.date_frame, text="월").grid(column=3, **date_label_config_grid) # (row=0, column=3, sticky='w', padx=(2, 10))
        tk.Label(self.date_frame, text="일").grid(column=5, **date_label_config_grid) # (row=0, column=5, sticky='w', padx=(2, 10))
        # ? 중복 코드를 더 줄이는 방법은?

        # ! 3. 우중앙: D-day 일수
        tk.Label(self.right_label, text="남은 일수").pack(anchor="w", padx=10, pady=(10, 0))
        self.dday_result_label = tk.Label(self.right_label, text="날짜를 입력하세요", font=("Arial", 12, "bold"))
        self.dday_result_label.pack(pady=20)
        
        # ! 4. 우하단: 버튼 프레임
        self.button_frame = tk.Frame(self.right_label)
        self.button_frame.pack(fill='x', pady=10)

        button_config = {"width": 8, "pady": 5}
        self.add_button = tk.Button(self.button_frame, text='추가', command=self.add_setting, **button_config)
        self.save_button = tk.Button(self.button_frame, text='저장', command=self.save_event, **button_config)
        self.delete_button = tk.Button(self.button_frame, text='삭제', **button_config)
        self.update_button = tk.Button(self.button_frame, text='수정', **button_config)
        
        button_config_grid = {'row': 0, 'padx': 5}
        self.add_button.grid(column=0,**button_config_grid)
        self.save_button.grid(column=1,**button_config_grid)
        self.delete_button.grid(column=2,**button_config_grid)
        self.update_button.grid(column=3,**button_config_grid)

    def set_entry_state(self, state_value):
        """입력 위젯 잠금/해제""" # ? 중복된 부분 해결을 위해서 ai 답변으로부터 채용
        self.title_entry.config(state=state_value)
        self.y_entry.config(state=state_value)
        self.m_entry.config(state=state_value)
        self.d_entry.config(state=state_value)

    def add_setting(self):
        self.newid = str(uuid.uuid4())
        self.set_entry_state("normal")

        self.title_entry.delete(0, tk.END)
        self.y_entry.delete(0, tk.END)
        self.m_entry.delete(0, tk.END)
        self.d_entry.delete(0, tk.END)
        self.dday_result_label.config(text="날짜를 입력하세요", fg="black")

    def save_event(self):
        
        self.set_entry_state("disabled")
        title = self.title_entry.get()
        y = self.y_entry.get()
        m = self.m_entry.get()
        d = self.d_entry.get()
        days_text = self.calculate_days()
        
        # * to-do: 제목이나 연,월,일등이 비워져 있을 때의 예외 처리 구현
        self.new_data = {'id': self.newid, '이벤트명': title, '연': y, '월': m, '일': d, '남은일수': days_text}
        
        self.events_data.append(self.new_data)
        self.list_update()

    def calculate_days(self):
        try:
            y = int(self.y_entry.get())
            m = int(self.m_entry.get())
            d = int(self.d_entry.get())
            
            target_date = datetime.datetime(y, m, d)
            today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            diff = (target_date - today).days
            
            if diff > 0:
                result = f'D-{abs(diff)}'
            elif diff < 0:
                result = f'D+{abs(diff)}'
            else:# diff가 0
                result = 'D-Day (오늘)'
            self.dday_result_label.config(text=result, fg="red" if diff == 0 else "blue")
            return result
        except ValueError:
            self.dday_result_label.config(text="날짜 오류", fg="grey")
            return "날짜 오류"
        # * 하고싶은 것: 남은 일수를 계산하는 기능과 화면에 표시되는 d-day 업데이트 기능을 함수로 분리

    def list_update(self): # 왼쪽 패널에 보여줄 이벤트 이름 리스트를 업데이트
        self.new_name_list = [events['이벤트명'] for events in self.events_data]
        self.name_var.set(self.new_name_list)

    def reading_event(self, event):
        select_index = self.listbox.curselection()
        index = select_index[0]
        selected_event = self.events_data[index]
    
        self.set_entry_state("normal")
        self.title_entry.delete(0, tk.END)
        self.y_entry.delete(0, tk.END)
        self.m_entry.delete(0, tk.END)
        self.d_entry.delete(0, tk.END)

        self.title_entry.insert(0, selected_event['이벤트명'])
        self.y_entry.insert(0, selected_event['연'])
        self.m_entry.insert(0, selected_event['월'])
        self.d_entry.insert(0, selected_event['일'])
        self.dday_result_label.config(text=f"{selected_event['남은일수']}")

        self.set_entry_state("disabled")
        # * 함께 있는 정보를 가져와야됨
        # * 모든 entry state= "normal"
        # * 이벤트명, 연월일
        # * 각 entry에 해당하는 키의 내용 가져옴
        # * 모든 entry state= "disabled"로


            

root = tk.Tk()
myapp = EventApp(root)
root.mainloop()