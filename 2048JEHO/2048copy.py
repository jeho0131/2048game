import pygame, sys, random
from pygame.locals import *

pygame.init()

GRAY = (224, 224, 224)
DARKGRAY = (128, 128, 128)
WHITE = (255,255,255)

screen = pygame.display.set_mode((520, 520))
array = [[0 for i in range(4)] for j in range(4)]
spawn = [2,2,2,2,4]

#numF = pygame.font.SysFont(None, 200)
numImage = []
image2 = pygame.image.load("2.png").convert()
image4 = pygame.image.load("4.png").convert()

def DrawMap():
    screen.fill(GRAY)
    
    for i in range(0, 5):
        pygame.draw.line(screen, DARKGRAY, (i * 129, 0), (i * 129, 520), 8)
        pygame.draw.line(screen, DARKGRAY, (0, i * 129), (520, i * 129), 8)

def DrawNumber(n,x,y):
    #rect = pygame.Rect(129 * x + 6, 129 * y + 6, 120, 120)
    #pygame.draw.rect(screen, WHITE, rect)
    screen.blit(n, (129 * x + 6, 129 * y + 6))

def SpawnNumber(n):
    x = random.randint(0, 3)
    y = random.randint(0, 3)

    if array[y][x] != 0:
        SpawnNumber(n)
    else:
        array[y][x] = n
        DrawNumber(n, x, y)

DrawMap()
Inum = "{}{}".format("image", 2)
print(Inum)
SpawnNumber(Inum.strip(' " '))
SpawnNumber(image2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
