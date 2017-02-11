import numpy
import random
import time
import unicornhat

#initialize unicorn hat
unicornhat.rotation(0)
unicornhat.brightness(0.5)

# initialize numpy ndarrays
matrix = numpy.zeros((8, 8), dtype=int)
matrix2 = numpy.zeros((8, 8), dtype=int)

# set intial random state of the array
for x in range(20):
    row = random.randrange(0, 8, 1)
    col = random.randrange(0, 8, 1)
    matrix[row][col] = 1


#function that implements the rules of Conway's Game of Life
# < 2 surrounding blocks kills a living cell
# 2 or 3 surrounding blocks keeps a cell alive
# 3 surrounding blocks will cause a dead cell to become alive
# >= 4 surrounding blocks will kill a cell
def step(i,j, mat, mat2):
    sumbox = 0
    if i < 7 & j < 7:
        sumbox = mat[i - 1][j] + mat[i + 1][j] + mat[i][j - 1] + mat[i][j + 1] + mat[i - 1][j - 1] + mat[i - 1][j + 1] + \
                 mat[i + 1][j - 1] + mat[i + 1][j + 1]
    elif i < 7 & j == 7:
        sumbox = mat[i - 1][j] + mat[i + 1][j] + mat[i][j - 1] + mat[i][0] + mat[i - 1][j - 1] + mat[i - 1][0] + \
                 mat[i + 1][j - 1] + mat[i + 1][0]
    elif i == 7 & j < 7:
        sumbox = mat[i - 1][j] + mat[0][j] + mat[i][j - 1] + mat[i][j + 1] + mat[i - 1][j - 1] + mat[i - 1][j + 1] + \
                 mat[0][j - 1] + mat[0][j + 1]
    elif i == 7 & j == 7:
        sumbox = mat[i - 1][j] + mat[0][j] + mat[i][j - 1] + mat[i][0] + mat[i - 1][j - 1] + mat[i - 1][0] + mat[0][
            j - 1] + mat[0][0]
    #print("the sum of the surrounding cells is ", sumbox)
    if mat[i][j] == 1:
        if sumbox < 2:
            mat2[i][j] = 0
        #print("The cell died")
        elif sumbox == 2:
            mat2[i][j] = 1
        #print("The cell lived or became 1")
        elif sumbox == 3:
            mat2[i][j] = 1
        #print("The cell lived or became 1")
        elif sumbox >= 4:
            mat2[i][j] = 0
        #print("The cell died")
    elif mat[i][j] == 0:
        if sumbox == 3:
            mat2[i][j] = 1
        else:
            mat2[i][j] = 0
    return mat2


#adjust the number in range to test different numbers of generations
for generations in range(100):
    unicornhat.clear()
    for x in range(0,8):
        for y in range(0,8):
            output = step(x, y, matrix, matrix2)
    for i in range(0,8):
        for j in range(0,8):
            if output[i][j]==1:
                unicornhat.set_pixel(i, j, 255, 124, 124)
    unicornhat.show()
    time.sleep(1)
    matrix = output
unicornhat.clear()



