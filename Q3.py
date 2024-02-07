def factorization(num):
    factors = []
    i = 2
    while num != 1:
        if num/i == int(num/i):
            factors.append(i)
            num = num/i
            i -= 1
        i += 1
    return factors
    

ans = factorization(600851475143)
#ans = factorization(134)
print(ans)