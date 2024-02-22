import math
PROBLEM_BOUND = 1000000

def champernowne(n):
    champ_list = []
    integer = 0
    digit = 0
    while digit <= n+1:
        for i in str(integer):
            champ_list.append(int(i))
            
            digit += 1
        integer += 1
    print(champ_list[1])
    print(champ_list[10])
    print(champ_list[100])
    print(champ_list[1000])
    print(champ_list[10000])
    print(champ_list[100000])
    print(champ_list[1000000])
    return math.prod(champ_list[10**i] for i in range(7))
            
print(champernowne(PROBLEM_BOUND))