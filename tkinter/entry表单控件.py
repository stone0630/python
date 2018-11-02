# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')


def getvalue():
    print(vname.get())
    print(entry1.get())
    print('**'*10)
    print(vpasswd.get())
    print(entry2.get())


vname = StringVar()
lb1 = Label(root, text='用户名:')
lb1.pack()
entry1 = Entry(root,textvariable=vname)
entry1.pack()
vname.set('admin')


vpasswd = StringVar()
lb2 = Label(root, text='密码:')
lb2.pack()
entry2 = Entry(root, show='*', textvariable=vpasswd)
entry2.pack()


btn = Button(root, text='获取账号', command=getvalue)
btn.pack()

root.mainloop()