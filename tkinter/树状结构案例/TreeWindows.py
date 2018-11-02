# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import ttk
import os
import chardet


class TreeWindows(Frame):
    def __init__(self, master, path, infowindow):
        self.infoWindow = infowindow
        frame = Frame(master)
        frame.grid(row=0, column=0)

        self.tree = ttk.Treeview(frame, height=25)
        self.tree.pack(side=LEFT, fill=Y)
        values = self.path_filter(path)
        root = self.tree.insert('', END, text=self.get_filename(path), open=True, values=values)
        # 执行循环插入函数
        self.loadTree(path, root)

        self.sc = Scrollbar(frame)
        self.sc.pack(side=RIGHT, fill=Y)

        # 绑定treeview和scrollbar,是文本和滚动条相互生效
        self.sc.config(command=self.tree.yview)

        self.tree.config(yscrollcommand=self.sc.set)


        # 给tree绑定事件
        self.tree.bind('<<TreeviewSelect>>', self.func)

    # tree点击事件处理
    def func(self, event):
        # 获取被选中的列表对象id
        v = event.widget.selection()
        # for sv in self.v:
        #     file = self.tree.item(sv)['text']
        #     print(file)
        #
        # 根据对象id获取这个对象的字典信息，比如：text
        entryname = self.tree.item(v)['text']
        value = self.tree.item(v)['values'][0]
        # 给entry设置内容
        self.infoWindow.Ventry.set(entryname)
        res_path = self.path_filter_to(value).strip('\\')
        print(res_path)
        if not os.path.isdir(res_path):
            # 此处注意文件编码问题
            if res_path.split('.').pop() not in ['txt', 'py', 'xml']:
                print('不支持此文件格式')

            else:
                if self.get_coding(res_path) != 'utf-8':
                    # 先删除文本内容然后在插入
                    self.infoWindow.text.delete('1.0', 'end')
                    # python 3中只有unicode str，所以把decode方法去掉了。你的代码中，f1已经是unicode str了，
                    # 不用decode。如果文件内容不是unicode编码的，要先以rb二进制方式打开，读入比特流，再解，中文就不乱码了
                    with open(res_path, 'rb') as fp:
                        for line in fp.readlines():
                            self.infoWindow.text.insert(INSERT, line.decode())

                else:
                    self.infoWindow.text.delete('1.0', 'end')
                    with open(res_path, 'r', encoding='UTF-8') as f:
                        for line in f.readlines():

                            self.infoWindow.text.insert(INSERT, line)

                # with open(res_path, 'r', encoding='UTF-8') as fp:
                #     for line in fp.readlines():
                #         self.infoWindow.text.insert(INSERT, line)

# 循环插入目录
    def loadTree(self, path, parent):

        for filename in os.listdir(path):
            # 获取当前文件的绝对路径
            abs_path = os.path.join(path, filename)
            # 向父树枝添加树枝
            tree_n = self.tree.insert(parent, END, text=self.get_filename(abs_path), values=self.path_filter(abs_path))
            # 判断当前文件夹是否是文件夹如果是则继续调用函数添加子树枝
            if os.path.isdir(abs_path):
                self.loadTree(abs_path, tree_n)

    # 获取路径最后一级的文件名
    def get_filename(self, path):

        res = path.split('\\')[-1]

        return res

    # 把路径的\替换为_
    def path_filter(self, path):
        new_path = ''
        for i in path.split('\\'):
            new_path += ('%s!' % i)
        return new_path

    # 把路径中的_替换为\
    def path_filter_to(self, path):
        new_path = ''
        for i in path.split('!'):
            new_path += ('%s\\' % i)
        return new_path

    # 获取文件编码格式
    def get_coding(self, file):
        with open(file, 'rb') as fp:
            res = fp.read(50)
            return chardet.detect(res)['encoding']