from itertools import permutations as pm
LIM=10000
def sieve():
    sieve = [True]*LIM
    for i in range(2, LIM):
        if sieve[i]:
            sieve[i*2::i] = [False] * int((LIM-1)/i - 1)
    return [i for i in range(2, 10000) if sieve[i] and i>1000]
    
sieve = sieve()

for i in sieve:
    perms = set(pm(ch for ch in str(i)))
    pmSet = set()
    for perm in perms:
        if int("".join(perm)) in sieve:
            pmSet.add(int("".join(perm)))
    for p in pmSet:
        for q in pmSet:
            if p!=q:
                if p-i == q-i or i-p == q-i:
                    ans = i, p, q

[i, p, q] = sorted(ans)
print(str(i)+str(p)+str(q))
