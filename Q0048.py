def selfpower():
    sum = 0
    mod = 10**10
    for i in range(1, 1000):
        sum += i**i%mod
        
    return sum%mod
    
print(selfpower())