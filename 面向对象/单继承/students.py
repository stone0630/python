# -*- coding: utf-8 -*-

from person import Person


# Students类继承Person类，此时拥有Person类的所有属性和函数
class Students(Person):
    def __init__(self, name, age, school):
        # 调用父类中的__init__

        # 第一种写法 (只适合单继承)
        # super(Students, self).__init__(name=name, age=age)

        # 第二种写法 (只适合单继承，2.0版本不支持)
        # super().__init__(name=name, age=age)

        # 第三种写法
        Person.__init__(self, name=name, age=age)

        # 定义自己的属性
        self.school = school