# -*- coding: utf-8 -*-


class Persion(object):
    # 构造函数
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print ('run')

    def eat(self, food):
        print ('eat: ' + food)
        return 1

    # self解释：self代表对象自己，谁调用就代表谁
    def say(self):
        print ('my name is %s, i am %d years old' % (self.name, self.age))
        # 打印类名
        print ('我的类名是 %s' % self.__class__)
        # 通过self.__class__()创建对象
        a = self.__class__('tt', 18)

        print a.name, a.age


'''
构造函数: __init__()
在使用类创建对象的时候自动调用该构造函数
注意： 
'''
# 给对象属性赋值
per3 = Persion('jame', 28)

# 调用构造函数属性以及函数
print per3.name, per3.age, per3.eat('汉堡')

print per3.say()