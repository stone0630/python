# -*- coding: utf-8 -*-
import os
path = os.path.join(os.getcwd(), 'file\\传奇.lrc')
print(path)
# 第一种打开方式
f = open(path, 'r', encoding='utf-8')

print(f.read())
print('**'*20)
# seek 是修改光标的位置，0表示文档的开头， 因为第一次read后光标已经放到了文件的结尾，所有再次去读就是空的
f.seek(0)
# 刷新缓冲区，一般在写文件的时候会用到，默认是在文件关闭时自动刷新缓冲区
f.flush()
print(f.read())

f.close()

print('++'*20)
# 第二种打开方式，会自动关闭文档
with open(path, 'r', encoding='utf-8') as fp:
    print(fp.read())


with open(path, 'r') as fp:
    # 配合while 逐行读取内容
    while True:
        lineinfo = fp.readline()
        if len(lineinfo) > 0:
            print lineinfo
        else:
            print ('没有了')
            break
