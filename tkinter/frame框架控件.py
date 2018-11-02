# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')

# 创建fram
frm = Frame(root)
frm.pack()

# left
frm_1 = Frame(root)
Label(frm_1, text='左上', bg='red').pack(side=TOP)
Label(frm_1, text='左下', bg='pink').pack(side=BOTTOM)
frm_1.pack(side=LEFT)

# right
frm_r = Frame(root)
Label(frm_r, text='右上', bg='yellow').pack(side=TOP)
Label(frm_r, text='右下', bg='blue').pack(side=BOTTOM)
frm_r.pack(side=RIGHT)


root.mainloop()