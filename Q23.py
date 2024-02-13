UPPER_BOUND = 28123

def notprimes(n):
    sieve = [True] * int(n/2)
    for i in range(3,int(n**0.5+1),2):
        if sieve[int(i/2)]:
            sieve[int(i*i/2)::i] = [False] * int((n-i*i-1)/(2*i)+1)
    return [2*i for i in range(3, int(n/2))] + [2*i+1 for i in range(1,int(n/2)) if not sieve[i]]


def find_abundant(num):
    sum = 0
    for i in range(1, int(num/3 + 1)):
        if num % i == 0:
            sum += i
    
    if num%2 == 0:
        sum += num/2
    
    if sum > num:
        return sum
    else:
        return 0

#print("start")
not_prime_list = notprimes(UPPER_BOUND)
#print(not_prime_list)
abundant_set = set([])
abundant_sum_list = []
for i in not_prime_list:
    if i not in abundant_set and find_abundant(i) != 0:
        abundant_set.update([i*j for j in range(1, int(UPPER_BOUND/i))])
        print(i)

list_length = len(abundant_list)

for i in range(list_length):
    for j in range(i+1, list_length):
        abundant_sum_list.append(abundant_list[i]+abundant_list[j])

ans = 0

for i in range(UPPER_BOUND+1):
    ans += i 


for num in abundant_sum_list:
    ans -= num
        
print(ans)