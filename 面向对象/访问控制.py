# -*- coding: utf-8 -*-

'''
在python中 __xxx 是私有变量，外部不可以访问  __xxx__ 是特殊变量外部可以访问
'''


class Persion(object):
    # 构造函数
    def __init__(self, name, age, money):
        self.name = name
        # 变量前加两个(__) 则该变量就不可以在外部被修改和访问, 变成了私有的
        self.__age = age
        self.__money__ = money

    # 通过自定义方法间接的修改私有属性的值
    def setAge(self, age):
        if age < 0:
            age = 0
        self.__age = age

    def say(self):
        # 变量前加两个(__), 在内部是可以使用的
        return 'i am %d years old' % self.__age

per = Persion('jame', 20, 10000)

print per.name
print per.say()
# 也可以这样访问，但是不建议这么干
print per._Persion__age

# 特殊变量的访问
print per.__money__

print ('***' * 10)
# 通过自定义函数修改私有变量的值
per.setAge(0)
print per.say()

# ==================================以下是@property==========================================
'''
property : 使私有属性可以像公有属性一样可以操作（读写方法还是要自己定义）

'''


class Person(object):
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    # property装饰器
    @property
    def age(self):
        return self.__age
    # 去掉下划线的setter， 方法固定以后都这么写

    @age.setter
    def age(self, age):
        if age < 0:
            age = 0
        self.__age = age

per1 = Person('jack', 10)

print per1.name, per1.age

per1.age = 20

print per1.age

