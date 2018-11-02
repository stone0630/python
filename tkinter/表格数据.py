# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

root = Tk()

root.title('表格数据')

root.geometry('400x300+400+20')
# 创建表格
tree = ttk.Treeview(root)
tree.pack()
# 定义表头
tree['columns'] = ("姓名", '年龄', '身高', '体重')
# 设置列的宽度
tree.column('姓名', width=50)
tree.column('年龄', width=50)
tree.column('身高', width=50)
tree.column('体重', width=50)

# 设置表头并显示
tree.heading('姓名', text='姓名')
tree.heading('年龄', text='年龄')
tree.heading('身高', text='身高')
tree.heading('体重', text='体重')


def onclick(event):
    item = tree.selection()[0]
    print(tree.selection())
    print("you clicked on ", tree.item(item, "values"))


for i in range(10):
    tree.insert('', i, text='list'+str(i), values=('a' + str(i), 'b' + str(i), 'c' + str(i), 'd' + str(i)))
tree.bind("<Double-1>", onclick)

root.mainloop()