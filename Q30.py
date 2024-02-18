UPPER_LIMIT = (9**5)*5

sum = 0

for i in range(2, UPPER_LIMIT):
    stri = str(i)
    pwers = 0
    for ch in stri:
        pwers += int(ch)**5
    if pwers == i:
       sum += pwers
       
print(sum)