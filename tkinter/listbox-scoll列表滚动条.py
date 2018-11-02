# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')

lb = Listbox(root, selectmode=EXTENDED)
# side指定Listbox为居左, fill指定填充满整个Y轴
lb.pack(side=LEFT, fill=Y)


# 创建滚动条
sc = Scrollbar(root)
# side指定Scrollbar为居右；fill指定填充满整个剩余区域
sc.pack(side=RIGHT, fill=Y)


# 给listbox设置滚动条
lb.configure(yscrollcommand=sc.set)
# 让listbox有滚动条的属性
sc['command'] = lb.yview


# 从当前listbox最后开始插入
for i in ['11', '22', '33', '11', '22', '33', '11', '22', '33']:
    lb.insert(END, i)
# 从当前listbox开头开始插入
lb.insert(ACTIVE, '44')

for i in ['4', '5', '6', '4', '5', '6', '4', '5', '6']:
    lb.insert(ACTIVE, i)



root.mainloop()