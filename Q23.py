UPPER_BOUND = 28123

def divisors(n):
    i=2;total={1}
    for i in range(2, int(n**0.5)+1):
        if n%i==0:
            total.add(i)
            total.add(n/i)
        i+=1
    return sum(total)

abun=set()
numbers=set(range(UPPER_BOUND))
for i in range(1,UPPER_BOUND):
    if i<divisors(i):
        abun.add(i)
        for j in abun:
            if (i+j) in numbers:
                numbers.remove(i+j)
            
print(sum(numbers))