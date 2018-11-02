# -*- coding: utf-8 -*-
import os
import time
import pygame


filePath = os.path.join(os.getcwd(), 'music/Kalimba.mp3')

# 初始化pygame
pygame.mixer.init()

# 加载音乐文件
track = pygame.mixer.music.load(filePath)

# 播放音乐
pygame.mixer.music.play()
# 播放10秒中，再结束程序
time.sleep(5)

# 暂停音乐
pygame.mixer.music.pause()

# 停止
pygame.mixer.music.stop()