def primes(n):
    sieve = [True] * int(n/2) #all even numbers are not primes (except 2)
    for i in range(3,int(n**0.5+1),2): #3, 5, 7, ...
        if sieve[int(i/2)]: #case: i=3, sieve[1] (representing 3) is true, then 
            sieve[int((i*i-1)/2)::i] = [False] * int((n-i*i-1)/(2*i)+1) #sieve[4], sieve[7], ... are representing odd multiples of 3 (9, 15, 21, ...)
    return [2] + [2*i+1 for i in range(1,int(n/2)) if sieve[i]] #return sieved true (primes)

sieve = primes(1000000)
prLen = len(sieve)
sum = 0
isPrime = [False]*1000000
for prime in sieve:
    isPrime[prime] = True
maxS = 0
maxL = 0
for i in range(prLen):
    sum = 0
    for j in range(i, prLen):
        sum += sieve[j]
        if sum > 999990:
            break
        if isPrime[sum] and sum > maxS and j-i > maxL:
            maxL = j-i
            maxS = sum
print(maxS, maxL)