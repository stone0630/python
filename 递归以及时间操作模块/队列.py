# -*- coding: utf-8 -*-
import collections
# 模拟队列


queue = collections.deque()
print(queue)
# 进队
queue.append('a')
queue.append('b')
queue.append('c')

print(queue)
# 出队 先进先出
print(queue.popleft())
print(queue.popleft())
print(queue.popleft())
