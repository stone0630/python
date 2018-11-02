# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')


lb1 = Label(root, text='指定按键事件')

lb1.pack()

lb1.focus_set()


# char获取键盘按钮字符，keycode获取键盘按钮对应的二进制值
def func(event):
    print("event.char=", event.char)
    print("event.keycode=", event.keycode)

# 表示按下a键是触发事件
# lb1.bind('a', func)

# 组合件事件例如:<Control-Alt-b> <Shift-Up> <Control-p>等
lb1.bind('<Control-Alt-b>', func)


root.mainloop()