# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import messagebox
import requests
import re
# python3 和python2 urlretrieve的用法不通 这点请注意
import urllib.request
import os
from PIL import Image, ImageTk
import time


def download():
    global OLD_IMG_PATH
    # 获取表单数据，并去除空格
    name = entry.get().strip()
    if name == '':
        print('签名不能为空!')
        # 弹框提示
        # messagebox._show('提示', '请输入签名')
        messagebox.showinfo('提示', '请输入签名')
    elif len(name) >10:
        print('名字长度不能超过10个字符')
    else:
        print('当前设计的用户名为:%s' % name)
        url = 'http://www.uustv.com/'
        data = {
            'word': name,
            'sizes': '60',
            'fonts': 'jfcs.ttf',
            'fontcolor':  ''# 000000'
        }
        result = requests.post(url, data=data)
        result.encoding = "utf-8"
        html = result.text
        # (.*?) 是匹配所有， 注意后面的/转义符
        req = '<div class="tu">﻿<img src="(.*?)"/></div>'

        img_path = re.findall(req, html)

        img_url = url + img_path[0]


        # 获取二进制图片内容
        # img_content = requests.get(img_url).content
        # 写入文件 方式一
        # with open('{}.gif'.format(name), 'wb') as fp:
        #     fp.write(img_content)

        # 写入文件 方式二， 直接下载图片
        filename = img_path[0].split('/')[1]
        path = os.path.join(os.getcwd(), filename)
        urllib.request.urlretrieve(img_url, path)

        # 定义图片label
        img = ImageTk.PhotoImage(file=path)
        label2 = Label(root, image=img)
        label2.bm = img
        # 显示图片
        label2.grid(row=1, columnspan=3)
        os.remove(path)


# 创建窗口
root = Tk()

# 标题
root.title('签名设计')

# 调整窗口大小
root.geometry('800x600')

# 调整窗口位置
root.geometry('+260+50')
# root.geometry('800x600+260+50')

# 标签控件
label = Label(root, text='签名：', font=('华文行楷', 20), fg='red')
# grid 网格式的布局
label.grid(row=0, column=0)

# 输入框
entry = Entry(root, font=('微软雅黑', 20))
entry.grid(row=0, column=1)

# 点击按钮 command 触发事件
button = Button(root, text='确定', font=('微软雅黑'), command=download)
# button['width'] = 10
# button['height'] = 1
# sticky 对齐方式 N S W E
button.grid(row=0, column=2, sticky=E)

# 显示窗口
root.mainloop()