# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')
# fill Y表示竖向填充 X表示横向填充， side表示显示的位置
lb1 = Label(root, text='label1', bg='red').pack(fill=Y, side=LEFT)
lb2 = Label(root, text='label2', bg='yellow').pack(fill=X, side=TOP)
lb3 = Label(root, text='label3', bg='pink').pack(fill=Y, side=RIGHT)


root.mainloop()