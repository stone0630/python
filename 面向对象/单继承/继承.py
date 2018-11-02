# -*- coding: utf-8 -*-

'''
单继承： 有两个类，a类和b类，当a类继承自b类时，a类拥有了b类的所有属性
说明：继承者叫子类， 被继承者叫父类
object类是所有类的父类，还可以称为基类或者超类
注意：如果父类中有私有属性，在子类中是不能访问的，可以间接通过函数进行访问

'''

from students import Students
from person import Person

per = Person('tt', 1)

stu1 = Students('jam', 20, '浙江理工')
print stu1.school
# 通过函数间接访问父类的私有属性
print stu1.getage()

stu = Students('tom', 19, '哈弗大学')
print stu.hobby('爬山') + '毕业于 %s' % stu.school