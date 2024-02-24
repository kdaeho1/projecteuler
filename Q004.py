#palindrome

def is_palindrome(number):
    digits = [int(digit) for digit in str(number)]
    
    for i in range(int(len(digits)/2)):
        if digits[i] != digits[len(digits)-i-1]:
            return 0
        
    return number

def three_digit_product_palindrome():
    pal = 0
    for first_num in range(100, 1000):
        for second_num in range(first_num+1, 1000):
            if pal < is_palindrome(first_num*second_num):
                pal = first_num*second_num
    
    print(pal)


three_digit_product_palindrome()
