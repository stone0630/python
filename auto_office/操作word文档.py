# -*- coding: utf-8 -*-
import win32com
import win32com.client
import os


# 取world文档并打印
def readWordFile(path):
    # 调用系统word功能，可以处理doc和docx两种类型的word
    myword = win32com.client.Dispatch('Word.Application')

    #  打开文件
    doc = myword.Documents.Open(path)

    # doc.Paragraphs 获取文档内容，列表形式存在
    for paragraph in doc.Paragraphs:
        # paragraph.Range.Text 获取一行内的文本内容
        line = paragraph.Range.Text
        print(line)
    # 关闭word
    doc.Close()
    # 退出word处理程序
    myword.Quit()
    print('=='*30)


# 读取world文档并另存到另外一个txt中
def writeWordFile(path, topath):
    myword = win32com.client.Dispatch('Word.Application')
    doc = myword.Documents.Open(path)
    # 将word的数据保存到另外一个文件，2表示txt文件
    doc.SaveAs(topath, 2)
    doc.Close()
    myword.Quit()


# 创建word文档
def mkWordFile(path, name):
    myword = win32com.client.Dispatch('Word.Application')
    # 让文档可见
    myword.Visible = True
    #  创建文档
    doc = myword.Documents.Add()
    # 写入内容
    # 表示从开始写入
    r = doc.Range(0, 0)
    r.InsertAfter('亲爱的:' + name)
    # 保存文件
    doc.SaveAs(path)

    # 关闭word
    doc.Close()
    # 退出word程序
    myword.Quit()


# ==========================================================
# 执行读取world文档并打印
def runreadword():
    for i in os.listdir(os.path.join(os.getcwd(), 'file')):
        path = os.path.join(os.getcwd(), 'file\\', i)
        if path.split('.').pop() == 'docx':
            print('目前阅读的文档类型是.docx')
            readWordFile(path)
        elif path.split('.').pop() == 'doc':
            print('目前阅读的文档类型是.doc')
            readWordFile(path)
        else:
            print('文件类型不支持')


# ===========================================================
# 执行读取world文档并另存到另外一个txt中
def runwriteword():
    path = os.path.join(os.getcwd(), 'file\\Galaxy-EL5.docx')
    topath = os.path.join(os.getcwd(), 'file\\Galaxy-EL5.txt')
    writeWordFile(path, topath)


# 执行创建word文档
def runaddword():
    for name in ['jam', 'jack', 'tina']:
        path = os.path.join(os.getcwd(), 'file\\', name)
        mkWordFile(path, name)


runaddword()