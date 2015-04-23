# coding=utf-8
import pygame
from pygame.locals import *
from sys import exit
import time
import random
import json


class Game():
    def __init__(self, file_name):
        self.colors = self.color_set()
        self.screen = self.init_screen()
        # 初始化bar和x,y坐标
        self.bar_x = 400
        self.bar_y = 570
        self.bar = Rect(400, 570, 100, 30)
        # 初始化block和x,y坐标
        self.block_x = 440
        self.block_y = 550
        # block的移动速度，
        self.speed_x = 0
        self.speed_y = 0
        self.block = Rect(440, 550, 20, 20)
        # 目标砖块，用二维数组存储，坐标值
        self.targetsColor = [[0 for j in range(9)] for i in range(20)]
        self.targets = self.init_targets(file_name)
        
        # 将目标砖块的二维数组draw在屏幕上
        self.display_targets()
        # 帧数控制
        self.times = 0
        # 游戏开始控制
        self.game_start = 0
        
    def init_screen(self):
        screen = pygame.display.set_mode((900, 600), 0, 32)
        screen.fill(self.colors[0])
        pygame.display.set_caption("Blocks")
        return screen
    
    def init_targets(self, file_name):
        targets = [[0 for j in range(9)] for i in range(20)]
        with open(file_name) as data_file:
            data = json.load(data_file)
        
        for i in data:
           targets[i["PosY"]][i["PosX"]] = 1
           self.targetsColor[i["PosY"]][i["PosX"]] = i["color"]
        
        return targets
    
    # 设置下一时刻block的坐标
    def set_block_position(self):
        _x = self.block_x
        _y = self.block_y  	
        _x += self.speed_x
        _y += self.speed_y       
        if _x <= 0 or _x >= 880:
            self.speed_x = -self.speed_x
        elif _y <= 0:
            self.speed_y = -self.speed_y
        # 与bar接触时的判定
        elif _y >= 550:
            if self.block_x > self.bar_x and self.block_x < self.bar_x+100:
                self.speed_y = -self.speed_y
            else:
                pygame.display.set_caption("Game Over~")
        # 将block的坐标映射在targets的二维数字上，如果值为1，表示发生碰撞
        elif self.targets[(_y+10)/30 % 20][(_x+10)/100 % 9] == 1:
            self.targets[(_y+10)/30 % 20][(_x+10)/100 % 9] = 0
            # block的状态转移
            if self.speed_x > 0 and self.speed_y > 0:
                self.speed_y = -self.speed_y
            elif self.speed_x > 0 and self.speed_y < 0:
                self.speed_y = -self.speed_y
            elif self.speed_x < 0 and self.speed_y < 0:
    	        self.speed_y = -self.speed_y
    	    elif self.speed_x < 0 and self.speed_y > 0:
    	        self.speed_y = -self.speed_y
            
    def block_move(self):    
    	time.sleep(1/60)	    
    	if self.times == 60:
           self.times = 0
        if self.times % 5 == 0:
            self.set_block_position()
            self.block.move_ip(self.speed_x, self.speed_y)
            self.block_x += self.speed_x
            self.block_y += self.speed_y    
        self.times += 1
        
    def display_targets(self):
        for i in range(20):
           for j in range(9):
               if self.targets[i][j] == 1:
                   t = Rect(j*100, i*30, 100, 30)
                   num = self.targetsColor[i][j]
                   pygame.draw.rect(self.screen, self.colors[num], t)
    
    # 初始颜色
    def color_set(self):
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
    	return colors
    	  
    def play(self):
        while True:
            self.block_move()
            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()   
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        if self.bar_x > 0:
                            self.bar.move_ip(-20,0)
                            self.bar_x -= 20
                        if self.game_start == 0:
                            self.block.move_ip(-20,0)
                            self.block_x -= 20
                        
                    elif event.key == K_RIGHT:
                        if self.bar_x < 800:
                            self.bar.move_ip(20,0)
                            self.bar_x += 20
                        if self.game_start == 0:
                            self.block.move_ip(20,0)
                            self.block_x += 20
                    elif event.key == K_SPACE:
                        if self.game_start == 0:
                            self.game_start = 1
                            self.speed_x = 1
                            self.speed_y = -1           
            pygame.draw.rect(self.screen, self.colors[7], self.bar)
            pygame.draw.rect(self.screen, self.colors[2], self.block)
            self.display_targets()
            pygame.display.flip()
            self.screen.fill((255,255,255))
    
if __name__ == "__main__":
    test = Game()
    test.play()   

                
