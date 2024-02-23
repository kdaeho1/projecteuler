def get_next_permutation(string):
    n = 10
    for i in range(n-2, -1, -1):
        if string[i] < string[i+1]:
            target = sorted(string[i:])
            new_num = target.pop(target.index(string[i])+1)
            last_nums = ''
            last_nums = last_nums.join(target)
            return string[:i] + new_num + last_nums
     
astring='0123456789'
ans = 0
for i in range(1,1000000000):
    string = get_next_permutation(astring)

    try:
        if string == '9876543210':
            break
        if int(string[7:10]) % 17 == 0:
            if int(string[6:9]) % 13 == 0:
                if int(string[5:8]) % 11 == 0:
                    if int(string[4:7]) % 7 == 0:
                        if int(string[3:6]) % 5 == 0:
                            if int(string[2:5]) % 3 == 0:
                                if int(string[1:4]) % 2 == 0:
                                    #print(string)
                                    ans += int(string)
                                    
    except TypeError:
        print(astring)
    astring = string
print(ans)
