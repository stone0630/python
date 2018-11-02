# -*- coding: utf-8 -*-
import calendar

# 返回指定某年某月的日历
print(calendar.month(2018, 7))

# 返回指定年的所有日历
print(calendar.calendar(2018))

# 判断是否是闰年 返回true,否则返回false

print(calendar.isleap(2000), calendar.isleap(2018))

# 返回的第一个参数是 每个月的第一天所在的是星期几， 第二参数是所有的天数
# print(calendar.monthrange(2018, 7))

# 返回某个月以周为单位的列表(每周是一个元素)
print(calendar.monthcalendar(2018, 7))