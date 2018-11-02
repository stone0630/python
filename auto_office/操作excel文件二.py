# -*- coding: utf-8 -*-

# 要使用该脚本需要安装一下模块
# pip install xlrd
# pip install future
# pip install pyexcel-io
# 此包可以得到有序字典，字典本身是无序的
# pip install ordereddict

# 只需要安装一下包 以上是依赖包
# pip install pyexcel
# pip install pyexcel-xls

# 有序字典
from collections import OrderedDict
from pyexcel_xls import get_data, save_data
import os


def readXlsxFile(path):
    # 定义有序字典
    dic = OrderedDict()

    # 获取整个文档的数据
    allData = get_data(path)
    for sheet in allData:
        dic[sheet] = allData[sheet]
    return dic


def writeXlsFile(path, data):
    # 定义有序字典
    dic = OrderedDict()
    # 首先对数据进行排序更新
    dic.update(data)
    # 写入数据
    save_data(path, dic)


def runReadXlsx():
    path = os.path.join(os.getcwd(), 'file\浙商测试云运维月报20180901-20180931.xlsx')
    dic = readXlsxFile(path)
    # 获取第一页的数据
    print(dic['总表'])


def runWriteXlsx():
    # 源excel文档
    path = os.path.join(os.getcwd(), 'file\浙商测试云运维月报20180901-20180931.xlsx')
    # 目标excel文档
    new_path = os.path.join(os.getcwd(), 'file\write.xls')
    # 先获取数据
    dic = readXlsxFile(path)
    # 写入数据
    writeXlsFile(new_path, dic)


runWriteXlsx()