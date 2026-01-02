import tkinter as tk

root = tk.Tk()
root.title("가로 Grid 배치")
right_panel = tk.Frame()
right_panel.pack(side='right', fill='both', expand=True)

# (라벨 텍스트, 입력창 너비) 튜플 리스트
items = [("년", 4), ("월", 2), ("일", 2)]
entries = {}

container = tk.Frame(right_panel, padx=5, pady=5)
container.pack()

# ? enumerate(items): (0, ("년", 8)), (1, ("월", 4)), ...
# ? i엔 0, 1, ... , (text, w)엔 ("년", 8), ... 가 들어감
for i, (text, w) in enumerate(items):

    # Entry 배치: 0, 2, 4, 6... 번째 열
    ent = tk.Entry(container, width=w)
    ent.grid(row=0, column=i*2)
    # Label 배치: 1, 3, 5, 7... 번째 열
    lbl = tk.Label(container, text=text)
    lbl.grid(row=0, column=i*2 + 1)
        
    entries[text] = ent # 데이터 접근용 저장

root.mainloop()