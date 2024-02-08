import math
ADJ_LEN = 4
GRD_LEN = 20

f = open("grid.txt","r")
grid = [[]*GRD_LEN]*GRD_LEN
counter = 0
product = 0

for line in f:
    grid[counter] = line.split()
    grid[counter] = grid[counter]
    counter += 1
    
grid = [[int(i) for i in line] for line in grid]
#print(grid)

for i in range(GRD_LEN):
    for j in range(GRD_LEN - ADJ_LEN+1):
        tmp = 1
        for k in range(ADJ_LEN):
            tmp *= grid[i][j+k]
        if product < tmp:
            product = tmp
            
for i in range(GRD_LEN - ADJ_LEN + 1):
    for j in range(GRD_LEN):
        tmp = 1
        for k in range(ADJ_LEN):
            tmp *= grid[i+k][j]
        if product < tmp:
            product = tmp

for i in range(GRD_LEN - ADJ_LEN+1):
    for j in range(GRD_LEN - ADJ_LEN+1):
        tmp = 1
        for k in range(ADJ_LEN):
            tmp *= grid[i+k][j+k]
        if product < tmp:
            product = tmp
                
for i in range(ADJ_LEN, GRD_LEN):
    for j in range(GRD_LEN - ADJ_LEN+1):
        tmp = 1
        for k in range(ADJ_LEN):
            tmp *= grid[i-k][j+k]
        if product < tmp:
            product = tmp

print(product)
                
