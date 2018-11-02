# -*- coding: utf-8 -*-

'''

概念: 不使用def这样的语句来定义函数， 使用lambda来创建匿名函数

特点：
1、lambda 只是一个表达式，函数体比def简单
2、lambda 主体是一个表达式，而不是代码块，仅仅只能在lambda表达式中封装简单的逻辑
3、lambda 函数有自己的命名空间， 且不能访问自由参数列表之外的货全局命名的参数

格式： lamdba 参数1，参数2， ..., 参数n，: 跟上表达式

'''

# 例如：

sum = lambda num1, num2: num1 + num2

print(sum(1, 2))