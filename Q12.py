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
    count = 0
    for i in range(1, len(factors)):
        candidates = combinations(factors, i)
        candidates = list(candidates)
        divisors = [tuple(div) for div in candidates]
        divisors = set(divisors)
        #print(divisors)
        for divisor in divisors:
            count += 1
    return count + 2
    
def triangle_generator(index):
    return sum(i for i in range(index))

x = 0
count = 0
while True:
    if x == num_divisors(triangle_generator(x)):
        break
    else:
        count += 1
        print(count)
    x += 1
print(x)
#print(triangle_generator(11))

#print(num_divisors(100))