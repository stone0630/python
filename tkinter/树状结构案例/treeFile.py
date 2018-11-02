# -*- coding: utf-8 -*-

from tkinter import *

from TreeWindows import TreeWindows
from InfoWindow import InfoWindow

path = 'D:\python教程资料'

root = Tk()

root.title('文件阅读器')

root.geometry('1000x600+200+20')

infoWindow = InfoWindow(root)
# 此处注意把infoWindow对象传给了TreeWindows对象，这时TreeWindows就可以操作infoWindow对象了
TreeWindows(root, path, infoWindow)




root.mainloop()