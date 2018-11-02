# -*- coding: utf-8 -*-

import os
# 获取操作系统类型
print(os.name)

# 只有linux支持，windows不支持，打印操作系统详细信息
# os.uname()

# 获取操作系统中所有的环境变量
# print(os.environ)

# 获取操作系统中指定环境变量的值
print(os.environ['OS'])
# print(os.environ.get('PATH'))

# 获取当前目录相对路径os.curdir输出结果是一个.
# 以下打印的是当前目录下的文件列表
# print(os.listdir(os.curdir))

# 如果没有输入path默认是当前目录
# print(os.listdir())

# 获取当前目录的绝对路径
# print(os.getcwd())

# 当期目录创建文件夹
# os.mkdir(os.path.join(os.getcwd(), 'file\\test'))
# 删除文件夹
# os.rmdir(os.path.join(os.getcwd(), 'file\\test'))
# 重命名文件夹
# os.rename(os.path.join(os.getcwd(), 'file\\test'), os.path.join(os.getcwd(), 'file\\test1'))


# 获取文件属性
# print(os.stat(os.path.join(os.getcwd(), 'file\\test1')))

# 删除文件
# os.remove(os.path.join(os.getcwd(), 'file\\test4.txt'))

# system运行shell命令
# os.system('cmd')

# 打开记事本
# os.system('notepad')

# 关闭windows进程
# os.system("taskkill /f /im notepad.exe")

# popen运行shell命令二
# print(os.popen('ipconfig"').read())


# abspath获取相对路径的绝对路径
print(os.path.abspath('.'))

# split拆分路径,得到一个元组，然后获取元组的最后一个元素，其实就是获取文件名
path = os.path.split(os.path.join(os.getcwd(), 'file\\test4.txt'))
path1 = os.path.split(os.path.join(os.getcwd()))
print(path[-1])
print(path1)


# 获取文件的扩展名
path2 = os.path.splitext(os.path.join(os.getcwd(), 'file\\test4.txt'))
print(path2[-1])


# 判断文件是不是目录或文件
# 还可以判断文件或目录是否存在
print(os.path.isdir(os.path.join(os.getcwd(), 'file1')))
print(os.path.isfile(os.path.join(os.getcwd(), 'file\\test5.txt')))

# 判断目录是否存在

print(os.path.exists(os.path.join(os.getcwd(), 'file1')))
print(os.path.exists(os.path.join(os.getcwd(), 'file')))


# 获取文件大小(单位字节)

print(os.path.getsize(os.path.join(os.getcwd(), 'file\\test4.txt')))

# 获取文件所在的目录路径
path4 = os.path.dirname(os.path.join(os.getcwd(), 'file\\test3.txt'))

print(path4)


# 获取文件所在的目录的名称
name = os.path.basename(path4)

print(name)


# os模块下的文件读写
'''
os.O_RDONLY: 以只读的方式打开
os.O_WRONLY: 以只写的方式打开
os.O_RDWR : 以读写的方式打开
os.O_NONBLOCK: 打开时不阻塞
os.O_APPEND: 以追加的方式打开
os.O_CREAT: 创建并打开一个新文件
os.O_TRUNC: 打开一个文件并截断它的长度为零（必须有写权限）
os.O_EXCL: 如果指定的文件存在，返回错误
os.O_SHLOCK: 自动获取共享锁
os.O_EXLOCK: 自动获取独立锁
os.O_DIRECT: 消除或减少缓存效果
os.O_FSYNC : 同步写入
os.O_NOFOLLOW: 不追踪软链接

'''

a = os.open(os.path.join(os.getcwd(), 'file\\test4.txt'), os.O_RDWR)
x = os.read(a, 10)
print(type(x))
print(x)
os.close(a)

