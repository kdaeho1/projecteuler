def comb(num):
    ans = 1 
    for i in range(num*2, num, -1):
        ans *= i
        print(i)
    for i in range(1, num+1):
        ans /= i
    return ans
    
print(int(comb(20)))