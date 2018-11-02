# -*- coding: utf-8 -*-

import os
# 如果是二进制写入，则必须要进行编码  ，打开的时候要进行解码
path1 = os.path.join(os.getcwd(), 'file\\test.txt')
with open(path1, 'wb') as fp1:
    fp1.write('my name is 小红'.encode())

with open(path1, 'rb') as f2:
    data = f2.read()
    print(data.decode('utf-8'))
    print(type(str(data)))



# 还可以读得时候以二进制读出来， 然后进行解码写入
# 例如：
path2 = os.path.join(os.getcwd(), 'file\\test2.txt')

with open(path2, 'w', encoding='utf-8') as fp:
    res = fp.write('my name is 小红')

with open(path2, 'rb') as f:
    data1 = f.read()
    data2 = data1.decode()
    print(data1.decode(), type(data1.decode()))


