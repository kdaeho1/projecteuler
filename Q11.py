import math
ADJ_LEN = 4
GRD_LEN = 20

f = open("grid.txt","r")
grid = [[0]*GRD_LEN]*GRD_LEN
numgrid = [[0]*GRD_LEN]*GRD_LEN
counter = 0
product = 0

for line in f:
    grid[counter] = line.split()
    counter += 1
#print(grid)

for i in range(GRD_LEN):
    for j in range(GRD_LEN):
        numgrid[i][j] = int(grid[i][j])
#print(numgrid)

for i in range(GRD_LEN):
    for j in range(GRD_LEN - ADJ_LEN+1):
        if product < math.prod(numgrid[i][j:j+ADJ_LEN]):
            product = math.prod(numgrid[i][j:j+ADJ_LEN])

for i in range(GRD_LEN - ADJ_LEN + 1):
    for j in range(GRD_LEN):
        tmp = 1
        for k in range(ADJ_LEN):
            tmp *= numgrid[i+k][j]
        if product < tmp:
            product = tmp

for i in range(GRD_LEN - ADJ_LEN+1):
    for j in range(GRD_LEN - ADJ_LEN+1):
        tmp = 1
        for k in range(ADJ_LEN):
            tmp *= numgrid[i+k][j+k]
        if product < tmp:
            product = tmp
                
for i in range(ADJ_LEN, GRD_LEN):
    for j in range(GRD_LEN - ADJ_LEN+1):
        tmp = 1
        for k in range(ADJ_LEN):
            tmp *= numgrid[i-k][j+k]
        if product < tmp:
            product = tmp
                
print(product)
                
