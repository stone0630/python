# -*- coding: utf-8 -*-

# pywin32是操作window系统的模块

import win32api
import win32con
import win32gui


def setWallPaper(path):

    # 打开注册表 指定对应的注册表目录层级
    reg_key = win32api.RegOpenKeyEx(
    # win32con.KEY_SET_VALUE 表示要设置value
        win32con.HKEY_CURRENT_USER, 'Control Panel\\Desktop', 0, win32con.KEY_SET_VALUE
    )

    # win32con.REG_SZ 设置图片的格式 2拉伸  0居中 6适应
    # WallpaperStyle 这个是注册表项即图片的格式 这个是参数可以设置所有的注册表项
    win32api.RegSetValueEx(reg_key, 'WallpaperStyle', win32con.REG_SZ, '6')

    '''
    一下代码可以单独执行，不需要设置 reg_key 和 win32api.RegSetValueEx
    '''
    # 执行设置图片动作win32con.SPI_SETDESKWALLPAPER
    # win32con.SPIF_SENDWININICHANGE 表示立即生效
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)