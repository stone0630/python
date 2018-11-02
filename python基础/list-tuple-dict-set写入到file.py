# -*- coding: utf-8 -*-
import pickle
import os

# pickle 可以把list tuple dict set持久化写入到文件然后可以再读出来
path = os.path.join(os.getcwd(), 'file\\test3.txt')
ls1 = [1,2,3,4,'python']

with open(path, 'wb') as fp:
    pickle.dump(ls1, fp)

with open(path, 'rb') as fp1:
    a = pickle.load(fp1)
    print(a)

# 一下方法实现起来比较麻烦，不建议使用
path2 = os.path.join(os.getcwd(), 'file\\test4.txt')
ls1 = [1,2,3,4,'python']

with open(path2, 'w') as fp2:
    fp2.write(str(ls1))

with open(path2, 'r') as fp3:
    a = fp3.read()
    print(a, type(a))

    b = list(a.strip('[').strip(']').strip(' ').strip("'").split(','))
    print(b, type(b))
