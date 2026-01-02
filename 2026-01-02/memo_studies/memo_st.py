import tkinter as tk
from tkinter import messagebox

class MemoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Memo Pad")
        self.root.geometry("500x600")

        # --- 데이터 저장소 (딕셔너리) ---
        self.memos_data = {
            "첫 번째 메모": "이것은 메모의 내용입니다.",
            "회의록": "오후 2시 팀 회의 예정",
            "쇼핑 리스트": "우유, 달걀, 빵"
        }

        self.setup_ui()
        self.refresh_list()

    def setup_ui(self):
        # 1. 메인 컨테이너 (좌우 구분)
        self.main_container = tk.Frame(self.root)
        self.main_container.pack(fill="both")
        # ? fill: 창을 꽉 채울건지, 아닌지에 대한 설정 기능. both, x, y가 있고, x면 x축만 꽉 채우고, y면 y축만 채운다. both면 x,y 둘다

        # 2. 왼쪽 패널 (세로로 긴 메모 이름 리스트)
        self.left_panel = tk.Frame(self.main_container, width=150) # ? 적당한 너비를 지정
        self.left_panel.pack(side="left", fill="y")

        self.list_label = tk.Label(self.left_panel, text="메모 목록") # ? left 패널에 집어넣을 리스트 패널
        self.list_label.pack(pady=10) # ? pack: 정렬. padding을 y=10만큼 줄것

        self.memo_listbox = tk.Listbox(self.left_panel, selectmode="single", bg="blue") # ? selectmode: 항목중 1개만 선택 (마우스 커서 상관x)
        self.memo_listbox.pack(fill="both", padx=5, pady=5)
        self.memo_listbox.bind('<<ListboxSelect>>', self.on_select_memo) # ? <<ListboxSelect>> 리스트가 선택되었다. MemoApp의 on_select_memo 함수를 실행해라

        # 3. 오른쪽 패널 (입력창 및 버튼)
        self.right_panel = tk.Frame(self.main_container) # ? 메인 컨테이너 내부에 Frame을 하나더 만든다 (제목, 내용 입력/ 버튼 만들기용)
        self.right_panel.pack(side="right", fill="both")

        # 상단: 메모 이름 입력
        tk.Label(self.right_panel, text="메모 제목", bg="white").pack(anchor="w", padx=10, pady=(10, 0)) # ? anchor=앵커, 닻. 동서남북으로 내용물을 어느 방향으로 붙일지를 결정하는 고정 장치
        self.title_entry = tk.Entry(self.right_panel, font=(12)) # 제목이니까 잘 보이게 폰트 크기 지정
        self.title_entry.pack(fill="x", padx=10, pady=5)

        # 중간: 메모 내용 입력
        tk.Label(self.right_panel, text="메모 내용", bg="white").pack(anchor="w", padx=10)
        self.content_text = tk.Text(self.right_panel, font=(11), undo=True) # ? undo: ctrl + z 등의 되돌리기 기능을 허용해줌(True)
        self.content_text.pack(fill="both", padx=10, pady=5)

        # 하단: 버튼 프레임 (Grid 레이아웃 사용)
        self.button_frame = tk.Frame(self.right_panel)
        self.button_frame.pack(fill="x", pady=10)

        # 버튼 생성 (순서대로: 추가, 저장, 삭제, 수정)
        btn_config = {"width": 8, "pady": 5} # ? 버튼이 많을 때 버튼의 설정을 따로 지정해 한번에 관리하게 해줌. 
        
        self.btn_add = tk.Button(self.button_frame, text="메모추가", command=self.add_memo, **btn_config) # ! **btn_config(kw 인자 자리): 딕셔너리 형태인 btn_config를 kw 형태로 풀어서 전달하라는 의미
        self.btn_save = tk.Button(self.button_frame, text="메모저장", command=self.save_memo, **btn_config)
        self.btn_delete = tk.Button(self.button_frame, text="메모삭제", command=self.delete_memo, **btn_config)
        self.btn_update = tk.Button(self.button_frame, text="메모수정", command=self.update_memo, **btn_config)

        # 버튼 배치
        self.btn_add.grid(row=0, column=0, padx=5)
        self.btn_save.grid(row=0, column=1, padx=5)
        self.btn_delete.grid(row=0, column=2, padx=5)
        self.btn_update.grid(row=0, column=3, padx=5)
        
        self.button_frame.columnconfigure((0, 1, 2, 3), weight=1) # ? 다른 기능인 pack의 fill=x같은 기능

    # --- 기능 함수들 ---

    def refresh_list(self): # 메모 추가시마다 리스트박스(순서-메모이름 구조)를 실시간으로 갱신시킴
        """리스트박스를 딕셔너리 데이터로 갱신"""
        self.memo_listbox.delete(0, tk.END) # ? 기존 (새 메모 추가나 수정, 삭제전) 메모 제목(리스트박스의 리스트)을 싸그리 지우기 
        # ? delete(시작할 위치, 끝낼 위치) 지정한 범위의 리스트박스-리스트 항목들을 지운다. 범위는 인덱스로 계산
        for title in self.memos_data.keys(): # ! memos_data 딕셔너리 데이터에서 key는 메모의 이름, 그에 대응하는 value가 메모 내용임.
        # ! key=메모이름을 title 임시 리스트변수에 집어넣고 memo_listbox(Listbox 위젯)에 하나씩 집어넣는다(for)
            self.memo_listbox.insert(tk.END, title) # ? tk.END = "맨끝 위치까지"라는 의미
            # ? insert(인덱스, 집어넣을 메모 제목) 어느 순서에 넣을지 결정(인덱스로), 지정한 인덱스 다음으로 기존 데이터(메모제목)는 뒤로 밀려남

    def on_select_memo(self, event): 
        """리스트에서 항목 선택 시 호출"""
        selection = self.memo_listbox.curselection() # ? Current Selection(현재 선택한 것)의 인덱스 번호들이 몇인지 반환해라. (튜플로 반환)
        
        if selection: # ? 빈 튜플은 false, 내용이 있는 튜플은 true를 반환하므로 if문은 t/f 조건으로 바르게 적용됨
            index = selection[0] # 튜플의 맨 첫번째 인덱스
            title = self.memo_listbox.get(index) # ? 인덱스-메모 제목 연결됨. 여기선 get으로 메모 제목을 가져옵니다.
            content = self.memos_data.get(title, "") # ? 내용 가져오기. 메모 내용을 보여주는 좌-중간 레이아웃 부분에 상세 내용을 보여주려고
            # 입력창에 반영
            self.title_entry.delete(0, tk.END) 
            self.title_entry.insert(0, title) 
            self.content_text.delete("1.0", tk.END)
            self.content_text.insert("1.0", content) # ? 기존 오른 패널에 쓰여있던 내용을 지우고 새로운 타이틀, 컨텐츠(내용)로 갱신
            self.title_entry.config(state="disabled")
            self.content_text.config(state="disabled")
            

    def add_memo(self):
        """입력창 비우기 (새 메모 작성 준비)"""
        self.title_entry.delete(0, tk.END)
        self.content_text.delete("1.0", tk.END)
        self.title_entry.focus() # ? 타이틀 입력창으로 포커스시켜줌 (사용자가 바로 추가적인 메모를 입력할 수 있게)

    def save_memo(self):
        """새로운 메모를 딕셔너리에 저장"""
        title = self.title_entry.get()
        content = self.content_text.get("1.0", tk.END).strip() # ? 1번째 줄 0번째 칸 / strip: 문자열의 앞뒤에 붙은 불필요한 공백의 제거
        
        if title: # 타이틀이 있으면
            self.memos_data[title] = content # 메모 데이터 업데이트
            self.refresh_list() # 데이터에 따라 새롭게 갱신
            messagebox.showinfo("알림", "새 메모가 저장되었습니다.") # messagebox: 메시지 박스를 보여줌 showinfo, 괄호에는 보여줄 메세지 입력
        else:
            messagebox.showwarning("주의", "제목을 입력해주세요.")

        if title in self.memos_data[title]:
            # 제목이 중복된 메모가 있으면 물어봅니다.
            messagebox.askyesno("알림" "중복된 제목의 메모가 있습니다. 제목이 변경됩니다.")
            title = title+"(사본)"

    def delete_memo(self):
        """현재 선택된 메모 삭제"""
        title = self.title_entry.get() # 삭제할 메모의 타이틀 가져오기
        if title in self.memos_data: # 해당 타이틀이 메모에 있으면
            del self.memos_data[title] # del: 삭제
            self.add_memo() # 입력창 비우기
            self.refresh_list()
            messagebox.showinfo("알림", "메모가 삭제되었습니다.")

    def update_memo(self):
        """기존 메모 내용 수정"""
        # 저장 로직과 비슷하게 작동하되, 수정임을 알림
        self.save_memo()

if __name__ == "__main__":
    root = tk.Tk()
    app = MemoApp(root)
    root.mainloop()