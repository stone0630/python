# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')

# 绝对布局用place进行布局，窗口的变化对位置没有影响
lb1 = Label(root, text='label1', bg='red').place(x=10, y=10)
lb2 = Label(root, text='label2', bg='yellow').place(x=100, y=100)
lb3 = Label(root, text='label3', bg='pink').place(x=200, y=200)


root.mainloop()