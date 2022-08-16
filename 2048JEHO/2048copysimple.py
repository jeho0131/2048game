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

def CheckFill(rc, n):
    if rc == 0:
        for i in range(4):
            if array[n][i] == 0:
                return True
        return False

    if rc == 1:
        for i in range(4):
            if array[i][n] == 0:
                return True
        return False

def Move(rc, s, d):
    x = 0
    y = 0
    count = 4
    
    if rc == 0:
        for i in range(4):
            y = i
            x = s
            if CheckFill(0, i):
                for j in range(3):
                    if array[y][x] == 0:
                        for m in range(1, count):
                            if array[y][x + d*m] != 0:
                                array[y][x] = array[y][x + d*m]
                                array[y][x + d*m] = 0
                                break
                    x = x + d
                    count -= 1
            count = 4
                          
    elif rc == 1:
        for i in range(4):
            x = i
            y = s
            if CheckFill(1, i):
                for j in range(3):
                    if array[y][x] == 0:
                        for m in range(1, count):
                            if array[y + d*m][x] != 0:
                                array[y][x] = array[y + d*m][x]
                                array[y + d*m][x] = 0
                                break
                    y = y + d
                    count -= 1
            count = 4
                    
Start()

while True:
    if keyboard.is_pressed(75): #left
        Move(0, 0, 1)
        SpawnNumber(random.choice(spawn))
        DrawMap()

    if keyboard.is_pressed(77): #right
        Move(0, 3, -1)
        SpawnNumber(random.choice(spawn))
        DrawMap()
    
    if keyboard.is_pressed(72): #up
        Move(1, 0, 1)
        SpawnNumber(random.choice(spawn))
        DrawMap()

    if keyboard.is_pressed(80): #down
        Move(1, 3, -1)
        SpawnNumber(random.choice(spawn))
        DrawMap()
