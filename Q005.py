import math

def prime(num):
    for i in range(2, int(math.sqrt(num)+1)):   #exclude 1 and num
        if num/i == int(num/i):
            return False
    return True
    

def sm(num):
    candidate = 2520
    for i in range(11,num+1):
        if prime(i) and candidate/i != int(candidate/i):
                candidate = candidate * i
        elif candidate/i != int(candidate/i):
            for j in range(2,11):
                if candidate*j/i == int(candidate*j/i):
                    candidate = candidate * j
                    break
        print(candidate)
        
print(sm(20))
                
            
