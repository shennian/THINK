import pygame
from sys import exit
from pygame.locals import *
import random
import json

class Color():
    def __init__(self):
        self.brush = self.setup()

        
    def setup(self):
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
        return color_set


class Map():
    def __init__(self, screen):
        self.screen = screen
        self.background = self.setup_map()
    
    def setup_map(self):
        background = []
        for i in range(30):
            x = random.randint(0, 179)
            y = random.randint(0, 119)
            rect = Rect(5*x, 5*y, 5, 5)
            background.append(rect)
        return background
    
    def display(self):
        self.screen.fill((0, 0, 0))  
        for star in self.background:
            pygame.draw.rect(self.screen, (255, 255, 255), star)


class MyPlane():
    def __init__(self, screen, x = 85, y = 105, resoucePath = "mplane_0.json"):
        self.screen = screen
        self.x = x
        self.y = y
        self.planeInfo = self.setup_planeInfo(resoucePath)
        self.plane = self.setup_plane()
        
    def setup_planeInfo(self, resoucePath):
        planeInfo = []
        with open(resoucePath) as data_file:
            datalist = json.load(data_file)
        for data in datalist:
            x = data["PosX"]
            y = data["PosY"]
            color = data["color"]
            planeInfo.append((x, y, color))
        return planeInfo
        
    def setup_plane(self):
        plane = []
        for data in self.planeInfo:
            rect = Rect(5 * (self.x + data[0]), 5 * (self.y + data[1]), 5, 5)
            plane.append(rect)
        return plane
    
    def display(self):
        i = 0
        color = Color()
        for rectOfplane in self.plane:
            
            pygame.draw.rect(self.screen, color.brush[self.planeInfo[i][2]], rectOfplane)
            i += 1
            
    def move_to_left(self):
        if self.x <= 0:
            return
        self.x -= 0.2
        for rectOfplane in self.plane:
            rectOfplane.move_ip(-1, 0)
    
    def move_to_right(self):
        if self.x >= 170:
            return
        self.x += 0.2 
        for rectOfplane in self.plane:
            rectOfplane.move_ip(1, 0)
    
    def shot(self): 
        bullet= Rect(5*self.x + 24, 5 * self.y, 5, 15)
        return bullet
          
        


screen = pygame.display.set_mode((900, 600), 0, 32)
pygame.display.set_caption("Galaxian")
bullet = Rect(0, 0, 0, 0)
enemyBullets = [Rect(i*100, random.randint(-600, 0), 5, 15) for i in range(10)]
print enemyBullets
def enemyBulletsFalling():
    count = 0
    for i in enemyBullets:
        i.move_ip(0, 1)
        #print i
        if i.top >= 600:
            enemyBullets[count] = Rect(random.randint(0, 900), random.randint(-600, 0), 5, 15)
        count += 1
        pygame.draw.rect(screen, (0, 255, 0), i)

def get_shot_state():
    global bullet
    if bullet.top <= 0:
        del bullet
        return True
    return False
        
def is_game_over(mplane, isOver):
    global enemyBullets
    if isOver is True:
        return True
    for i in enemyBullets:
        if i.top == mplane.y*5 and i.left >= mplane.x * 5 and i.left <= mplane.x*5 + 50:
            return True
    return False    
    
def display_shot():
    global bullet
    if bullet.top <= 0:
        return 
    bullet.move_ip(0, -1)
    pygame.draw.rect(screen, (255, 0, 0), bullet)
    #print bullet

def play_game():
    global bullet
    _map = Map(screen)
    l = MyPlane(screen)
    
    pygame.font.init()
    myfont = pygame.font.SysFont("Comic Sans MS", 150)
    textsurface = myfont.render('Game Over~', False, (255, 0, 255))
    Direction = {"left" : 0, "right" : 1, "none" : -1}
    planeMoveDirection = Direction["none"]
    isPlaneMove = False
    isShot = False
    isGameOver = False
    font_y = 600
    while True:
        _map.display()
        if isGameOver is False:
            l.display()
            display_shot()
        else:   
            font_y -= 1
            if font_y <= 200:
                font_y = 200
            screen.blit(textsurface,(150, font_y))
        
        enemyBulletsFalling()
        isGameOver = is_game_over(l, isGameOver)
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                
                if event.key == K_LEFT:
                    isPlaneMove = True
                    planeMoveDirection = Direction["left"]
                elif event.key  == K_RIGHT:
                    isPlaneMove = True
                    planeMoveDirection = Direction["right"]
                elif event.key == K_SPACE:
                    isShot = get_shot_state()
                    
                    
            elif event.type == KEYUP:
                isPlaneMove = False
        
        if isPlaneMove is True:
            if planeMoveDirection == Direction["left"]:
                l.move_to_left()
            elif planeMoveDirection == Direction["right"]:
                l.move_to_right()
        if isShot is True:
            bullet = l.shot()
            isShot = False    
        pygame.display.flip()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
play_game()   
