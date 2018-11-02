# -*- coding: utf-8 -*-
from types import MethodType


'''
只允许添加指定的属性的值， 在定义类的时候通过__slot__方法来限制

'''


class Person(object):
    __slots__ = ('name', 'age', 'speak')


def say(self):
    print 'my name is jack'

# 添加属性
per = Person()

per.name = 'jack'
print per.name

# 添加方法
per.speak = MethodType(say, per)
per.speak()


