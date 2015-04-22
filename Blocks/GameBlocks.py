import blocks
import os
from multiprocessing import Process
import pygame
from sys import exit
from pygame.locals import *


def main_window():

    screen = pygame.display.set_mode((900, 600), 0, 32)
    screen.fill((255, 255, 255))
    pygame.display.set_caption("select chapters")

    pygame.font.init()
    myfont = pygame.font.SysFont("Comic Sans MS", 30)
    for i in range(9):
        textsurface = myfont.render('chapter '+str(i), False, (0,0,0))
        screen.blit(textsurface,(400,i*70))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_event = pygame.mouse.get_pressed()
                mouse_pos = pygame.mouse.get_pos()
                if mouse_event[0]:
                    y = (mouse_pos[1]/70%9) * 30
                    if y == 0:
                        others = Process(target=game, args=("chapter_one.json",))
                        others.start()
                        others.join()
        pygame.display.update()


def game(file_name):
    _game = blocks.Game(file_name)
    _game.play()


'''
main = Process(target=main_window)
main.start()
main.join()
'''
if __name__ == '__main__':
    main = Process(target=main_window)
    main.start()
    main.join()
