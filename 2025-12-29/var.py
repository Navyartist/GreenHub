# 내가 혼자 해석하고 작성해둔 부분
# ! 지피티의 도움을 받고 다시 공부한 부분
# ? 코드를 딱 봤을 때 궁금하다고 느끼는 부분
# * 

import tkinter as tk

# myApp은 tk.Frame이라는 클래스를 부모 클래스로서 상속받는 클래스.
class myApp(tk.Frame): # myApp= 정해진 게 아닌 내가 임의로 지어주는 클래스 이름
    def __init__(self, master): # 이 클래스를 초기화하는 법
        super().__init__(master) # super는 부모 클래스의 다른 이름이고, 이 줄 전체는 "부모가 가진 기본 설정(메모리 할당, 윈도우 연결 등)을 완료하고 자식에게 물려줄 준비를 마치라는 의미(=초기화)이다."
        # ! "또한, master 매개변수에는 이 프레임(myApp)을 포함할 **부모 위젯(예: root)**을 집어넣어준다."
        self.pack() # tk의 Button, Checkbutton, Label, Frame 위젯을 창에서 정렬하는 기능. 코드에서는 클래스 형태

        self.entrythingy = tk.Entry(self) # 사용자의 입력을 한줄씩 받는 위젯을 생성하는 tkinter 내부의 클래스 Entry()
        # entrythingy는 내가 붙인 Entry 클래스의 별명
        # ! 그냥 tk.Entry()로 두는 것보다 tk.Entry(self)로 주인을 지정해주는 것이 정석
        # ! 괄호를 비워두면 Tkinter가 자동으로 가장 최근에 만든 root 창을 주인으로 지정해버립니다.
        self.entrythingy.pack() # 여기도 정렬. pack(side='top') 옵션이 기본 셋팅

        self.contents = tk.StringVar() # 실시간으로 정보를 자동 업데이트해주는 특별한 변수인 StringVar
        self.contents.set("메시지 입력") # 메세지의 기본 셋팅 지정
        # ? textvariable은 entrythingy의 정확히 무엇인가?
        # ! "Entry 위젯의 데이터와 StringVar 객체를 서로 연결(Binding)해주는 연결 고리 역할"
        self.entrythingy["textvariable"] = self.contents # entrythingy로 사용자가 입력한 텍스트를 이 코드 안에 만들어둔 contents 변수에 저장함

        self.entrythingy.bind('<Key-Return>', self.print_contents)
        # 사용자가 객체로 띄워진 entrythingy 위젯에서 엔터키(Return)를 누르는 걸 감지하고, 예를들어 누름=True이면 함께 지정한 함수를 실행한다.

    def print_contents(self, event): # ? 이 event 매개변수는 무엇인가?
        # ! event: <Key-Return> 사건이 발생했을 때 Tkinter가 생성하여 전달해주는 종합 정보 패키지
        # ! event.x, event.y: Enter 키를 누른 그 찰나에 마우스 커서가 'Entry 위젯 내부' 어디에 있었는지의 좌표
        print("Hi, The current entry contest is:", self.contents.get()) # **'이벤트 바인딩'**

        # self.entrythingy.bind('<Key-Return>', self.print_contents)에서:
            # 사용자: "엔터키(Return)가 눌리면 print_contents 함수를 실행해줘."
            # Tkinter: "알았어. 대신 내가 그 함수를 실행할 때, **'어떤 키가 눌렸는지', '어느 위젯에서 눌렸는지' 같은 정보(event 객체)**를 매개변수로 넘겨줄 거야. 그러니까 그 정보를 받을 자리를 꼭 만들어 둬!"

        print("눌린 키:", event.keysym)      # 예: Return
        print("발생한 위젯:", event.widget)  # 예: .!entry  경로(. <= 최상위 경로(root)를 의미함) + !Tkinter가 지어준 해당 위젯의 고유한 이름. entry 위젯이 2개면 첫번째 entry 위젯은 .!entry1, 두번째 entry 위젯은 .!entry2 등으로 이름이 지어짐
        print("마우스 좌표:", event.x, event.y) # ? 정확히 어느 시점의 마우스 좌표를 반환해주는 것인가?
        # 코드 실행으로 띄워진 창에서, entrythingy 위젯을 통해 사용자가 뭔갈 입력하고 "Enter(Return)"를 눌렀을 때.
        # ! 기준점: 창의 좌상단 지점

root = tk.Tk()
myapp= myApp(root)
myapp.mainloop()

# ! 작성하신 코드에서 한 가지 더 눈여겨볼 점은 super().__init__(master) 부분입니다.
# ! 계층 구조: root (Tk 클래스인 객체)가 부모가 되고, myApp (Frame)이 그 안에 들어가는 자식이 됩니다.
# ! 독립성: 이렇게 클래스로 위젯을 감싸면(Encapsulation), 나중에 프로그램이 커졌을 때 이 myApp 클래스만 똑 떼어다가 다른 창에 붙이기가 매우 쉬워집니다.