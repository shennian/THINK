import pygame
from sys import exit
from pygame.locals import *
import random
import json


color_index = 0
color_set = []
color_set.append((255,192,203))
color_set.append((220,20,60))
color_set.append((199,21,133))
color_set.append((139,0,139))
color_set.append((0,0,139))
color_set.append((30,144,255))
color_set.append((0,191,255))
color_set.append((0,255,0))
color_set.append((255,69,0))
color_set.append((255,0,0))
color_set.append((70,130,180))
color_set.append((123,104,238))

screen = pygame.display.set_mode((900, 600), 0, 32)
screen.fill((0, 0, 0))

with open("t.json") as data_file:
    data = json.load(data_file)
_x = 300
_y = 300
for i in data:
    _x = 300 + 5 * i["PosX"]
    _y = 300 + 5 * i["PosY"]
    rect = Rect(_x, _y, 5, 5)
    pygame.draw.rect(screen, color_set[i["color"]], rect)
    
    

targets = [[0 for j in range(180)] for i in range(160)]
for i in range(40):
    x = random.randint(0, 179)
    y = random.randint(0, 159)
    targets[y][x] = 1

for i in range(160):
    for j in range(180):
        if targets[i][j] == 1:
            rect = Rect(i*5, j*5, 5, 5)
            pygame.draw.rect(screen, (255, 255, 255), rect)
#print targets
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    pygame.display.update()
