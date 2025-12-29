import tkinter as tk # tkinter 쓸건데 이름이 너무 길다. 내맘대로 tk란 이름으로 쓰겠다

# from tkinter import *
# 기능자체는 1번줄이랑 같지만, 1번줄이 더 권장되는 네이밍방식
# from tkinter import ttk
# tkinter에 연관된? ttk란 모듈 가져와서 쓰겠다. 다른건 안 씀
# ttk는 기본 tkinter에서 기능을 좀더 확장한 모듈
# 더 예쁘고 세련되게 볼수있게
# ttk는 확장 모듈이라 tk만 가져오면 ttk는 못써서 따로 가져와주어야함

class App(tk.Frame):
    def __init__(self, master):
        super().__init__(master) # super는 부모 클래스
        # 부모 클래스에게 기능을 물려받겠다
        # 여기서 부모클래스는 tk.Frame
        self.pack()

        self.entrythingy = tk.Entry() # 사용자의 입력을 한줄씩 받는 위젯 생성하는 클래스 : Entry
        self.entrythingy.pack()

        self.contents = tk.StringVar()
        self.contents.set("메시지 입력") # 메세지의 기본 셋(set)
        self.entrythingy["textvariable"] = self.contents

        self.entrythingy.bind('<Key-Return>', self.print_contents)
        # 사용자가 엔터키(Return) 누르면 지정한 함수실행
    def print_contents(self, event):
        print("Hi, The current entry contest is:", self.contents.get())


root = tk.Tk()
myapp= App(root)
myapp.mainloop()