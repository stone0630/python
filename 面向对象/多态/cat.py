# -*- coding: utf-8 -*-
from base import Base


# 继承Base类
class Cat(Base):
    def __init__(self, name):
        Base.__init__(self, name=name)