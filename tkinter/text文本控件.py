# -*- coding: utf-8 -*-
from tkinter import *

root = Tk()

root.title('RadioButton')

root.geometry('400x300+400+20')

# 创建Frame
fm = Frame(root, width=50, height=8)
fm.pack()

# 文本框在frame内创建
text = Text(fm, width=50, height=8)
text.pack(side=LEFT, fill=Y)

str = 'On October 18, TÜV Rheinland, a global leader for independent inspection services, unveiled the plaque for its Internet-of-Things Excellence Center in Longhua, Shenzhen to mark its official opening.On October 18, TÜV Rheinland, a global leader for independent inspection services, unveiled the plaque for its Internet-of-Things Excellence Center in Longhua, Shenzhen to mark its official opening.On October 18, TÜV Rheinland, a global leader for independent inspection services, unveiled the plaque for its Internet-of-Things Excellence Center in Longhua, Shenzhen to mark its official opening.'

# 插入字符串
text.insert(INSERT, str)

# 删除文本内容
# text.delete('1.0', 'end')

# 滚动条在frame内创建
scroll = Scrollbar(fm)
scroll.pack(side=RIGHT, fill=Y)

# 是文本和滚动条相互生效
scroll.config(command=text.yview)
text.config(yscrollcommand=scroll.set)



root.mainloop()