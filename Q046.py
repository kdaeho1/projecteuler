#9 = 7 + 2* 1**2
#

def primes(n):
    sieve = [True] * int(n/2) #all even numbers are not primes (except 2)
    for i in range(3,int(n**0.5+1),2): #3, 5, 7, ...
        if sieve[int(i/2)]: #case: i=3, sieve[1] (representing 3) is true, then 
            sieve[int((i*i-1)/2)::i] = [False] * int((n-i*i-1)/(2*i)+1) #sieve[4], sieve[7], ... are representing odd multiples of 3 (9, 15, 21, ...)
    prime_list = [2] + [2*i+1 for i in range(1,int(n/2)) if sieve[i]] #return sieved true (primes)
    composite_list = [2*i+1 for i in range(1,int(n/2)) if not sieve[i]]
    
    return prime_list, composite_list


prime_list, composite_list = primes(1000000)

goldbach = False

for composite in composite_list:
    found = False
    #print(composite)
    for prime in prime_list:
        if prime > composite:
            print(composite)
            goldbach = True
            break
        for square in range(1, int(composite**0.5)):
            if composite == prime + 2*square**2:
                found = True
                break
            elif composite < prime + 2*square**2:
                break
            
        if found:
            break
    if goldbach == True:
        break
    
