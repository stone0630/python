# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('500x300+400+20')

# 标签控件
label = Label(root, text='签名：', font=('华文行楷', 20), fg='red')
# grid 网格式的布局
label.grid(row=0, column=0)

# 输入框
entry = Entry(root, font=('微软雅黑', 20))
entry.grid(row=0, column=1)

# 点击按钮 command 触发事件
button = Button(root, text='确定', font=('微软雅黑'))
# button['width'] = 10
# button['height'] = 1
# sticky 对齐方式 N S W E
button.grid(row=0, column=2, sticky=E)



root.mainloop()