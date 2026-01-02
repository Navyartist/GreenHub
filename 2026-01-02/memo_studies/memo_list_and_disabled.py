import tkinter as tk
from tkinter import messagebox
import uuid

class MemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Memo Pad")
        self.root.geometry("500x600")

        # --- 데이터 저장소 (고유 ID를 포함한 리스트 구조) ---
        # 기존 구조에서 id라는 고유 key 역할을 추가하고 제목이 같아도 id가 다르면 서로 다른 메모로 취급되도록 재구성
        self.memos_data = [
            {"id": str(uuid.uuid4()), "제목": "첫 번째 메모", "내용": "이것은 메모의 내용입니다."},
            {"id": str(uuid.uuid4()), "제목": "회의록", "내용": "오후 2시 팀 회의 예정"},
            {"id": str(uuid.uuid4()), "제목": "쇼핑 리스트", "내용": "우유, 달걀, 빵"}
            # ! uuid4: uuid라는 고유 아이디 생성 메서드의 종류중 하나. 1부터 5까지 있고, 4는 완전 랜덤 난수로 id를 만든다.
            # ! 그냥 겹치지 않는 id = uuid4, 만든 자의 정보, 만들어진 시간 관련 정보가 추가 필요한 id = uuid1등.
            # ! notion같은 페이지 생성자가 함께 나와있는 구현은 uuid1이 적합할듯하다. 흔히 보는 메모앱처럼 만들어진 시간만 나오게 하는 방법도 찾아보면 있을것같다.
        ]
        
        # 현재 선택된 메모의 id를 추적하기 위한 변수
        self.current_memo_id = None

        self.setup_ui()
        self.refresh_list()

    def setup_ui(self):
        # 1. 메인 컨테이너 (좌우 구분)
        self.main_container = tk.Frame(self.root)
        self.main_container.pack(fill="both", expand=True)
        # ? fill: 창을 꽉 채울건지, 아닌지에 대한 설정 기능. both, x, y가 있고, x면 x축만 꽉 채우고, y면 y축만 채운다. both면 x,y 둘다
        # ? expand: 사용자가 임의로 창 크기를 키우면 컨테이너 크기가 그에 따라갈 것인지 결정
        # 2. 왼쪽 패널 (세로로 긴 메모 이름 리스트)
        self.left_panel = tk.Frame(self.main_container, width=150)  # ? 적당한 너비를 지정
        self.left_panel.pack(side="left", fill="y")

        self.list_label = tk.Label(self.left_panel, text="메모 목록") # ? left 패널에 집어넣을 리스트 패널
        self.list_label.pack(pady=10) # ? pack: 정렬. padding을 y=10만큼 줄것

        self.memo_listbox = tk.Listbox(self.left_panel, selectmode="single") # ? selectmode: 항목중 1개만 선택 (마우스 커서 상관x)
        self.memo_listbox.pack(fill="both", expand=True, padx=5, pady=5)
        self.memo_listbox.bind('<<ListboxSelect>>', self.on_select_memo) # ? <<ListboxSelect>> 리스트가 선택되었다. MemoApp의 on_select_memo 함수를 실행해라

        # 3. 오른쪽 패널 (입력창 및 버튼)
        self.right_panel = tk.Frame(self.main_container) # ? 메인 컨테이너 내부에 Frame을 하나더 만든다 (제목, 내용 입력/ 버튼 만들기용)
        self.right_panel.pack(side="right", fill="both", expand=True) # 제목이니까 잘 보이게 폰트 크기 지정

        # 상단: 메모 이름 입력
        tk.Label(self.right_panel, text="메모 제목", bg="white").pack(anchor="w", padx=10, pady=(10, 0)) # ? anchor=앵커, 닻. 동서남북으로 내용물을 어느 방향으로 붙일지를 결정하는 고정 장치
        self.title_entry = tk.Entry(self.right_panel, font=(12))
        self.title_entry.pack(fill="x", padx=10, pady=5)

        # 중간: 메모 내용 입력
        tk.Label(self.right_panel, text="메모 내용", bg="white").pack(anchor="w", padx=10)
        self.content_text = tk.Text(self.right_panel, font=(11), undo=True) # ? undo: ctrl + z 등의 되돌리기 기능을 허용해줌(True)
        self.content_text.pack(fill="both", expand=True, padx=10, pady=5)

        # 하단: 버튼 프레임
        self.button_frame = tk.Frame(self.right_panel) # ? 버튼이 많을 때 버튼의 설정을 따로 지정해 한번에 관리하게 해줌. 
        self.button_frame.pack(fill="x", pady=10)

        btn_config = {"width": 8, "pady": 5}
        
        self.btn_add = tk.Button(self.button_frame, text="메모추가", command=self.prepare_new_memo, **btn_config) # ! **btn_config(kw 인자 자리): 딕셔너리 형태인 btn_config를 kw 형태로 풀어서 전달하라는 의미
        self.btn_save = tk.Button(self.button_frame, text="메모저장", command=self.save_memo, **btn_config)
        self.btn_delete = tk.Button(self.button_frame, text="메모삭제", command=self.delete_memo, **btn_config)
        self.btn_update = tk.Button(self.button_frame, text="메모수정", command=self.unlock_for_update, **btn_config)

        self.btn_add.grid(row=0, column=0, padx=5)
        self.btn_save.grid(row=0, column=1, padx=5)
        self.btn_delete.grid(row=0, column=2, padx=5)
        self.btn_update.grid(row=0, column=3, padx=5)
        
        self.button_frame.columnconfigure((0, 1, 2, 3), weight=1) # ? 다른 기능인 pack의 fill=x같은 기능

    def refresh_list(self): # 메모 추가시마다 리스트박스(순서-메모이름 구조)를 실시간으로 갱신시킴
        """리스트박스를 리스트 데이터로 갱신"""
        self.memo_listbox.delete(0, tk.END) # ! 기존 (새 메모 추가나 수정, 삭제전) 메모 제목(리스트박스의 리스트)을 싸그리 지우기 -> 바뀐 데이터(memos_data)로 리스트에 다시 집어넣기.
        # ? delete(시작할 위치, 끝낼 위치) 지정한 범위의 리스트박스-리스트 항목들을 지운다. 범위는 인덱스로 계산
        for memo in self.memos_data: # ? memos_data (리스트 안의 딕셔너리 요소 구조)에서 각 딕셔너리들을 하나씩 꺼내오기
            self.memo_listbox.insert(tk.END, memo["제목"]) # ? 각 딕셔너리의 '제목' value를 왼 패널 리스트에 재추가

    def on_select_memo(self, event): 
        """리스트에서 항목 선택 시 호출"""
        selection = self.memo_listbox.curselection() # ? Current Selection(현재 선택한 것)의 인덱스 번호들이 몇인지 반환해라. (튜플로 반환)
        if selection: # 튜플의 맨 첫번째 인덱스
            index = selection[0]
            # 인덱스를 통해 데이터 리스트에서 해당 메모 객체를 가져옵니다.
            selected_memo = self.memos_data[index] 
            
            self.current_memo_id = selected_memo["id"] # ? 현재 선택한 메모의 id에 해당하는 제목과 내용을 보여줌
            title = selected_memo["제목"]
            content = selected_memo["내용"]
            
            self.title_entry.config(state="normal") # entry 등의 위젯의 설정을 바꾸려면 추가로 config를 붙여 사용한다
            self.content_text.config(state="normal")

            self.title_entry.delete(0, tk.END) # ? 기존 내용을 지우고, 선택한 메모의 제목과 내용을 집어넣기
            self.title_entry.insert(0, title) 
            self.content_text.delete("1.0", tk.END)
            self.content_text.insert("1.0", content)

            self.title_entry.config(state="disabled")
            self.content_text.config(state="disabled")

    def prepare_new_memo(self):
        """새 메모 작성을 위한 준비 (현재 선택 ID 초기화)"""
        self.current_memo_id = None # 새로운 메모에 id를 새로 부여하기 위해 설정
        self.title_entry.config(state="normal")
        self.content_text.config(state="normal") # 두 entry 위젯에 글자를 입력/삭제등 편집할 수 있게 허용
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)
        self.title_entry.focus() # ? 사용자가 제목을 바로 입력할 수 있게 title_entry 위젯에 커서 이동 (포커스)

    def save_memo(self):
        """메모 저장 (ID가 있으면 수정, 없으면 신규 추가)"""
        title = self.title_entry.get()
        content = self.content_text.get("1.0", tk.END).strip()
        
        if not title:
            messagebox.showwarning("주의", "제목을 입력해주세요.")
            return

        if self.current_memo_id: # id가 있을 때 (기존 메모일 때)
            # 기존 메모 수정
            for memo in self.memos_data: # refresh_list와 반복 동일하게
                if memo["id"] == self.current_memo_id: # ? 현재 리스트중 같은 id가 있으면 = 그것은 기존 메모의 수정이란 의미
                    memo["제목"] = title
                    memo["내용"] = content
                    break
        else:
            # 신규 메모 추가 (제목이 같아도 새로운 id 부여)
            new_memo = { # ? 새롭게 추가할 메모 데이터
                "id": str(uuid.uuid4()),
                "제목": title,
                "내용": content
            }
            self.memos_data.append(new_memo)

        self.refresh_list() # ? 추가된대로 리스트 재갱신
        
        self.title_entry.config(state="disabled")
        self.content_text.config(state="disabled")
        messagebox.showinfo("알림", "메모가 저장되었습니다.")

    def unlock_for_update(self):
        """메모 수정 버튼 클릭 시 잠금 해제"""
        if not self.current_memo_id:
            messagebox.showwarning("주의", "수정할 메모를 선택해주세요.")
            return
        self.title_entry.config(state="normal")
        self.content_text.config(state="normal")
        self.content_text.focus()

    def delete_memo(self):
        """고유 ID를 기준으로 현재 선택된 메모 삭제"""
        if not self.current_memo_id:
            messagebox.showwarning("주의", "삭제할 메모를 선택해주세요.")
            return
            
        self.memos_data = [memo for memo in self.memos_data if memo["id"] != self.current_memo_id] # ! 리스트 필터링 = 삭제할 메모(현재 선택한, 현재의 current_memo_id를 가지고 있는 메모가 아닌 메모 데이터만 리스트에 다시 집어넣음)
        
        self.current_memo_id = None
        self.prepare_new_memo()
        self.refresh_list() # 메모가 삭제된 후 리스트 재갱신
        messagebox.showinfo("알림", "메모가 삭제되었습니다.")

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoApp(root)
    root.mainloop()