# coding=utf-8
import pygame
from pygame.locals import *
from sys import exit
import time
import random
import json


# 初始化一些颜色
colors = []
white = (255, 255, 255)
colors.append(white)
colors.append((0, 255, 255))
colors.append((255, 0, 0))
colors.append((255, 0, 255))
colors.append((255, 127, 0))
colors.append((255, 0, 127))
colors.append((95, 0, 191))
colors.append((0, 0, 0))

screen = pygame.display.set_mode((900, 600), 0, 32)
screen.fill(colors[0])
pygame.display.set_caption("Chapters")

# 画线
for i in range(20):
    pygame.draw.line(screen, colors[7], (0,i*30), (900,i*30), 1)
for i in range(9):
    pygame.draw.line(screen, colors[7], (i*100,0), (i*100,570), 1)
    
# 打开关卡文件
fp = open('chapter_one.json', 'w')
data_json = []

# OK 按钮的设置
pygame.font.init()
myfont = pygame.font.SysFont("Comic Sans MS", 30)
textsurface = myfont.render('OK', False, colors[7])
rect = Rect(400, 570, 100, 30)
pygame.draw.rect(screen, colors[6], rect)
screen.blit(textsurface,(435,580))

while True:
    time.sleep(1/60)
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 鼠标的事件和位置信息的获得
            mouse_event = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            if mouse_event[0]:
                # 点击左键后，得到鼠标的位置信息
                x = (mouse_pos[0]/100%9) * 100
                y = (mouse_pos[1]/30%20) * 30
                if x == 400 and y == 570:
                    textsurface = myfont.render('OK', False, colors[0])
                    screen.blit(textsurface,(435,580))
                    num = random.randint(1,6)
                    json.dump(data_json, fp)
                    exit()
                elif y <= 570:
                    numColor = random.randint(1,6)
                    data = {"PosX":x/100%9,
		            "PosY":y/30%19,
		            "color":numColor,
                    }
                    print data
                    data_json.append(data)
                    
                    rect = Rect(x+2, y+2, 97, 27)
                    pygame.draw.rect(screen, colors[numColor], rect)
   
    pygame.display.update()
