def get_next_permutation(string):
    i=8
    while i >= 0:
        if string[i] < string[i+1]:
            target = sorted(string[i:])
            new_num = target.pop(target.index(string[i])+1)
            last_nums = ''
            last_nums = last_nums.join(target)
            return string[:i] + new_num + last_nums
        i-=1
    return number
     
string='0123456789'
for i in range(1,1000000):    
    string = get_next_permutation(string)
print(string)