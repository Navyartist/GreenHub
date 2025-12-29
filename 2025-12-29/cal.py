from tkinter import *
from tkinter import ttk


키패드 = Tk()
frm = ttk.Frame(키패드, padding=10)

frm.grid()

기호 = '+'
숫자1 = '1'
숫자2 = '3'

ttk.Label(frm, text="calculator").grid(column=0, row=5)
ttk.Button(frm, text="Quit", command=키패드.destroy).grid(column=1, row=5)

ttk.Button(frm, text=f"1").grid(row=0,column=0)
ttk.Button(frm, text=f"2").grid(row=0,column=1)
ttk.Button(frm, text=f"3").grid(row=0,column=2)

ttk.Button(frm, text=f"4").grid(row=1,column=0)
ttk.Button(frm, text=f"5").grid(row=1,column=1)
ttk.Button(frm, text=f"6").grid(row=1,column=2)

ttk.Button(frm, text=f"7").grid(row=2,column=0)
ttk.Button(frm, text=f"8").grid(row=2,column=1)
ttk.Button(frm, text=f"9").grid(row=2,column=2)

키패드.mainloop()