# -*- coding: utf-8 -*-


# 默认参数
# 定义参数默认值,如果定义了默认值，调用函数是可以不传参，如果传参则按照你输入的参数为准
def func1(name='jak', age=20):
    print(name, age)

func1()
func1('tom', 30)

# 关键字参数
# 关于函数参数填写顺序的问题，可以不按照函数定义的顺序，但是要按照以下写法来调用函数
func1(age=50, name='小明')


'''
不定长参数(*)
*arr表示接收除了第一个参数以外的所有参数（类型为元组）,arr可以自定义
如果没有指定惨的呼，他就是一个空元组
'''


def func2(name, *arr):
    print(name)
    for i in arr:
        print(i)


def func3(*tt):
    for i in tt:
        print(i)


# 求和
def func4(*tt):
    x = 0
    for i in tt:
        x += i
    print(x)

func2('11', '22', 2, (1, 2))

func3('qq', 'dd', 'rrr')

func4(1, 2, 3)


# **kwargs 传入的参数必须是关键字参数(x=1)，函数获取到的就是一个字典
def func5(**kwargs):
    print(kwargs)
    print(type(kwargs))

func5(x=1, y=2, z=3)


# *args, **kwargs 表示可以输入任意参数,参数名字可以自定义

def func6(*u, **uuu):
    print(uuu)
    for i in u:
        print(i)
func6('123132', x=1, y=2, z=3)

