import tkinter as tk

root = tk.Tk()

print(tk)
label_data = {
        "label_text" : "Hello, World",
        "label_pady" : 20,
        "label_pady" : 20
    }

#? 왜 매개변수 자리에 할당 연산자가 있는가?
label = tk.Label(root, text=label_data["label_text"])
label.pack(pady=20, padx=20)

#? 이름이 왜 mainloop인가
root.mainloop()

# 자기가 아는 문법과 모르는 문법을 구분해서 사용해라
# 시도부터 하고 안되면 에이전트한테 물어봐라. 모르는 건 # ? 로 써놓기
# 빠르게 큰그림을 그리는법

