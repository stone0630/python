# -*- coding: utf-8 -*-


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self._age = age

    def hobby(self, hobby):
        return '%s 的爱好是 %s' % (self.name, hobby)

    # 返回私有属性
    def getage(self):
        return self._age
