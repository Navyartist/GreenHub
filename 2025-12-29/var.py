import tkinter as tk

class myApp(tk.Frame): # myApp: 내가 임의로 지어준 클래스 이름
    def __init__(self, master):
        super().__init__(master) # super는 부모 클래스
        # 부모 클래스에게 기능을 물려받겠다
        # 여기서 부모클래스는 tk.Frame
        self.pack()

        self.entrythingy = tk.Entry() # 사용자의 입력을 한줄씩 받는 위젯 생성하는 클래스 : Entry,
        # entrythingy = 내가 붙여준/사용할 Entry 클래스의 별명
        self.entrythingy.pack() # 정렬(pack(side='top') 기본셋

        self.contents = tk.StringVar() # 실시간으로 업데이트해주는 특별한 변수
        self.contents.set("메시지 입력") # 메세지의 기본 셋(set)
        self.entrythingy["textvariable"] = self.contents

        self.entrythingy.bind('<Key-Return>', self.print_contents)
        # 사용자가 엔터키(Return) 누르면 지정한 함수실행

    def print_contents(self, event):
        print("Hi, The current entry contest is:", self.contents.get()) # **'이벤트 바인딩'**

        # self.entrythingy.bind('<Key-Return>', self.print_contents)에서:
            # 사용자: "엔터키(Return)가 눌리면 print_contents 함수를 실행해줘."
            # Tkinter: "알았어. 대신 내가 그 함수를 실행할 때, **'어떤 키가 눌렸는지', '어느 위젯에서 눌렸는지' 같은 정보(event 객체)**를 매개변수로 넘겨줄 거야. 그러니까 그 정보를 받을 자리를 꼭 만들어 둬!"

        print("눌린 키:", event.keysym)      # 예: Return
        print("발생한 위젯:", event.widget)  # 예: .!entry  경로(. <= 최상위 경로(root)를 의미함) + !Tkinter가 지어준 해당 위젯의 고유한 이름. entry 위젯이 2개면 첫번째 entry 위젯은 .!entry1, 두번째 entry 위젯은 .!entry2 등으로 이름이 지어짐
        print("마우스 좌표:", event.x, event.y)


root = tk.Tk()
myapp= myApp(root)
myapp.mainloop()