import tkinter as tk
import datetime
import time

# 1. 메인 창 생성 (Class로부터 객체 생성)
root = tk.Tk() # tk로부터 클래스 Tk 가져오기
root.title("D-day") # 창 이름
root.geometry("400x300") # 창 크기를 설정

today = datetime.date.today() # 오늘 날짜 가져오기
이벤트날짜 = datetime.date(2025, 12, 29) # 이벤트 날짜 설정하기
디데이 = 0 # 디데이 계산할 때 쓸 integer 변수

디데이 = abs(이벤트날짜-today) # 이벤트 날짜-오늘 날짜의 절댓값을 반환
기호 = '-'

if 이벤트날짜 <= today: # 만약 이벤트 날짜가 오늘보다 이전 날짜면
    과거_이벤트_날짜 = True
    기호 = '+'

# 첫 번째 라벨
label1 = tk.Label(root, text=f"{today}", fg="blue") # text = 라벨내에 쓸 내용, fg = 글자색
label1.pack() # 화면에 배치

label2 = tk.Label(root, text=f"{이벤트날짜}", fg="purple")
label2.pack()

label3 = tk.Label(root, text=f"D{기호}{디데이.days}", fg="purple")
label3.pack()
# 화면에 배치
# 기본 label2.pack()면 위아래 순서대로 배치
# label2.pack(side='left')면 왼쪽부터 순서대로 라벨들이 배치됨
# label4.grid(row=0, column=1)


root.mainloop()


# # 3. 버튼 부품 (동작/Method 연결 예정)
# button = tk.Button(root, text="대여하기")
# button.pack()

# # 4. 실행 (전원 버튼 누르기)
# root.mainloop()