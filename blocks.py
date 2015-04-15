import pygame
from pygame.locals import *
from sys import exit
import time

pygame.init()
screen = pygame.display.set_mode((900, 600), 0, 32)
screen.fill((255,255,255))
pygame.display.set_caption("Blocks")

bar = Rect((0,570),(100,30))

position = [21, 21]
dx = 20
dy = 20
block = Rect((position[0], position[1]),(20,20))

targets = []
for i in range(10):
	pass
def block_move():
	global dx, dy, position
	block.move_ip(dx, dy)
	position[0] += dx
	position[1] += dy
	if position[1] >= 550 or position[1] <= 20:
		print "yes"
		dy = -dy
	if position[0] >= 880 or position[0] <= 20:
		dx = -dx
	
	
		
while True:
	time.sleep(0.2)
	block_move()
	
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
		if event.type == KEYDOWN:
			if event.key == K_LEFT:
				bar.move_ip(-30,0)
			if event.key == K_RIGHT:
				bar.move_ip(30,0)
			
		
	pygame.draw.rect(screen, (0,0,0), bar)
	pygame.draw.rect(screen, (0,0,0), block)
	pygame.display.flip()
	screen.fill((255,255,255))
