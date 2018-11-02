# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('顶层菜单')

root.geometry('400x300+400+20')
# 创建菜单条
menubar = Menu(root)
# 设置窗口菜单为menubar
root.config(menu=menubar)

# root['menu'] = menubar


def run():
    print(vLang.get())

# 创建菜单
menu1 = Menu(menubar, tearoff=False)

vLang = StringVar()

# 给菜单添加label项
for i in ['java', 'php', 'python', '退出']:
    if i == '退出':
        # 添加分割线
        menu1.add_separator()
        # 退出窗口
        menu1.add_command(label=i, command=lambda: root.quit())
    else:
        # 与add_checkbutton不同的是，同一个组内只有一个处于选中状态
        menu1.add_radiobutton(label=i, command=run, variable=vLang)

menu2 = Menu(menubar, tearoff=False)
menu2.add_command(label='用户')
menu2.add_command(label='部门')
menu2.add_command(label='角色')
# 向菜单条添加菜单选项
menubar.add_cascade(label='语言', menu=menu1)
menubar.add_cascade(label='系统管理', menu=menu2)

root.mainloop()