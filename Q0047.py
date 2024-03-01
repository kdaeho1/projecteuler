def solve():

    target = 4
    limit = 150000
    n_prime_divisors = [0] * limit
    count = 0 
    for num in range(2, limit):
        if n_prime_divisors[num] == 0:
            for mul in range(2 * num, limit, num):
                n_prime_divisors[mul] += 1
            count = 0
        elif n_prime_divisors[num] == target:
            count += 1
        else:
            count = 0

        if count == target:
            return num - target + 1
    
print(solve())