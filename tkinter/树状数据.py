# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')

tree = ttk.Treeview(root)
tree.pack()

# 添加一级目录
tree1 = tree.insert('', 0, '中国', text='中国', values=('f1'))
tree2 = tree.insert('', 0, '美国', text='美国', values=('f2'))
tree3 = tree.insert('', 0, '英国', text='英国', values=('f3'))


# 添加二级目录
tree1_1 = tree.insert(tree1, 0, '上海', text='上海')
tree1_2 = tree.insert(tree1, 1, '北京', text='北京')
tree2_1 = tree.insert(tree2, 0, '华盛顿', text='华盛顿')
tree3_1 = tree.insert(tree3, 0, '伦敦', text='伦敦')

# 添加三级目录

tree1_1_1 = tree.insert(tree1_1, 0, '虹桥', text='虹桥')
tree1_1_2 = tree.insert(tree1_1, 1, '浦东', text='浦东')

root.mainloop()