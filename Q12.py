from itertools import combinations
import math

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
    
def num_divisors(num):
    factors = factorization(num)
    candidates = []
    divisors = []
    count = 2
    for i in range(1, len(factors)):
        candidates = combinations(factors, i)
        #candidates = list(candidates)
        divisors = [tuple(div) for div in candidates]
        divisors = set(divisors)
        #print(divisors)
        for divisor in divisors:
            count += 1
    return count
    
"""def triangle_generator(index):
    return sum(i for i in range(index))
"""

x = 500
count = 2
triangle = 1
while True:
    triangle += count
    print(triangle)
    #triangle = triangle_generator(count)
    if triangle < 50000000:
        count += 1
    elif x < num_divisors(triangle):
        print(triangle)
        break
    else:
        count += 1

