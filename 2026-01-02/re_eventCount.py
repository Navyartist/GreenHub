
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
                "남은일수": 365
            }
        ]
        self.selected_index = None  # 현재 선택된 이벤트의 인덱스를 저장 (추가)
        self.newid = ''
        self.name_var = tk.StringVar(value=[ev['이벤트명'] for ev in self.events_data])

        # ! 메인 컨테이너
        self.main_container = tk.Label(self.root, text='메인 컨테이너', bg='yellow')
        self.main_container.pack(fill='both', expand=True)

        # ! 왼쪽 패널 (listbox)
        self.left_label = tk.Label(self.main_container, text='왼쪽패널', bg='green', width=150)
        self.left_label.pack(side='left', fill='y')
        self.listbox = tk.Listbox(self.left_label, listvariable=self.name_var, selectmode="single", exportselection=False)
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
        self.add_button = tk.Button(self.button_frame, text='추가', command=self.add_event, **button_config)
        self.save_button = tk.Button(self.button_frame, text='저장', command=self.save_event, state='disabled', **button_config)
        self.delete_button = tk.Button(self.button_frame, text='삭제', state='disabled', **button_config)
        self.update_button = tk.Button(self.button_frame, text='수정', command=self.update_event, state='disabled', **button_config)
        
        button_config_grid = {'row': 0, 'padx': 5}
        self.add_button.grid(column=0,**button_config_grid)
        self.save_button.grid(column=1,**button_config_grid)
        self.delete_button.grid(column=2,**button_config_grid)
        self.update_button.grid(column=3,**button_config_grid)


    def clear_inputs(self):
        """모든 입력 필드와 선택 상태를 초기화"""
        # 1. 인덱스 초기화
        self.selected_index = None
        
        # 2. 입력창 내용 삭제 (state가 disabled면 삭제가 안 되므로 잠시 normal로 변경)
        current_state = self.title_entry['state']
        self.set_entry_state("normal")
        
        self.title_entry.delete(0, tk.END)
        self.y_entry.delete(0, tk.END)
        self.m_entry.delete(0, tk.END)
        self.d_entry.delete(0, tk.END)
        
        # 3. 원래 상태로 복구 (또는 기본적으로 비활성화)
        self.set_entry_state("disabled")
        
        # 4. 라벨 및 버튼 상태 초기화
        self.dday_result_label.config(text="날짜를 입력하세요", fg="black")
        self.delete_button.config(state="disabled")
        self.update_button.config(state="disabled")

    def set_entry_state(self, state_value):
        """입력 위젯 잠금/해제""" # ? 중복된 부분 해결을 위해서 ai 답변으로부터 채용
        self.title_entry.config(state=state_value)
        self.y_entry.config(state=state_value)
        self.m_entry.config(state=state_value)
        self.d_entry.config(state=state_value)
        self.save_button.config(state=state_value)

    def add_event(self):
        self.clear_inputs()
        self.selected_index = None
        self.newid = str(uuid.uuid4())
        self.set_entry_state("normal")

    def save_event(self):
        title = self.title_entry.get()
        y = self.y_entry.get()
        m = self.m_entry.get()
        d = self.d_entry.get()

        days = self.calculate_d_day()

        if not title or not y or not m or not d:
            self.dday_result_label.config(text='모든 칸을 입력해주세요.', fg='orange')
            return

        if self.selected_index is not None:
        # [수정 로직] 기존 데이터 교체
            current_id = self.events_data[self.selected_index]['id']
            self.events_data[self.selected_index] = {
                'id': current_id,
                '이벤트명': title, '연': y, '월': m, '일': d
            }
            self.selected_index = None # 수정 완료 후 초기화
        else:
            # [추가 로직] 새로운 데이터 생성
            new_data = {'id': self.newid, '이벤트명': title, '연': y, '월': m, '일': d}
            self.events_data.append(new_data)
        
        # 저장 후 디데이 라벨을 한번 더 업데이트
        self.calculate_d_day()
        # 예외 처리: 항목 선택 안한 상태로 바꿔주기
        self.selected_index = None
        self.delete_button.config(state="disabled")
        self.update_button.config(state="disabled")

        self.set_entry_state("disabled")
        self.list_update()

    def calculate_d_day(self):
        try:
            y = int(self.y_entry.get())
            m = int(self.m_entry.get())
            d = int(self.d_entry.get())
            
            target_date = datetime.datetime(y, m, d)
            today = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            diff = (target_date - today).days
            
            if diff > 0:
                result = f"D-{abs(diff)}"
            elif diff < 0:
                result = f"D+{abs(diff)}"
            else:# diff가 0
                result = "D-Day (오늘)"
            self.dday_result_label.config(text=result, fg="red" if diff == 0 else "blue")
            return result
        except ValueError:
            self.dday_result_label.config(text="날짜 오류", fg="grey")
            return "날짜 오류"

    def list_update(self): # 왼쪽 패널에 보여줄 이벤트 이름 리스트를 업데이트
        self.new_name_list = [events['이벤트명'] for events in self.events_data]
        self.name_var.set(self.new_name_list)

    def reading_event(self, event):
        select_index = self.listbox.curselection()

        # 예외 처리: 항목을 선택하지 않으면 수정과 삭제는 불가하도록 막음
        if not select_index:
            self.clear_inputs()
            return
        
        self.clear_inputs()

        self.selected_index = select_index[0] # 인덱스 저장
        selected_event = self.events_data[self.selected_index]
        
        # 항목이 선택되었으니 버튼 다시 활성화시키기
        self.delete_button.config(state="normal")
        self.update_button.config(state="normal")
        
        self.set_entry_state("normal")

        self.title_entry.insert(0, selected_event['이벤트명'])
        self.y_entry.insert(0, selected_event['연'])
        self.m_entry.insert(0, selected_event['월'])
        self.d_entry.insert(0, selected_event['일'])

        self.calculate_d_day()
        self.set_entry_state("disabled")
        self.delete_button.config(state="normal")
        self.update_button.config(state="normal")
        # * 함께 있는 정보를 가져와야됨
        # * 모든 entry state= "normal"
        # * 이벤트명, 연월일
        # * 각 entry에 해당하는 키의 내용 가져옴
        # * 모든 entry state= "disabled"로

    def update_event(self):
        #* select 후 수정 버튼을 누른다.
        #* 입력창이 활성화되며, 내용을 기존상태에서 수정할수있다.
        #* 수정후 저장을 누르면, 세이브 기능이 실행된다.
        #* id가 고유값이어야 하고, new_data는 기존 데이터자리에 들어가야된다.
        #* def update_event(self):
        if self.selected_index is None:
            return # 선택된 게 없으면 아무것도 안 함
        
        self.set_entry_state("normal") # 입력창 활성화
        # 이제 사용자가 내용을 수정하고 '저장' 버튼을 누를 것입니다.
            

root = tk.Tk()
myapp = EventApp(root)
root.mainloop()