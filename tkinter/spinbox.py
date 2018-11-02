# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')
# increment 代表步长,values不能和from_=0, to=20, increment=2 同时使用
# sb = Spinbox(root, values=(1,3,5,7,9))
# 定义变量
v = StringVar()
# textvariable 绑定变量
sb = Spinbox(root, from_=0, to=20, increment=2, textvariable=v)
sb.pack()
# 给变量赋值
v.set(10)

def show():
    # 获取Spinbox的值
    print(sb.get())
    print(v.get())

Button(root, text='获取Spinbox值', command=show).pack()




root.mainloop()