# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')



#创建菜单条
menubar = Menu(root)

# 创建菜单
menu = Menu(menubar, tearoff=False)

for i in ['查看', '刷新', '属性']:
    menu.add_command(label=i)

menubar.add_cascade(label='功能', menu=menu)


def showmenu(event):
    # 指定显示位置
    menubar.post(event.x_root, event.y_root)
# 绑定事件，不要忘记尖括号
# 鼠标右键
root.bind("<Button-3>", showmenu)
# 鼠标滚轮
# root.bind("<Button-2>", showmenu)
# # 鼠标左键
# root.bind("<Button-1>", showmenu)


root.mainloop()