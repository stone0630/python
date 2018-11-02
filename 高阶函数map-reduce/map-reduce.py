# -*- coding: utf-8 -*-
from functools import reduce
'''
大数据 map（进行拆分） reduce（进行合并）

google的mapreduce

'''


# python内置了map()和reduce()函数
# 原型 map(fn, lsd)  参数一是函数， 参数二是序列
# 功能： 将传入的的函数依次作用在序列中的每一个元素，并把结果作为新的Iterator返回
# map()


# 将字符串的序列转换为int类型的
def char_to_int(chr):
    return int(chr)


def int_to_char(num):
    return str(num)

list1 = ['1', '22', '111']
list2 = [1, 4, 3, 4]

res = map(char_to_int, list1)
# 类似于 char_to_int('1'), char_to_int('22'), char_to_int('111')
print res, list(res)

res2 = map(int_to_char, list2)
print res2


# reduce(fn, lsd) 参数是1是函数， 参数2是列表
# 功能: 一个函数作用在序列上，这个函数必须接受两个参数， reduce把结果继续和序列的下一个元素累计运算
# reduce(f, [a,b,c]) ----> f(f(f(a,b),c),d)

# 求一个序列的和
list3 = [1, 2, 3, 4, 5]


def mysum(a, b):
    return a + b

res3 = reduce(mysum, list3)

print res3



