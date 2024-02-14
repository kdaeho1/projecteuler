fib1, fib2 = 1, 1
index = 2
digits = 1
while(digits < 1000):
    tmp = fib1
    fib1 = fib1 + fib2
    fib2 = tmp
    index += 1
    digits = len(str(fib1))
    #print(fib1)

print(index)