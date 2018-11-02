# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')

lb1 = Label(root, text='聚焦离焦事件')

lb1.pack()


def func(event):
    print(event.x, event.y)


# <Enter> 当鼠标滚轮释放时触发事件
# <Leave> 当鼠标右键释放时触发事件
lb1.bind('<Enter>', func)
# lb1.bind('<Leave>', func)


root.mainloop()