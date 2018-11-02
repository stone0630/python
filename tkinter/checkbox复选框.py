# -*- coding: utf-8 -*-
from tkinter import *

# 创建窗口
root = Tk()

# 标题
root.title('checkbox')

# 调整窗口大小
root.geometry('400x300')

# 调整窗口位置
root.geometry('+260+50')



# def update():
#
#     if hobby1.get():
#         if '音乐' not in hobby_list:
#             hobby_list.append('音乐')
#     else:
#         if '音乐' in hobby_list:
#             hobby_list.remove('音乐')
#
#     if hobby2.get():
#         if '运动' not in hobby_list:
#             hobby_list.append('运动')
#     else:
#         if '运动' in hobby_list:
#             hobby_list.remove('运动')



def update():
    # hobby_list = ''
    # if hobby1.get():
    #     hobby_list += '音乐\n'
    #
    # if hobby2.get():
    #     hobby_list += '运动\n'
    # gethobby(hobby_list)

    hobby_list = []
    if hobby1.get():
        hobby_list.append('音乐')

    if hobby2.get():
        hobby_list.append('运动')
    return hobby_list


def gethobby():
    # 删除现有文本框内的内容
    text.delete(0.0, END)
    # 向文本框插入内容
    hobby_list = update()
    text.insert(INSERT, hobby_list)


hobby1 = BooleanVar()
# check1 = Checkbutton(root, text='音乐', variable=hobby1, command=update)
check1 = Checkbutton(root, text='音乐', variable=hobby1)
check1.grid(row=0, column=0, sticky=W)
hobby2 = BooleanVar()
# check2 = Checkbutton(root, text='运动', variable=hobby2, command=update)
check2 = Checkbutton(root, text='运动', variable=hobby2)
check2.grid(row=0, column=1, sticky=W)


# 点击按钮 command 触发事件
button = Button(root, text='获取爱好', font=('微软雅黑'), command=gethobby)
button.grid(row=0, column=2, sticky=W)



# 文本框

text = Text(root)

text.grid(row=1, columnspan=3)


# 显示窗口
root.mainloop()
