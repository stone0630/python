# -*- coding: utf-8 -*-

'''
递归调用： 一个函数，调用了自身，称为递归调用
递归函数：一个调用自身的函数称为递归函数
'''


# 例如, 常规函数:

def sum1(num):
    count = 0
    for i in range(1, num + 1):
        count += i
    return count

res = sum1(5)
print(res)


# 此函数为递归函数 求和
def sum2(num):
    if num == 1:
        return num
    else:
        return num + sum2(num - 1)
print(sum2(5))


def sum3(num):
    if num == 0:
        return 0
    return num + sum3(num - 1)

print(sum3(5))

