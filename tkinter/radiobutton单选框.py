# -*- coding: utf-8 -*-

from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x400+400+20')


def update():
    print(r.get())

# 推荐绑定使用INT类型的变量，一组单选框必须绑定一个变量
r = IntVar()
radio1 = Radiobutton(root, text='男', value=1, variable=r, command=update)
radio1.pack()


radio2 = Radiobutton(root, text='女', value=2, variable=r, command=update)
radio2.pack()


# r = StringVar()
# radio1 = Radiobutton(root, text='男', value='男', variable=r, command=update)
# radio1.pack()
#
#
# radio2 = Radiobutton(root, text='女', value='女', variable=r, command=update)
# radio2.pack()



root.mainloop()