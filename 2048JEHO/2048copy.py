import pygame, sys
from pygame.locals import *

pygame.init()

GRAY = (224, 224, 224)
DARKGRAY = (128, 128, 128)
screen = pygame.display.set_mode((520, 520))
array = [[0 for i in range(4)] for j in range(4)]

def DrawMap():
    screen.fill(GRAY)
    
    for i in range(0, 5):
        pygame.draw.line(screen, DARKGRAY, (i * 129, 0), (i * 129, 520), 8)
        pygame.draw.line(screen, DARKGRAY, (0, i * 129), (520, i * 129), 8)

#def DrawNumber(n):
    

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    DrawMap()  
    pygame.display.update()
