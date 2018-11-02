# -*- coding: utf-8 -*-
import os
import time
import pygame
import win32api
import win32con
import win32gui


def play():
    pygame.mixer.init()
    musicPath = os.path.join(os.getcwd(), 'music')
    while True:
        for i in os.listdir(musicPath):
            pygame.mixer.music.load(os.path.join(musicPath, i))
            pygame.mixer.music.play()
            changePic()
            # time.sleep(10)
            pygame.mixer.music.stop()


def changePic():
    while True:
        x = 0
        for i in os.listdir(os.path.join(os.getcwd(), 'wallpaper')):
            x += 5
            path = os.path.join(os.path.join(os.getcwd(), 'wallpaper'), i)
            # 设置背景图片win32con.SPIF_SENDWININICHANGE 表示立即生效
            win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, path, win32con.SPIF_SENDWININICHANGE)
            time.sleep(5)
            print('更换下一张桌面')
        if x == 15:
            print('播放下一曲')
            break


if __name__ == '__main__':
    play()
