# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')
# orient=HORIZONTAL 代表横向排列
scale1 = Scale(root, from_=0, to=100, orient=HORIZONTAL, length=200, tickinterval=20)
scale1.pack()

# 设置scale1的值
scale1.set(30)
# 获取scale1的值
print(scale1.get())

root.mainloop()