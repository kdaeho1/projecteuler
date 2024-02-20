def primes(n):
    sieve = [True] * int(n/2)
    for i in range(3,int(n**0.5+1),2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1,int(n/2)) if sieve[i]]
    

def circular(prime):
    circledPrime = 0
    cnt = 1
    while circledPrime != prime:
        primestr = str(prime)
        circledPrime = int(primestr[cnt:]+primestr[:cnt])
        yield circledPrime
        cnt += 1


primeList = primes(1000000)
ans = 0
for prime in primeList:
    for cirPrime in circular(prime):
        if cirPrime not in primeList:
            break
        else:
            ans += 1
    
ans = circular(primeList)
print(ans)
