def primes(n):
    sieve = [True] * int(n/2)
    for i in range(3,int(n**0.5+1),2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2] + [2*i+1 for i in range(1,int(n/2)) if sieve[i]]

def truncate(n):
    primeList = primes(n)
    ans = 0
    found = 0
    for prime in primeList:
        if prime < 10:
            digits = 1
        elif prime < 100:
            digits = 2
        elif prime < 1000:
            digits = 3
        elif prime < 10000:
            digits = 4
        elif prime < 100000:
            digits = 5
        elif prime < 1000000:
            digits = 6
            
        count = 0
        for digit in range(1,digits):
            if int(str(prime)[digit::]) in primeList and int(str(prime)[:digit:]) in primeList:
                count += 1
        
        if digits == 1:
            continue
        elif digits == count+1:
            ans += prime
            print(prime)
            found += 1
            
        if found == 11:
            break
        
    return ans

print(truncate(1000000))