def primes(n):
    sieve = [True] * int(n/2)
    for i in range(3,int(n**0.5+1),2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1,int(n/2)) if sieve[i]]

def truncate(n):
    primeList = primes(1000000)
    ans = 0
    count = 0
    while count < 11:
        for prime in primeList:
            digits = len(str(prime))
            count = 0
            for digit in range(1,digits):
                if int(str(prime)[digit::]) in primeList and int(str(prime)[:digit:]) in primeList:
                    count += 1
                    
            if digits == count+1:
                ans += prime
                print(prime)
        
    return ans

print(truncate(1000000))
        
        
        