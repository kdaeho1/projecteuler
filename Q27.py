def primes(n):
    out = list()
    sieve = [True] * (n+1)
    for p in range(2, n+1):
        if (sieve[p] and sieve[p]%2==1):
            out.append(p)
            for i in range(p, n+1, p):
                sieve[i] = False
    return out
    
def quad_prime(num):
    return
    
prime_list = primes(1000)
max = 0
ans = 0
for i in prime_list:
    for j in prime_list:
        cand = j-i-1
        n = 1
        while (n ** 2 + cand * n + i) in prime_list:
            n += 1
        if n > max:
            max = n
            ans = cand*i
print(ans)