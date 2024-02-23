def is_hex(n):
    if ((8*n+1)**0.5 + 1) % 4 == 0:
        return True
    return False
        
def is_pent(n):
    if ((24*n+1)**0.5 + 1) % 6 == 0:
        return True
    return False

i = 286
while i > 0:
    tri = int(i*(i+1)/2)
    if is_pent(tri) and is_hex(tri):
        print(tri)
        break
    i+=1