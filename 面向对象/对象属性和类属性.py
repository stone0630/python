# -*- coding: utf-8 -*-
'''
对象属性：用对象名调用的属性
类属性： 用类名调用的属性

注意：
1、如果没有定义对象属性，则对象调用和类调用显示类属性的值， 对象属性优先级高于类属性
2、对象属性和类属性的名字不要重名，减少不必要的麻烦

'''


class Person(object):
    name = 'person'

    def __init__(self, name):
        self.name = name
        # pass

# 类名调用
print (Person.name)
Person.name = 'person1'
print (Person.name)

# 对象调用
per = Person('tom')
print per.name

# 删除对象
del per
