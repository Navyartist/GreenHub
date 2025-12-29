import tkinter as tk

# 1. 메인 창 생성 (Class로부터 객체 생성)
root = tk.Tk() # tk로부터 클래스 Tk 가져오기
root.title("스마트 도서관 시스템") # 창 이름
root.geometry("400x300") # 창 크기를 설정

# 첫 번째 라벨
label1 = tk.Label(root, text="북", fg="blue") # text = 라벨내에 쓸 내용, fg = 글자색
label1.pack(side='top') # 화면에 배치

label2 = tk.Label(root, text="서", fg="purple")
label2.pack(side='left')

label3 = tk.Label(root, text="동", fg="green")
label3.pack(side='right')

label4 = tk.Label(root, text="남", fg="red")
label4.pack(side='bottom') # 화면에 배치
# 기본 label2.pack()면 위아래 순서대로 배치
# label2.pack(side='left')면 왼쪽부터 순서대로 라벨들이 배치됨
# label4.grid(row=0, column=1)


root.mainloop()


# # 3. 버튼 부품 (동작/Method 연결 예정)
# button = tk.Button(root, text="대여하기")
# button.pack()

# # 4. 실행 (전원 버튼 누르기)
# root.mainloop()