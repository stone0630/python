# -*- coding: utf-8 -*-

'''
__del__(self) 释放对象的时候执行析构函数， 知道就好一般不会用
'''


class Persion(object):
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 默认python会自动释放对象，减少内存空间的浪费
    def __del__(self):
        print '这里是析构函数'

    def run(self):
        print ('run')

    def eat(self, food):
        print ('eat: ' + food)

    # self解释：self代表对象自己，谁调用就代表谁
    def say(self):
        print ('my name is %s, i am %d years old' % (self.name, self.age))

per = Persion('jame', 20)

#  手动释放对象
del per


