# -*- coding: utf-8 -*-


class Person(object):
    def feedcat(self, cat):
        print '给你'
        cat.eat()

    def feeddog(self, dog):
        print '给你'
        dog.eat()

    def feedany(self, any):
        print '给你'
        any.eat()