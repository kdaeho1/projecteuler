prod = 1
for i in range(1, 101):
    prod *= i
    
prod = str(prod)
sum = 0
for ch in prod:
    sum += int(ch)
    
print(sum)