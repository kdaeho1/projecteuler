# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
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
        cnt += 1
        yield circledPrime


primeList = primes(1000000)
cirPrimeList = [False]*1000000
ans = 0
for prime in primeList:
    if prime == 11:
        ans += 1
        
    if not cirPrimeList[prime]:
        target = len(str(prime))
        count = 0
        for cirPrime in circular(prime):
            if cirPrime in primeList and not cirPrimeList[cirPrime]:
                count += 1
                cirPrimeList[cirPrime] = True
            else:
                break
        if count == target:
            ans += count

print(ans)