MAX_FIB = 4000000
#values do not exceed four million

def fibonacci_even(max):
    next_fibonacci = 0
    f1, f2 = 1, 2
    fibonacci_sequence = [f2]
    while next_fibonacci < max:
        next_fibonacci = f1+f2
        if next_fibonacci/2 == int(next_fibonacci/2):
            fibonacci_sequence.append(next_fibonacci)
        f1 = f2
        f2 = next_fibonacci
    
    return fibonacci_sequence
    
print(sum(fibonacci(MAX_FIB)))


    
    
