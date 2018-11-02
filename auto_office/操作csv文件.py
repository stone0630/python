# -*- coding: utf-8 -*-
import csv
import os


def read_csv(file):
    lists = []
    with open(file) as fp:
        # 使用csv 读取csv文件内容
        obj = csv.reader(fp)
        # 读取的结果是一个对象
        for i in obj:
            lists.append(i)
    return lists


def write_csv(path, data):
    with open(path, 'w') as fp:
        wr = csv.writer(fp)
        for i in data:
            wr.writerow(i.strip())
    print('恭喜，写入完成!')
    return 1


file = os.path.join(os.getcwd(), 'csv_files/阿里云机器梳理20180803.csv')

lists = read_csv(file)

path = os.path.join(os.getcwd(), 'csv_files/new_csv.csv')
write_csv(path, lists)

