
import datetime
import tkinter as tk
import uuid

class EventApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python event Pad")
        self.root.geometry("500x600")
        
        self.events_data = [
            {
                "id": str(uuid.uuid4()), 
                "제목": "첫 번째 이벤트", 
                "연": "2024", "월": "01", "일": "01",
                "남은일수": 365
            }
        ]

        # ! 메인 컨테이너
        self.main_container = tk.Label(self.root, text='메인 컨테이너', bg='yellow')
        self.main_container.pack(fill='both', expand=True)

        # ! 왼쪽 패널 (listbox)
        self.left_label = tk.Label(self.main_container, text='왼쪽패널', bg='green', width=150)
        self.left_label.pack(side='left', fill='y')
        self.listbox = tk.Listbox(self.left_label, selectmode="single")
        # self.event_listbox.bind('<<ListboxSelect>>', self.on_select_event)
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
        
        self.y_entry.grid(row=0, column=0, sticky='w', pady=5)
        self.m_entry.grid(row=0, column=2, sticky='w', pady=5)
        self.d_entry.grid(row=0, column=4, sticky='w', pady=5)

        label_config = {'row': 0, 'sticky': 'w', 'padx': (2, 10) }
        tk.Label(self.date_frame, text="년").grid(column=1, **label_config)
        tk.Label(self.date_frame, text="월").grid(column=3, **label_config) # (row=0, column=3, sticky='w', padx=(2, 10))
        tk.Label(self.date_frame, text="일").grid(column=5, **label_config) # (row=0, column=5, sticky='w', padx=(2, 10))
        # ? 중복 코드를 더 줄이는 방법은?

        # ! 3. 우중앙: D-day 일수
        tk.Label(self.right_label, text="남은 일수").pack(anchor="w", padx=10, pady=(10, 0))
        self.dday_result_label = tk.Label(self.right_label, text="날짜를 입력하세요", font=("Arial", 12, "bold"))
        self.dday_result_label.pack(pady=20)
        
        # ! 4. 우하단: 버튼 프레임
        self.button_frame = tk.Frame(self.right_label)
        self.button_frame.pack(fill='x', pady=10)

        button_config = {"width": 8, "pady": 5}
        self.add_button = tk.Button(self.button_frame, text='추가', **button_config)
        self.save_button = tk.Button(self.button_frame, text='저장', **button_config)
        self.delete_button = tk.Button(self.button_frame, text='삭제', **button_config)
        self.update_button = tk.Button(self.button_frame, text='수정', **button_config)
        
        self.add_button.grid(row=0, column=0, padx=5)
        self.save_button.grid(row=0, column=1, padx=5)
        self.delete_button.grid(row=0, column=2, padx=5)
        self.update_button.grid(row=0, column=3, padx=5)

root = tk.Tk()
myapp = EventApp(root)
root.mainloop()