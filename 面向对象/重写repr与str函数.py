# -*- coding: utf-8 -*-
'''
重写: 将函数重新写一遍
__str__ 打印获取对象per的时候会执行str函数， 一般用于描述对象的时候会用到
__repr__ 在python解释器里面(黑屏终端)调用对象per会执行repr函数
注意：如果没有str函数时，定义了repr则会调用repr函数 即 str = repr

'''


class Persion(object):
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 打印对象per的时候会执行str函数
    def __str__(self):
        print self.name, self.age
        return '这里是str'

    def __repr__(self):
        return '这里是repr'

    def say(self):
        print 'say'

per = Persion('jame', 20)
# 打印对象
print per
