def is_palindrome_ten(n):
    digits = []
    pal_digits = []
    while n >= 1:
        digits.insert(0, n%10)
        pal_digits.append(n%10)
        n = int(n/10)
    if digits == pal_digits:
        return digits

    return 0
    
def is_palindrome_two(n):
    digits = []
    pal_digits = []
    while n >= 1:
        digits.insert(0, n%2)
        pal_digits.append(n%2)
        n = int(n/2)
    if digits == pal_digits:
        return digits

    return 0
    
sum = 0
palindrome_list = []
for i in range(1, 1000000):
    if i==int(str(i)[::-1]):
        palindrome_list.append(i)
print(palindrome_list)
for i in palindrome_list:
    if is_palindrome_two(i):
        sum += i
        
print(sum)

""" way faster solution :(
sum = 0
for i in range(1, 1000000):
    bini = int(str(bin(i)).replace('0b',''))
    if i==int(str(i)[::-1]) and bini==int(str(bini)[::-1]):
        sum += i
        
print(sum)
"""
        