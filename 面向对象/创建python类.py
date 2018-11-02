# -*- coding: utf-8 -*-

'''

格式：
class 类名(父类列表)
    属性
    行为

'''


# object：称为基类或者超类
class Persion(object):
    # 定义属性(实际是定义变量)
    name = ''
    age = 0
    height = 0
    weight = 0

    # 定义方法(实际是定义函数), 方法的参数必须以self当第一个参数
    # self代表类的实例(摸个对象)
    def run(self):
        print ('run')

    def eat(self, food):
        print ('eat: ' + food)