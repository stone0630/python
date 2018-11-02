# -*- coding: utf-8 -*-
import win32api
import win32con
import time

while True:

    # 模拟键盘windows键点击事件
    win32api.keybd_event(91, 0, 0, 0)

    # 模拟键盘D键点击事件
    win32api.keybd_event(77, 0, 0, 0)

    time.sleep(0.1)

    # 模拟windows键 up事件
    win32api.keybd_event(91, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(77, 0, win32con.KEYEVENTF_KEYUP, 0)

    time.sleep(3)


# 以上是简单举例具体请查看键盘码表


