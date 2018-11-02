# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')

lb1 = Label(root, text='移动事件')

lb1.pack()


def func(event):
    print(event.x, event.y)

# <B1-Motion> 鼠标左键按住移动触发事件
# <ButtonRelease-1> 当鼠标左键释放时触发事件
# <ButtonRelease-2> 当鼠标滚轮释放时触发事件
# <ButtonRelease-3> 当鼠标右键释放时触发事件


# lb1.bind('<B1-Motion>', func)
lb1.bind('<ButtonRelease-1>', func)


root.mainloop()