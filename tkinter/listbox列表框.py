# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')

# 绑定变量
lbv = StringVar()


lb = Listbox(root, selectmode=BROWSE, listvariable=lbv)

# BROWSE 和 SINGLE 的区别在于BROWSE支持鼠标单击不放的情况下选中列表元素
# lb = Listbox(root, selectmode=SINGLE)

# EXTENDED 可以使listbox支持shift和ctrl
# lb = Listbox(root, selectmode=EXTENDED, listvariable=lbv)

# MULTIPLE 可以支持listbox多选
# lb = Listbox(root, selectmode=MULTIPLE, listvariable=lbv)


lb.pack()
# 从当前listbox最后开始插入
for i in ['11', '22', '33']:
    lb.insert(END, i)
# 从当前listbox开头开始插入
lb.insert(ACTIVE, '44')

for i in ['4', '5', '6']:
    lb.insert(ACTIVE, i)

# 删除所有数据
# lb.delete(0, END)
# 删除下标0-1
# lb.delete(0, 1)
# 删除下标为1的元素
lb.delete(1)
# 默认选中的参数
# lb.select_set(0, 1)
lb.select_set(0)


# 取消选中下标为1
# lb.select_clear(1)


# 获取被选中的参数
print('-'*20)
print('被选中的参数:%s' % lb.selection_get())
print('-'*20)
# 获取指定索引的参数值
print('索引3的参数值:%s' % lb.get(3))
print('-'*20)
# 获取被选中的索引
print(lb.curselection())
print('-'*20)
# 获取列表中元素的个数
print('列表中元素的个数:%s' % lb.size())
print('-'*20)
# 判断列表中元素是否被选中
if lb.selection_includes(0):
    print('索引为0的数据被选中返回状态为:%s' % lb.selection_includes(0))
print('-'*20)

# 获取列表中所有选项
print(lbv.get())
# 修改列表元素，如果设置多个选项需要用元组()括号
# lbv.set('123')
# lbv.set((100, '123', 'nihao'))
print('-'*20)


# 列表绑定事件
def myapp(event):
    # 用get通过下标lb.curselection()获取被选中的值
    print(lb.get(lb.curselection()))

lb.bind('<Double-Button-1>', myapp)

root.mainloop()