import tkinter as tk
from tkinter import messagebox
import uuid
from datetime import datetime

class eventApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python event Pad")
        self.root.geometry("500x600")

        # --- 데이터 저장소 (고유 ID를 포함한 리스트 구조) ---
        # 기존 구조에서 id라는 고유 key 역할을 추가하고 제목이 같아도 id가 다르면 서로 다른 이벤트로 취급되도록 재구성
        self.events_data = [
            {
                "id": str(uuid.uuid4()), 
                "제목": "첫 번째 이벤트", 
                "연": "2024", "월": "01", "일": "01",
                "남은일수": "D-365"
            }
            # ! uuid4: uuid라는 고유 아이디 생성 메서드의 종류중 하나. 1부터 5까지 있고, 4는 완전 랜덤 난수로 id를 만든다.
            # ! 그냥 겹치지 않는 id = uuid4, 만든 자의 정보, 만들어진 시간 관련 정보가 추가 필요한 id = uuid1등.
            # ! notion같은 페이지 생성자가 함께 나와있는 구현은 uuid1이 적합할듯하다. 흔히 보는 메모앱처럼 만들어진 시간만 나오게 하는 방법도 찾아보면 있을것같다.
        ]
        
        # 현재 선택된 이벤트항목의 id를 추적하기 위한 변수
        self.current_event_id = None

        self.setup_ui()
        self.refresh_list()

    def setup_ui(self):
        # ! 1. 메인 컨테이너 (좌우 구분)
        self.main_container = tk.Frame(self.root)
        self.main_container.pack(fill="both", expand=True)

        # ! 2. 왼쪽 패널 (세로로 긴 메모 이름 리스트)
        self.left_panel = tk.Frame(self.main_container, width=150)
        self.left_panel.pack(side="left", fill="y")
        # self.list_label = tk.Label(self.left_panel, text="내 이벤트 목록")
        # self.list_label.pack(pady=10)
        self.event_listbox = tk.Listbox(self.left_panel, selectmode="single")
        self.event_listbox.pack(fill="both", expand=True, padx=5, pady=5)
        self.event_listbox.bind('<<ListboxSelect>>', self.on_select_event) # 이벤트 바인딩

        # ! 오른쪽 패널 (입력창 및 버튼)
        self.right_panel = tk.Frame(self.main_container)
        self.right_panel.pack(side="right", fill="both", expand=True)

        # ! 우상단: 이벤트명 입력
        tk.Label(self.right_panel, text="이벤트명", bg="white").pack(anchor="w", padx=10, pady=(10, 0))
        self.title_entry = tk.Entry(self.right_panel, font=(12))
        self.title_entry.pack(fill="x", padx=10, pady=5)

        # ! 우중간: D-day 일수, 입력창 3가지
        tk.Label(self.right_panel, text="이벤트 날짜 (년/월/일)", bg="white").pack(anchor="w", padx=10)
        self.date_frame = tk.Frame(self.right_panel)
        self.date_frame.pack(fill="x", padx=10, pady=5)
        self.year_entry = tk.Entry(self.date_frame, width=6)
        self.year_entry.pack(side="left")
        tk.Label(self.date_frame, text="년").pack(side="left", padx=(2, 10))
        self.month_entry = tk.Entry(self.date_frame, width=4)
        self.month_entry.pack(side="left")
        tk.Label(self.date_frame, text="월").pack(side="left", padx=(2, 10))
        self.day_entry = tk.Entry(self.date_frame, width=4)
        self.day_entry.pack(side="left")
        tk.Label(self.date_frame, text="일").pack(side="left", padx=(2, 10))

        # ! 우하단: 입력받은 날짜대로 남은 일수를 계산하고 표시
        tk.Label(self.right_panel, text="남은 일수", bg="white").pack(anchor="w", padx=10, pady=(10, 0))
        self.dday_result_label = tk.Label(self.right_panel, text="날짜를 입력하세요", font=("Arial", 12, "bold"))
        self.dday_result_label.pack(pady=20)

        # 버튼 프레임 (추가, 저장, 삭제, 수정)
        self.button_frame = tk.Frame(self.right_panel)
        self.button_frame.pack(fill="x", pady=10)

        btn_config = {"width": 8, "pady": 5}
        self.btn_add = tk.Button(self.button_frame, text="추가", command=self.prepare_new_event, **btn_config)
        self.btn_save = tk.Button(self.button_frame, text="저장", command=self.save_event, **btn_config)
        self.btn_delete = tk.Button(self.button_frame, text="삭제", command=self.delete_event, **btn_config)
        self.btn_update = tk.Button(self.button_frame, text="수정", command=self.unlock_for_update, **btn_config)
        # * 버튼 위젯들 정의

        self.btn_add.grid(row=0, column=0, padx=5)
        self.btn_save.grid(row=0, column=1, padx=5)
        self.btn_delete.grid(row=0, column=2, padx=5)
        self.btn_update.grid(row=0, column=3, padx=5)
        # * grid를 이용해 정렬: 버튼들을 균등하고 깔끔하게 배치하기 위해서
        self.button_frame.columnconfigure((0, 1, 2, 3), weight=1) # pack()의 fill 옵션과 비슷한 기능

    # --- 내부 계산 함수 ---
    def calculate_dday(self):
        """입력된 년, 월, 일을 바탕으로 오늘과의 차이 계산"""
        try:
            y = int(self.year_entry.get())
            m = int(self.month_entry.get())
            d = int(self.day_entry.get())
            
            target_date = datetime(y, m, d)
            today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
            # ! 현재 시간(now)에서 시간, 분, 초, 밀리초를 다 빼고 day만 남도록 바꿈 (replace)
            diff = (target_date - today).days # 차이 일수를 계산 (days는 일수를 계산해 반환한다)
            
            if diff > 0:
                result = f"D-{abs(diff)}"
            elif diff < 0:
                result = f"D+{abs(diff)}" # ! abs: 기호 없는 절댓값을 반환
            else:# diff가 0
                result = "D-Day (오늘)"
            
            self.dday_result_label.config(text=result, fg="red" if diff == 0 else "blue") # D-day일 때 글씨를 red로
            return result
        except ValueError:
            self.dday_result_label.config(text="날짜 오류", fg="grey") # ! datetime 모듈이 계산하지 않는 날짜/시간은 에러를 발생시킴. ex: 2월 30일, 4월 31일 (존재 불가능) 연도: 최대 9999까지 계산함 (10001년 불가)
            return "날짜 오류"
        
    def refresh_list(self): # 이벤트 추가시마다 리스트박스(순서-이벤트이름 구조)를 실시간으로 갱신시킴
        """리스트박스를 리스트 데이터로 갱신"""
        self.event_listbox.delete(0, tk.END) # ! 기존 (새 이벤트 추가나 수정, 삭제전) 이벤트명(리스트박스의 리스트)을 싸그리 지우기 -> 바뀐 데이터(events_data)로 리스트에 다시 집어넣기.
        # ? delete(시작할 위치, 끝낼 위치) 지정한 범위의 리스트박스-리스트 항목들을 지운다. 범위는 인덱스로 계산
        for event in self.events_data: # ? events_data (리스트 안의 딕셔너리 요소 구조)에서 각 딕셔너리들을 하나씩 꺼내오기
            self.event_listbox.insert(tk.END, event["제목"]) # ? 각 딕셔너리의 '제목' value를 왼 패널 리스트에 재추가

    def on_select_event(self, event): # ! 이벤트 바인딩으로 호출되기에 이벤트 관련 변수를 받아와야함 (눌린 키 정보, 마우스 커서 위치같은 것)
        """리스트에서 항목 선택 시 호출"""
        selection = self.event_listbox.curselection() # ? Current Selection(현재 선택한 것)의 인덱스 번호들이 몇인지 반환해라. (튜플로 반환)
        if selection: # 튜플의 맨 첫번째 인덱스
            index = selection[0]
            # 인덱스를 통해 데이터 리스트에서 해당 이벤트 정보 객체를 가져옵니다.
            selected_event = self.events_data[index] 
            
            self.current_event_id = selected_event["id"] # ? 현재 선택한 이벤트의 id에 해당하는 제목과 내용을 보여줌
            self.set_widgets_state("normal")

            self.title_entry.delete(0, tk.END) 
            self.title_entry.insert(0, selected_event["제목"])
            
            self.year_entry.delete(0, tk.END) # ! entry 내용 싸그리 지우기. 처음부터 끝(tk.END)까지
            self.year_entry.insert(0, selected_event.get("연", "")) # ! 선택한 메모의 "연" (key)에 해당하는 value 가져와라. 해당하는 value가 없으면 "" 반환
            self.month_entry.delete(0, tk.END)
            self.month_entry.insert(0, selected_event.get("월", ""))
            self.day_entry.delete(0, tk.END)
            self.day_entry.insert(0, selected_event.get("일", ""))

            # 데이터 삽입 후 자동으로 디데이 계산하여 라벨 업데이트
            self.calculate_dday()

            self.set_widgets_state("disabled")


    def set_widgets_state(self, state_value):
        """입력 위젯 잠금/해제"""
        self.title_entry.config(state=state_value)
        self.year_entry.config(state=state_value)
        self.month_entry.config(state=state_value)
        self.day_entry.config(state=state_value)

    def prepare_new_event(self):
        """새 이벤트 작성을 위한 준비 (현재 선택 ID 초기화)"""
        self.current_event_id = None # 새로운 이벤트에 id를 새로 부여하기 위해 설정
        self.set_widgets_state("normal")
        self.title_entry.delete(0, tk.END)
        self.year_entry.delete(0, tk.END)
        self.month_entry.delete(0, tk.END)
        self.day_entry.delete(0, tk.END)
        self.dday_result_label.config(text="날짜를 입력하세요", fg="black")
        self.title_entry.focus() # ? 사용자가 제목을 바로 입력할 수 있게 title_entry 위젯에 커서 이동 (포커스)

    def save_event(self):
        """이벤트 저장 (ID가 있으면 수정, 없으면 신규 추가)"""
        title = self.title_entry.get()
        y, m, d = self.year_entry.get(), self.month_entry.get(), self.day_entry.get()
        
        if not title or not y or not m or not d:
            messagebox.showwarning("주의", "모든 필드를 입력해주세요.")
            return

        # 저장 전 계산 한 번 수행
        self.calculate_dday()

        if self.current_event_id: # id가 있을 때 (기존 이벤트일 때)
            # 기존 이벤트 수정
            for event in self.events_data: # refresh_list와 반복 동일하게
                if event["id"] == self.current_event_id: # ? 현재 리스트중 같은 id가 있으면 = 그것은 기존 이벤트의 수정이란 의미
                    event.update({"제목": title, "연": y, "월": m, "일": d})
                    break
        else:
            # 신규 이벤트 추가 (제목이 같아도 새로운 id 부여)
            new_event = { # ? 새롭게 추가할 이벤트 데이터
                "id": str(uuid.uuid4()), "제목": title, 
                "연": y, "월": m, "일": d
            }
            self.events_data.append(new_event)

        self.refresh_list() # ? 추가된대로 리스트 재갱신
        
        self.set_widgets_state("disabled")
        messagebox.showinfo("알림", "이벤트가 저장되었습니다.")

    def unlock_for_update(self):
        """이벤트 수정 버튼 클릭 시 잠금 해제"""
        if not self.current_event_id:
            messagebox.showwarning("주의", "수정할 이벤트를 선택해주세요.")
            return
        self.set_widgets_state("normal")

    def delete_event(self):
        """고유 ID를 기준으로 현재 선택된 이벤트 삭제"""
        if not self.current_event_id:
            messagebox.showwarning("주의", "삭제할 이벤트를 선택해주세요.")
            return
            
        self.events_data = [m for m in self.events_data if m["id"] != self.current_event_id] # ! 리스트 필터링 = 삭제할 이벤트(현재 선택한, 현재의 current_event_id를 가지고 있는 이벤트가 아닌 이벤트 데이터만 리스트에 다시 집어넣음)
        
        self.current_event_id = None
        self.prepare_new_event()
        self.refresh_list() # 이벤트가 삭제된 후 리스트 재갱신
        messagebox.showinfo("알림", "이벤트가 삭제되었습니다.")

if __name__ == "__main__":
    root = tk.Tk()
    app = eventApp(root)
    root.mainloop()