# -*- coding: utf-8 -*-
from functools import wraps

'''
概念： 是一个闭包，把一个函数当做参数返回一个替代版的函数，本质是一个返回函数的函数


'''


# 不传参装饰器
def say():
    print('sunk is 10 year old')

# say(-10)


def check(func):
    def inner():
        print('你好:')
        func()
    return inner()

# check(say)


# 传参的装饰器(装饰器的原理)
def age0(num):
    print("jam is %d years old" % num)


def outer(func):
    def inner(num):
        if num < 0:
            num = 0
        func(num)
    return inner

# outer(age0(-5))
a = outer(age0)
a(-10)


# 装饰器的进阶写法
def outer1(func):
    # @wraps(func)
    def inner(num):
        if num < 0:
            print('年龄输入有误，请重新输入...')
            return
        func(num)
    return inner


@outer1
def age1(num):
    print("jam is %d years old" % num)


# age1(10)


# 装饰器的标准写法
def outer2(func):
    # @wraps(func)
    def inner(*args, **kwargs):
        for i in args:
            if i < 0:
                print('年龄输入有误，请重新输入...')
                return
        func(*args, **kwargs)
    return inner


@outer2
def age2(num):
    print("jam is %d years old" % num)

# age2(-10)


# 装饰器的终极写法

def outer1(func):
    def wrapper(*args, **kwargs):
        # 功能代码区域

        print('欢迎光临...')
        func(*args, **kwargs)

    return wrapper


@outer1
def info(name, age):
    print('My name is %s, I age is %d' % (name, age))


info('爱如少年', 30)
