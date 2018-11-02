# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')


lb1 = Label(root, text='聚焦离焦事件')

lb1.pack()

lb1.focus_set()


# char获取键盘按钮字符，keycode获取键盘按钮对应的二进制值
def func(event):
    print("event.char=", event.char)
    print("event.keycode=", event.keycode)

# <Key>
# lb1.bind('<Key>', func)

# <Shift_L>响应特殊按键事件，比如左边的shift键
# <Shift_R>响应特殊按键事件，比如右边的shift键
# <F5><Return>回车<BackSpace>退格键
lb1.bind('<Shift_L>', func)


root.mainloop()