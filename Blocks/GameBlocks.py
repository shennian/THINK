# coding=utf-8
import blocks
import os
from multiprocessing import Process
import pygame
from sys import exit
from pygame.locals import *
import random

def main_window():
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
    screen.fill(colors[7])
    pygame.display.set_caption("select chapters")
        
    # 画色块
    for i in range(3):
        for j in range(3):
            rect = Rect(i*300 + 10, j*200 + 10, 280, 180)
            num = random.randint(1,6)
            pygame.draw.rect(screen, colors[num], rect)
        
    pygame.font.init()
    myfont = pygame.font.SysFont("Comic Sans MS", 40)
    for i in range(3):
        for j in range(3):
            textsurface = myfont.render('chapter '+str(i*3+j+1), False, (0,0,0))
            screen.blit(textsurface,(j*300+100,i*200+80))
        
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_event = pygame.mouse.get_pressed()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_event[0]:
                    chapter = "chapter_one.json"
                    x = mouse_pos[0] / 300 % 3
                    y = mouse_pos[1] / 200 % 3
                    if x == 0 and y == 0:                 
                        chapter = "chapter_one.json"
                    elif x == 1 and y == 0:
                        chapter = "chapter_two.json"
                    elif x == 2 and y == 0:
                        chapter = "chapter_three.json"
                    
                    others = Process(target=game, args=(chapter,))
                    others.start()
                    others.join()                     
        pygame.display.update()
        
        
def game(file_name):
    _game = blocks.Game(file_name)
    _game.play()

if __name__ == "__main__":
    main = Process(target=main_window)
    main.start()
    main.join()
