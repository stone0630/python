# -*- coding: utf-8 -*-

import os
import time


def get_lrc(now_time):
    with open(os.path.join(os.getcwd(), 'file\\传奇.lrc'), encoding='utf-8') as f:
        # 方法一 获取每一行内容
        # for i in f.readlines():
        #     print(i)

        # 方法二
        text = f.read()
        # 文本以行为单位形成列表
        LrcDic = {}
        timeList = []
        for Lrcline in text.splitlines():
            # Lrcline.count('[') 以某个字符参考计数
            for i in range(Lrcline.count('[')):
                contentList = Lrcline.split(']')
                # 获取列表最后一个元素
                if i != Lrcline.count('['):
                    # contentList[-1] 获取列表中最后一个元素
                    timeNum = contentList[i].strip('[').split(':')
                    # print(timeNum[0])
                    second = float(timeNum[0]) * 60 + float(timeNum[1])
                    LrcDic[second] = contentList[-1]
        for key in LrcDic:
            timeList.append(key)
        timeList.sort()

        if now_time > timeList[-1]:
            print(now_time)
            print("该时间点没有歌词...")
        elif now_time < timeList[0]:
            print(now_time)
            print("该时间点歌唱还没有开始...")
        else:
            i = 0
            for tm in timeList:
                i += 1
                # if nowTime >= tm and nowTime < timeList[i]:
                if tm <= now_time <= timeList[i]:
                    print('%f秒对应的歌词为:%s' % (now_time, LrcDic[tm]))
                    print('下一段歌词的打印时间为%f' % timeList[i])


# 滚动歌词功能函数
def run_lrc():
    with open(os.path.join(os.getcwd(), 'file\\传奇.lrc'), encoding='utf-8') as f:
        # 方法一 获取每一行内容
        # for i in f.readlines():
        #     print(i)

        # 方法二
        text = f.read()
        # 文本以行为单位形成列表
    LrcDic = {}
    timeList = []
    for Lrcline in text.splitlines():
        # Lrcline.count('[') 以某个字符参考计数
        for i in range(Lrcline.count('[')):
            contentList = Lrcline.split(']')
            # 获取列表最后一个元素
            if i != Lrcline.count('['):
                # contentList[-1] 获取列表中最后一个元素
                timeNum = contentList[i].strip('[').split(':')
                # print(timeNum[0])
                second = float(timeNum[0]) * 60 + float(timeNum[1])
                LrcDic[second] = contentList[-1]

    for key in LrcDic:
        timeList.append(key)
    timeList.sort()
    x = 0
    for tmp_time in timeList:
        x += 1
        print(LrcDic[tmp_time])
        # 减去上一个歌词出现的时间
        time.sleep(timeList[x] - float(tmp_time))


def run_get_lrc():
    while True:
        str_now = input('请输入时间(格式为[分:秒]):')
        # str_now.count(':')  判断字符串中冒号的个数
        if ':' not in str_now or str_now.count(':') > 1:
            print('时间格式错误,请重新输入...')
        else:
            now_time = float(str_now.split(':')[0]) * 60 + float(str_now.split(':')[1])
            get_lrc(now_time)

# 滚动歌词
# run_lrc()


# 获取指定时间的歌词
run_get_lrc()