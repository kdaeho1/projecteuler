import math

def prime(num):
    for i in range(2, int(math.sqrt(num)+1)):   #exclude 1 and num
        if num/i == int(num/i):
            return False
    return True
    
def primeListFinder(index):
    candidate = 2
    primeList = []
    for i in range(index):
        found = False
        while not found:
            if prime(candidate):
                primeList.append(candidate)
                #print(candidate)
                candidate += 1
                found = True
            else:
                candidate += 1
    
    return primeList

ans = primeListFinder(10001)[-1]
print(ans)
#print(primeListFinder(10001))