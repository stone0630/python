# -*- coding: utf-8 -*-
import win32com
import win32com.client
import os


def writePptFile(path):
    # 规定要创建的文件为ppt格式
    ppt = win32com.client.Dispatch('PowerPoint.Application')
    ppt.Visible = True

    # 增加一个ppt文件
    pptFile = ppt.Presentations.Add()

    # 创建页 第一个1表示第一页， 第二个1表示页面主题
    page1 = pptFile.Slides.Add(1, 1)
    # Shapes[0] 向第一页中的第一个框里插入文本
    frame1 = page1.Shapes[0].TextFrame.TextRange
    frame1.Text = '爱如少年'
    # Shapes[1] 向第一页中的第二个框里插入文本
    frame2 = page1.Shapes[1].TextFrame.TextRange
    frame2.Text = '爱如少年的Python-PPT'

    # 创建页 第一个1表示页数， 第二个1表示页面主题
    page2 = pptFile.Slides.Add(2, 2)
    # Shapes[0] 向第一页中的第一个框里插入文本
    frame1 = page2.Shapes[0].TextFrame.TextRange
    frame1.Text = '爱如少年'
    # Shapes[1] 向第一页中的第二个框里插入文本
    frame2 = page2.Shapes[1].TextFrame.TextRange
    frame2.Text = '爱如少年的Python-PPT'

    # 保存文件
    pptFile.SaveAs(path)
    pptFile.Close()
    ppt.Quit()



def runwiteppt():
    path = os.path.join(os.getcwd(), 'file\\wite.pptx')
    writePptFile(path)

runwiteppt()