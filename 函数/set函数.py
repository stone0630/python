# -*- coding: utf-8 -*-

'''
set是存储key的不能存放value，并且是有序排列的，而字典是无序排列的
创建set需要一个list或者tuple或者dict作为输入集合
重复元素在set中会被过滤
如果传入的是字典set只会取key不取value
不能传入可变对象比如list
'''

# 本质:有序没有索引无重复的元素集合

# 实例一
set1 = set([1, 2, 3, 4, 5, 2, 4, 6, 5, 4])

# 添加元素
set1.add(10)
set1.add('1111')
set1.add((11, 12, 13))
# 删除元素
set1.remove('1111')

# set是没有索引的
for i in set1:
    print(i)

# 实例二

set2 = set((1, 2, 3, 3, 2, 1))
# 如果要插入列表可以使用update
set2.update([7, 8, 9])

print(set2)

# 实例三

set3 = set({'1': 123, '2': 355, '2': 678})

# 删除最后一个元素
set3.pop()

print(set3)


# 实例四
# 将set转换为list
list1 = list(set1)
print(list1)


# 实例四
# 求交集
a = set([1, 2, 3, 4])
b = set([5, 2, 3, 4])
# 求a和b的交集
print(a & b)
# 求a和b的并集
print(a | b)



# 实例五
# 对于字符串来说就没有顺序了
str = '这是我的set测试测试方法'
res = ''
for i in set(str):
    res += i
print(res)