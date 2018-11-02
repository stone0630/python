# -*- coding: utf-8 -*-
import datetime
import time


time.clock()
# 计算程序cpu占用时间（单位秒），windows和linux是不一样的，windows是计算从第一次执行time.clock()后开始计算的，
# linux则不是，linux是重程序开始时计算的
time.sleep(2)
print(time.clock())


# 获取当前时间
y1 = datetime.datetime.now()
str1 = y1.strftime('%Y-%m-%d %X')
print(y1, type(y1))
print(str1)


# 获取指定时间

y2 = datetime.datetime(2018, 10, 1, 12, 32, 23, 123456)
print(y2, type(y2))

# 把时间转换为字符串
y3 = y2.strftime('%Y-%m-%d %X')
print(y3, type(y3))


# 将格式化后的字符串转换为datetime对象
y4 = datetime.datetime.strptime(y3, '%Y-%m-%d %X')
print(y4, type(y4))


# 注意只有datetime对象可以进行减法操作
y5 = y1 - y4
print(y5, type(y5))
# 取返回值中的详细项的值,其中y5.seconds是间隔天数以外的秒数
print(y5.days, y5.seconds)
