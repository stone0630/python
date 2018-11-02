# -*- coding: utf-8 -*-


class Base(object):
    def __init__(self, name):
        self.name = name

    def eat(self):
        print self.name + ' eat'