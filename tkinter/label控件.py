# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')

lb = Label(root,
           text='label',
           bg='pink',
           fg='red',
           font=('黑体', 20),
           width=20,
           height=10,
           # 文本换行
           # wraplength=1,
           # 设置换行后的对齐方式
           # justify='left'
           # 设置对齐方式
           # e s w n 东南西北 center是居中，ne是东北方向， se东南方向
           anchor='e'
           )
lb.pack()


root.mainloop()