# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')


def run():
    print('click事件执行中。。。')

btn = Button(root,
             text='button',
             # bg='red',
             fg='blue',
             command=run,
             width=30,
             height=2
             )
btn.pack()


btn1 = Button(root, text='lambda', command=lambda: print('这个是lambda执行的命令'))
btn1.pack()

# 退出窗口
btn2 = Button(root, text='退出', command=root.quit)
btn2.pack()

root.mainloop()