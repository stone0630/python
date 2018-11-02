
# -*- coding: utf-8 -*-
import os


# 递归函数案例
def get_all_file(path, sp=''):
    # 目录层级
    sp += '  '
    for i in os.listdir(path):
        absPath = os.path.join(path, i)
        if os.path.isdir(absPath):
            print(sp + '目录:%s' % i)
            get_all_file(absPath, sp)
        else:
            print(sp + '文件:%s' % i)


path = os.path.join(os.getcwd(), 'dir')
get_all_file(path)