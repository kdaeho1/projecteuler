def number_letter_count_ones(num): #one two three four five six seven eight nine ten
    if num == 1 or num == 2 or num == 6 or num == 10: #one two six ten
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

def number_letter_count_tens(num): #ten twenty thirty fourty fifty sixty seventy eighty ninety
    if num == 50 or num == 60:
        return 5
    elif num == 20 or num == 30 or num == 40 or num == 80 or num == 90:
        return 6
    elif num == 10:
        return 3
    else:
        return 7

def number_letter_count(num):
    ones = num%10
    tens = num%100
    tens -= tens%10
    hundreds = num%1000
    hundreds -= hundreds%100
    #print(ones, tens, hundreds)
    if num < 10:
        return number_letter_count_ones(num)
    elif num < 20:
        return number_letter_count_teens(num)
    elif num < 100:
        return number_letter_count_tens(num)
    
    if num == 1000: #case: 1000
        # one thousand = 11 letters
        return 11
    elif 100 < num: #case: 100 to 999
        if num % 100 == 0: #case: one hundred, two hundred, etc
            return 0
    return 0
    
number_letter_count(525)
            
            
        