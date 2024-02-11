def number_letter_count_ones(num): #one two three four five six seven eight nine ten
    if num == 0:
        return 0
    elif num == 1 or num == 2 or num == 6: #one two six ten
        return 3
    elif num == 4 or num == 5 or num == 9: #four five nine
        return 4
    else: #three seven eight
        return 5

def number_letter_count_teens(num): #eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen
    if num == 11 or num == 12:
        return 6
    elif num == 15 or num == 16:
        return 7
    elif num == 13 or num == 14 or num == 18 or num == 19:
        return 8
    else:
        return 9

def number_letter_count_tens(num): #ten twenty thirty forty fifty sixty seventy eighty ninety
    if num == 0:
        return 0
    elif num == 40 or num == 50 or num == 60:
        return 5
    elif num == 20 or num == 30 or num == 80 or num == 90:
        return 6
    elif num == 10:
        return 3
    else:
        return 7
        
def number_letter_count_hundreds(num):
    #print(number_letter_count_ones(num/100)+7)
    return number_letter_count_ones(num/100) + 7

def number_letter_count(num):
    ones = num%10
    tens = num%100
    tens -= tens%10
    hundreds = num%1000
    hundreds -= hundreds%100
    #print(ones, tens, hundreds)
    
    if num == 1000:
        return 11
    
    if num < 10:
        return number_letter_count_ones(num)
    elif num < 20 and num > 10:
        return number_letter_count_teens(num)
    elif num < 100:
        return number_letter_count_tens(tens) + number_letter_count_ones(ones)
    elif 100 <= num: #case: 100 to 999
        if num % 100 == 0: #case: x hundred
            return number_letter_count_hundreds(hundreds)
        elif tens == 10 and ones != 0: #case: x hundred + and + teen number
            return number_letter_count_hundreds(hundreds) + number_letter_count_teens(num%100) + 3
        else: #case: x hundred + and + number
            return number_letter_count_hundreds(hundreds) + number_letter_count_tens(tens) + number_letter_count_ones(ones) + 3
    return 0
    
ans = 0

print(number_letter_count(342))

for i in range(1, 1001):
    #print(i)
    ans += number_letter_count(i)
print(ans)
            
            
        