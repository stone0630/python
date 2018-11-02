# -*- coding: utf-8 -*-

'''
多态：一种事务的多种形态，实际就是复用类中的方法, 这样代码开起来就非常的简洁
'''

from cat import Cat

from dog import Dog

from person import Person

tom = Cat('tom')
jerry = Dog('jerry')
tom.eat()
jerry.eat()
print ('===' * 10)
# 创建人的对象，并把动物对象传递给人类
per = Person()
per.feedcat(tom)
per.feeddog(jerry)

print ('===' * 10)
# 多态：实际就是复用类中的方法，该案例中cat和dog都继承base 属于复用
#      下面对象调用同一个类中的方法，传递不同的对象，属于复用
per.feedany(tom)
per.feedany(jerry)