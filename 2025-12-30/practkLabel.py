import tkinter as tk
# ? 왜 굳이 Tk라는 메서드를 호출했을까?
root = tk.Tk()

# ? 왜 매개변수자리에 = 할당연산자가 있는거지?
class Test_Data:
    def __init__(self, label_text, pady_value):
        self.label_text = label_text
        self.pady_value = pady_value

test_date = Test_Data("Hello, Tkinter!", 10)

label = tk.Label(root)


def create_label(text, pady):
    label = tk.Label(root, text=text)
    label.pack(pady=pady)

for _ in range(10):
    create_label(test_date.label_text, test_date.pady_value)



label.pack(pady=test_date.pady_value)
# ? 왜 메서드 이름이 loop 라는 뜻 이 담겨있을까?
root.mainloop()