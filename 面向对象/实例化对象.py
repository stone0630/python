# -*- coding: utf-8 -*-

class Persion(object):
    name = ''
    age = 0
    height = 0
    weight = 0

    def run(self):
        print ('run')

    def eat(self, food):
        print ('eat: ' + food)

'''
实例化对象
格式:
对象名 = 类名(参数列表)
注意： 没有参数，小括号也不能省略
'''

# 实例化一个对象(一下实例化了像个人)

per1 = Persion()
# print (per1, type(per1), id(per1))

per2 = Persion()
# print (per2, type(per2))

'''
访问对象属性
格式：对象名.属性名
赋值: 对象名.属性名 = 新值
'''

per1.name = 'tom'


print per1.name


'''
访问对象方法
格式：对象名.方法名(参数列表)
'''

per2.run()
