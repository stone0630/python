# -*- coding: utf-8 -*-
from father import Father
from mother import Mather


# Child类同时继承Father, Mather类
class Child(Father, Mather):
    def __init__(self, money, face):
        Father.__init__(self, money=money)
        Mather.__init__(self, face=face)


child = Child(1000, 100)
print child.money, child.face
# 父类中有相同的方法名，则执行Child(Father, Mather):中第一个对象的方法
child.func()
