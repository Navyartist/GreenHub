from tkinter import *
from tkinter import ttk


키패드 = Tk()
frm = ttk.Frame(키패드, padding=10)
frm.grid()
msg = StringVar(value="hi")

def change_msg1():
    msg.set("Hello")

def change_msg2():
    msg.set("World")

def change_msg3():
    msg.set("Happy")

def change_msg4():
    msg.set("Comma")

ttk.Label(frm, textvariable=msg).grid(column=0, row=0)
ttk.Label(frm, text="Calculator").grid(column=0, row=3)
ttk.Button(frm, text="Quit", command=키패드.destroy).grid(column=1, row=3)
ttk.Button(frm, text=f"1", command=change_msg1).grid(row=1,column=0)
ttk.Button(frm, text=f"2", command=change_msg2).grid(row=1,column=1)
ttk.Button(frm, text=f"3", command=change_msg3).grid(row=1,column=2)
ttk.Button(frm, text=f"4", command=change_msg4).grid(row=1,column=3)


키패드.mainloop()