def pwr_sum(pwrsum, index, num):
    while(index <= num):
        pwrsum *= 2
        return pwr_sum(pwrsum, index+1, num)
    return pwrsum

def add_digits(num):
    num = str(num)
    ans = 0
    for i in num:
        ans += int(i)
    return ans


#pwrsum = pwr_sum(8, 1, 997)
#print(pwr_sum(8, 1, 997))
print(add_digits(pwr_sum(8, 1, 997)))