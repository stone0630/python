# -*- coding: utf-8 -*-

from collections import Iterable, Iterator


def isinstance1():

    # 判断输入的内容是目标类型
    print(isinstance('123', str))

    print(isinstance([1, 2, 3], list))

    print(isinstance(1, str))

    # 以下执行结果可以看出函数也是一个对象
    def run():
        pass

    print(isinstance(run(), object))

'''
可迭代对象：可以直接作用于for循环的对象统称为可迭代对象(Iterable).
可以用于isinstance()去判断一个对象是否是Iterable对象

可以直接作用于for的数据类型一般分为两种：
1、集合数据类型，list tuple dict set string
2、是generator， 包括生成器和带yield的generator function函数

'''

print(isinstance([], Iterable))
print(isinstance((), Iterable))
print(isinstance({}, Iterable))
print(isinstance('', Iterable))
print(isinstance(set(), Iterable))




'''
迭代器：不但可以作用于for循环，还可以被next()函数不断的调用并返回下一个值
，直到最后抛出一个stopIteration错误表示无法继续返回下一个值

可以被next()函数调用并不断返回下一个值的对象称为迭代器（Interator对象）

'''
# l就是一个generator迭代器
l = (x for x in range(5))
print(next(l))

print(isinstance([], Iterator))
print(isinstance((), Iterator))
print(isinstance({}, Iterator))
print(isinstance('', Iterator))
print(isinstance(set(), Iterator))
print(isinstance(l, Iterator))


# 转成迭代器
a = iter([1,2,3,4])
print(next(a))
# 以下可以说明list tuple dict sting可以被转为迭代器
print(isinstance(iter([]), Iterator))
print(isinstance(iter(()), Iterator))
print(isinstance(iter({}), Iterator))
print(isinstance(iter(''), Iterator))


# 案例, 慢慢体会
def iter1():

    endstr = 'over'
    str = ''

    for line in iter(input, endstr):
        str += line + '\n'
        print(line)
    print(str)

isinstance1()

