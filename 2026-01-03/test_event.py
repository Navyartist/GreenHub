import datetime
import tkinter as tk
import uuid
from tkinter import messagebox

class EventApp:
    def __init__(self, root):
        self.root = root # self.~ :인스턴스 변수
        self.root.title('Python event Pad')
        self.root.geometry('500x600')
        
        self.events_data = [
            {
                'id': str(uuid.uuid4()), 
                '이벤트명': '첫 번째 이벤트', 
                '연': '2024', '월': '01', '일': '01',
                '남은일수': 365
            }
        ]
        self.selected_index = None  # 현재 선택된 이벤트의 인덱스를 저장할 인스턴스 변수 (추가)
        self.newid = ''
        self.name_var = tk.StringVar(value=[ev['이벤트명'] for ev in self.events_data])

        # ! 메인 컨테이너
        self.main_container = tk.Label(self.root, text='메인 컨테이너', bg='yellow')
        self.main_container.pack(fill='both', expand=True)

        # ! 왼쪽 패널 (listbox)
        self.left_label = tk.Label(self.main_container, text='왼쪽패널', bg='green', width=150)
        self.left_label.pack(side='left', fill='y')
        self.listbox = tk.Listbox(self.left_label, listvariable=self.name_var, selectmode='single', exportselection=False)
        self.listbox.bind('<<ListboxSelect>>', self.reading_event)
        self.listbox.pack(fill='both', expand=True, padx=5, pady=5)

        # ! 오른쪽 패널 (이벤트명, [yyyy, mm, dd], d-day 일수 [추가, 저장, 삭제, 수정])
        self.right_label = tk.Frame(self.main_container)
        self.right_label.pack(side='right', fill='both', expand=True)

        # ! 1. 우상단: 이벤트명
        self.title_entry = tk.Entry(self.right_label, text='타이틀 엔트리', font=(12))
        self.title_entry.pack(fill='x', padx=10, pady=5)
        self.date_frame = tk.Frame(self.right_label)
        self.date_frame.pack(fill='x', padx=10, pady=5)
        # ! 2. 우중앙: year, month, day
        self.y_entry = tk.Entry(self.date_frame, width=6)
        self.m_entry = tk.Entry(self.date_frame, width=4)
        self.d_entry = tk.Entry(self.date_frame, width=4)
        
        date_entry_config_grid = {'row': 0, 'sticky': 'w', 'pady': 5}
        self.y_entry.grid(column=0, **date_entry_config_grid)
        self.m_entry.grid(column=2,**date_entry_config_grid)
        self.d_entry.grid(column=4,**date_entry_config_grid)

        date_label_config_grid = {'row': 0, 'sticky': 'w', 'padx': (2, 10) }
        tk.Label(self.date_frame, text='년').grid(column=1, **date_label_config_grid)
        tk.Label(self.date_frame, text='월').grid(column=3, **date_label_config_grid) # (row=0, column=3, sticky='w', padx=(2, 10))
        tk.Label(self.date_frame, text='일').grid(column=5, **date_label_config_grid) # (row=0, column=5, sticky='w', padx=(2, 10))
        # ? 중복 코드를 더 줄이는 방법은?

        # ! 3. 우중앙: D-day 일수
        tk.Label(self.right_label, text='남은 일수').pack(anchor='w', padx=10, pady=(10, 0))
        self.dday_result_label = tk.Label(self.right_label, text='날짜를 입력하세요', font=('Arial', 12, 'bold'))
        self.dday_result_label.pack(pady=20)
        tk.Label(self.right_label, text='수정/삭제하고 싶으면 리스트 목록에서 선택하세요.').pack(anchor='w', padx=10, pady=(10, 0))
        
        # ! 4. 우하단: 버튼 프레임
        self.button_frame = tk.Frame(self.right_label)
        self.button_frame.pack(fill='x', pady=10)

        button_config = {'width': 8, 'pady': 5}
        self.add_button = tk.Button(self.button_frame, text='추가', command=self.add_event, state='disabled', **button_config)
        self.save_button = tk.Button(self.button_frame, text='저장', command=self.save_event, state='disabled', **button_config)
        self.delete_button = tk.Button(self.button_frame, text='삭제', command=self.delete_event, state='disabled', **button_config)
        self.update_button = tk.Button(self.button_frame, text='수정', command=self.update_event, state='disabled', **button_config)
        
        button_config_grid = {'row': 0, 'padx': 5}
        self.add_button.grid(column=0,**button_config_grid)
        self.save_button.grid(column=1,**button_config_grid)
        self.delete_button.grid(column=2,**button_config_grid)
        self.update_button.grid(column=3,**button_config_grid)

        self.set_mode('IDLE')

    def clear_entry(self):
        # 1. 입력창 열기
        self.title_entry.config(state='normal')
        self.y_entry.config(state='normal')
        self.m_entry.config(state='normal')
        self.d_entry.config(state='normal')
        
        # 2. 내용 삭제
        self.title_entry.delete(0, tk.END)
        self.y_entry.delete(0, tk.END)
        self.m_entry.delete(0, tk.END)
        self.d_entry.delete(0, tk.END)

        # 3. 라벨 및 버튼 상태 초기화
        self.dday_result_label.config(text='날짜를 입력하세요', fg='black')

    def set_mode(self, mode):
        self.current_mode = mode
        if mode == 'EDIT':
            self.title_entry.config(state='normal')
            self.y_entry.config(state='normal')
            self.m_entry.config(state='normal')
            self.d_entry.config(state='normal')
            self.save_button.config(state='normal')
            self.add_button.config(state='disabled')
            self.delete_button.config(state='normal')
            self.update_button.config(state='disabled')
        elif mode == 'ADD':
            self.title_entry.config(state='normal')
            self.y_entry.config(state='normal')
            self.m_entry.config(state='normal')
            self.d_entry.config(state='normal')
            self.save_button.config(state='normal')
            self.add_button.config(state='disabled')
            self.delete_button.config(state='disabled')
            self.update_button.config(state='disabled')
        elif mode == 'READ':
            self.title_entry.config(state='disabled')
            self.y_entry.config(state='disabled')
            self.m_entry.config(state='disabled')
            self.d_entry.config(state='disabled')
            self.save_button.config(state='disabled')
            self.add_button.config(state='normal')
            self.delete_button.config(state='normal')
            self.update_button.config(state='normal')
        elif mode == 'IDLE':
            self.title_entry.config(state='disabled')
            self.y_entry.config(state='disabled')
            self.m_entry.config(state='disabled')
            self.d_entry.config(state='disabled')
            self.save_button.config(state='disabled')
            self.add_button.config(state='normal')
            self.delete_button.config(state='disabled')
            self.update_button.config(state='disabled')

    def add_event(self):
        self.clear_entry()
        self.selected_index = None
        self.newid = str(uuid.uuid4())
        self.set_mode('ADD')

    def save_event(self):
        title = self.title_entry.get()
        y = self.y_entry.get()
        m = self.m_entry.get()
        d = self.d_entry.get() # ? 입력된 데이터 가져옴 -추가(Create), -수정(Update)

        self.calculate_d_day() # 나중에 데이터에 남은 일수까지 저장하려면 미리 결과 리턴할 때 사용

        if not title or not y or not m or not d:
            self.dday_result_label.config(text='모든 칸을 입력해주세요.', fg='orange')
            return

        if self.selected_index is not None: # ? 저장 로직 처리: 수정(Update)과 추가(Create)
        # [수정 로직] 기존 데이터를 대입으로 아예 교체. dict의 update() 쓰는 방식도 가능
            current_id = self.events_data[self.selected_index]['id']
            self.events_data[self.selected_index] = {
                'id': current_id,
                '이벤트명': title, '연': y, '월': m, '일': d
            } # ? 실제 저장 처리되는 부분 (Update)
            self.selected_index = None # 수정 완료 후 초기화
        else: # 기존에 있는 데이터가 아님
            # [추가 로직] 새로운 데이터 생성
            new_data = {'id': self.newid, '이벤트명': title, '연': y, '월': m, '일': d}
            self.events_data.append(new_data) # ? 실제 저장 처리되는 부분 (Create)
        
        # 저장 후 디데이 라벨을 한번 더 업데이트
        self.calculate_d_day()
        self.selected_index = None

        self.set_mode('IDLE')

        messagebox.showinfo("저장 확인" "저장되었습니다!")
        self.list_update() # ? 출력: 추가 (Create), 수정 (Update) 사용자에게 피드백 출력, 좌측 리스트 업데이트

    def calculate_d_day(self):
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
            self.dday_result_label.config(text=result, fg='red' if diff == 0 else 'blue')
            return result
        except ValueError:
            self.dday_result_label.config(text='날짜 오류', fg='grey')
            return '날짜 오류'

    def list_update(self): # 왼쪽 패널에 보여줄 이벤트 이름 리스트를 업데이트하는 함수
        self.new_name_list = [events['이벤트명'] for events in self.events_data]
        self.name_var.set(self.new_name_list)

    def reading_event(self, event): # 리스트 선택시에만 활성화되는 기능
        select_index = self.listbox.curselection() # ? 조회할 리스트 선택 (Reading) 
        # ? 선택한 리스트 번호를 튜플로 반환해줌

        # 예외 처리: 선택된 것이 없을 때 오른쪽 창 내용을 초기화하고 종료
        if not select_index:
            self.clear_entry()
            self.set_mode('IDLE')
            return

        self.selected_index = select_index[0] # 반환된 인덱스 튜플 맨 첫 요소를 대입
        selected_event = self.events_data[self.selected_index] # ? 처리 (Reading): 이벤트 정보 출력을 위해 선택된 리스트 (딕셔너리) 대입
        
        # READ 모드 활성화
        self.set_mode('READ')

        self.clear_entry() # entry 입력 열고, 내부 내용 삭제 -Entry 초기화
        self.title_entry.insert(0, selected_event['이벤트명'])
        self.y_entry.insert(0, selected_event['연'])
        self.m_entry.insert(0, selected_event['월'])
        self.d_entry.insert(0, selected_event['일']) # ? 출력 (Reading): 선택된 리스트 내용 집어넣기

        self.calculate_d_day() # Entry에 들어간 데이터를 따라 재계산 후 d-day 위젯 내용 출력
        self.set_mode('READ') # READ 모드로 전환

    def update_event(self): # 리스트 선택시에만 활성화되는 기능
        if self.selected_index is None:
            return # 예외처리: 선택된 게 없으면 아무것도 안 함
        
        self.set_mode('EDIT') # 입력창 활성화 -편집 모드 (EDIT)
        # ->사용자가 내용을 수정한 후 저장 버튼을 누름
            
    def delete_event(self): # 리스트 선택시에만 활성화되는 기능
            ''''삭제' 버튼 클릭 시 실행'''
            if self.selected_index is None:
                return
            
            confirm = messagebox.askyesno('삭제 확인', '정말로 이 이벤트를 삭제하시겠습니까?') # ? 삭제 예외 처리: 삭제 여부 재확인
            if confirm:
                del self.events_data[self.selected_index] # ? 처리 (Delete): 선택된 인덱스의 데이터를 삭제
                self.selected_index = None
                self.list_update()
                self.clear_entry()
                self.dday_result_label.config(text='삭제되었습니다', fg='gray')
                self.set_mode('IDLE')

root = tk.Tk()
myapp = EventApp(root)
root.mainloop()
