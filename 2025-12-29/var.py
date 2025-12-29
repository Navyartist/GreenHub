import tkinter as tk

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