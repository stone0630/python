# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')

# 定义并绑定变量
cv = StringVar()

com = ttk.Combobox(root, textvariable=cv)
com.pack()
# 设置下拉属性
com['value'] = ('中国', '美国', '英国')
# 设置默认值, 根据下标来设置
com.current(0)

print(cv.get())

# 获取选中的值
def run(event):
    print(com.get())

# 绑定事件
com.bind("<<ComboboxSelected>>", run)




root.mainloop()