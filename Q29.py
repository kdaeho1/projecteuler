distinct_powers_set = set()

for a in range(2, 101):
    for b in range(2, 101):
        distinct_powers_set.add(a**b)
        
print(len(distinct_powers_set))