import numpy
import random
import time
import unicornhat

def sumbox(i,j, mat):
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
    return sumbox

def pop_update(mat_orig,mat_up):
    for i in range(8):
        for j in range (8):
            if mat_orig[i][j] == 0:
                sum = sumbox(i,j, mat_orig)
                if sum == 3:
                    mat_up[i][j] = 1
                else:
                    mat_up[i][j] = 0
            elif mat_orig[i][j] == 1:
                sum = sumbox(i,j, mat_orig)
                if sum <= 1 or sum >= 4:
                    mat_up[i][j] = 0
                else:
                    mat_up[i][j] = 1
    return mat_up

def lightup(output):
    for i in range(0,8):
        for j in range(0,8):
            if output[i][j]==1:
                unicornhat.set_pixel(i, j, 255, 124, 124)
    unicornhat.show()

def simulation(generations):
    #initialize unicorn hat
    unicornhat.brightness(0.4)

    matrix = numpy.random.randint(2, size=(8, 8))
    matrix_update = numpy.zeros((8, 8), dtype=int)
    lightup(matrix)    
    for generation in range(generations):
        time.sleep(1)
        unicornhat.clear()
        output = pop_update(matrix, matrix_update)
        lightup(output)
        matrix = output
        
simulation(50)
