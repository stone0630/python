# -*- coding: utf-8 -*-


def func(num1, num2):
    # 预言num2不能为0，如果为0则打印内容
    assert(num2 != 0), print('num2不能为0')
    print(num1/num2)


def run():
    func(2, 0)


run()
