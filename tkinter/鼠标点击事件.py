# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')


def run(event):
    print(event.x, event.y)

btn = Button(root, text='left_click')
# 鼠标左击
# Double-Button-1 鼠标左键双击
# Triple-Button-1 鼠标左键三击
btn.bind("<Button-1>", run)

btn.pack()


root.mainloop()