# -*- coding: utf-8 -*-

'''

try ... execept...else

格式
try:
    语句
except 错误码 as e：
    语句1

except 错误码 as e：
    语句2

else:
    语句 e

注意： else语句可以省略

作用: 用来检测try下面的语句块是否有错误， 从而让except捕获错误，并进行处理，不同的错误码返回不同的错误结果

逻辑：
1、如果try下面的语句块出现错误，先匹配第一个错误码，如果匹配不上继续执行下面的匹配，
2、如果都没匹配上，那么错误将被提交到上一层的try语句或者到程序的最上层
3、如果try执行没有出现错误，则会执行else下面的语句块
4、具体错误码可以在网上查找码表

'''
# 一种错误执行一个except的错误码的操作
num = float(input())
try:
    print(3/num)
except NameError as e:
    print('没有变量')
except ZeroDivisionError as e:
    print('除数不能为0')
else:
    print('程序处理没有问题')


# 使用except而不使用任何的错误类型，常用方法
def run():
    print('========')

try:
    print(4/0)
except:
    print('程序出现异常')
    run()


# 使用except带着多种异常
try:
    5/0
except(NameError, ZeroDivisionError) as e:
    print('出现NameError或ZeroDivisionError错误')


# 使用BaseException基类进行捕获，他会捕获所有的子类的错误
try:
    5/0
except BaseException as e:
    print('异常1')


# 多级调用捕获异常,只需捕获第一级就可以捕获错误
def fun1(num):
    return print(5/num)


def fun2(num):
    fun1(num)


def fun():
    fun2(0)


try:
    fun()
except ZeroDivisionError:
    print('*****')


# try ..... execpt ......finally 无论try是否有错误都将执行语句 finally
try:
    pass
except:
    pass
finally:
    pass






