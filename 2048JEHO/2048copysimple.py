import keyboard, random

array = [[0 for i in range(4)] for j in range(4)]
spawn = [2,2,2,2,4]

def SpawnNumber(n):
    x = random.randint(0, 3)
    y = random.randint(0, 3)

    if array[y][x] != 0:
        SpawnNumber(n)
    else:
        array[y][x] = n

def DrawMap():
    for i in range(4):
        for j in range(4):
            print(array[i][j], end=" ")
        print("")

    print("\n")

def Start():
    SpawnNumber(2)
    SpawnNumber(2)

    DrawMap()

def Move(rc, s, e, d):
    x = 0
    y = 0
    
    if rc == 0:
        for i in range(4):
            y = i
            x = s
            for j in range(2):
                if array[y][x] != 0:
                    while(array[y][x + d] == 0 and x != e):
                        array[y][x + d] = array[y][x]
                        array[y][x] = 0
                        x = x + d
                x = s + (d * -1 * j)
                          
    elif rc == 1:
        for i in range(4):
            x = i
            y = s
            for j in range(1, 3):
                if array[y][x] != 0:
                    while(array[y + d][x] == 0 and y != e):
                        array[y + d][x] = array[y][x]
                        array[y][x] = 0
                        y = y + d
                y = s + (d * -1 * j)
    
Start()

while True:
    '''if keyboard.is_pressed(80):
        Move(0, 1, 0, -1)

    if event.key == pygame.K_RIGHT:
        Move(0, 2, 3, 1)'''

    if keyboard.is_pressed(72): #up
        Move(1, 1, 0, -1)
        DrawMap()

    if keyboard.is_pressed(80): #down
        Move(1, 2, 3, 1)
        DrawMap()
