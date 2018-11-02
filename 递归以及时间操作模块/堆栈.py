# -*- coding: utf-8 -*-
# 模拟堆栈结构

stack = []

# 压栈(向堆栈添加内容)
stack.append('a')
stack.append('b')
stack.append('c')

print(stack)

# 出栈 遵循先进后出的原理 也就是说c要先出栈，a最后 （这里只是列表举例）

print(stack.pop())
print(stack.pop())
print(stack.pop())