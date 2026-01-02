import tkinter as tk
import datetime

class CountApp:
    def __init__(self, root):
        self.root = root
        self.root.title("이벤트 카운트")
        self.root.geometry("400x300")

        self.event_data = []
        today = datetime.date.today()

        addBtn = tk.Button(root, text=("추가"), command=new_event)
        titleEntry = tk.Entry(self)
        self.titleEntry.pack()

        self.titles = tk.StringVar() # 실시간으로 정보를 자동 업데이트해주는 특별한 변수인 StringVar
        self.titles.set("제목 입력") # 메세지의 기본 셋팅 지정
        # ! "Entry 위젯의 데이터와 StringVar 객체를 서로 연결(Binding)해주는 연결 고리 역할"
        self.titles["textvariable"] = self.titles # entrythingy로 사용자가 입력한 텍스트를 이 코드 안에 만들어둔 contents 변수에 저장함

        self.titles.bind('<Key-Return>', self.new_event)
        # CREATE : 이벤트 정보를 입력받아 새 데이터를 만든다.
        def new_event(self):
            name = input("이벤트 이름을 입력하세요: ")
            y = input("년도를 입력하세요: ")
            m = input("월을 입력하세요: ")
            d = input("일을 입력하세요: ")

            date = datetime.date(y, m, d)

            new_data = {name: date}
            self.event_data.append(new_data)

            print(f"{name} 저장 완료!")


root = tk.Tk()
app = CountApp(root)
root.mainloop()

