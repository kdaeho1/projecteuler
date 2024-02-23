import math

def prime(num):
    for i in range(2, int(math.sqrt(num)+1)):   #exclude 1 and num
        if num/i == int(num/i):
            return False
    return True

def get_next_permutation(string, n):
    for i in range(n-2, -1, -1):
        try:
            if string[i] > string[i+1]:
                target = sorted(string[i:], reverse = True)
                new_num = target.pop(target.index(string[i])+1)
                last_nums = ''
                last_nums = last_nums.join(target)
                return string[:i] + new_num + last_nums
        except IndexError:
            print(string)
    return None
string = "987654321"
cand = string
n = 9
while not prime(int(cand)):
    cand = get_next_permutation(cand, n)
    
    if not cand:
        string = string[1:]
        n -= 1
        cand = get_next_permutation(string, n)
print(cand)
