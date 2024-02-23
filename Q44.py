#find pentagonal numbers
#find differences and sums in pentagonal numbers
#find smallest

def is_pentagonal(n):
    """function to check if the number
    is pentagonal number or not"""
    if (1+(24*n+1)**0.5) % 6 == 0:
        return True
    return False

min = 100000000
pent = True
i = 1
while pent:
    for j in range(1, i):
        pk = int(i*(3*i-1)/2)
        pj = int(j*(3*j-1)/2)
        #print(pk-pj)
        if is_pentagonal(pk-pj) and is_pentagonal(pk+pj):
            print(pk-pj)
            print(i, j)
            pent = False
    i += 1