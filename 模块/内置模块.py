# -*- coding: utf-8 -*-
import sys, os

# 直接引入自定义模块
import login

# 注意：从文件引入具体的函数是不会执行函数体以外的代码
from login import check


# 引入包模块，放置模块重名以及函数重名
import view.login

# 接收 文件名 以及所有后面的参数
print (sys.argv)

login.check()

print ("***" * 20)

check()

print ("***" * 20)
# 执行包包块
view.login.check()

#
# with open(os.path.join(os.getcwd(), 'login.py'), 'r') as fp:
#     print os.path.join(os.getcwd(), 'login.py')
#     # 配合while 循环读取内容
#     while True:
#         lineinfo = fp.readline()
#         if len(lineinfo) > 0:
#             print lineinfo
#         else:
#             print ('没有了')
#             break
