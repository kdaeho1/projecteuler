def three_or_five(num):
    sum = 0
    for i in range (num):
        if int(i/3) == i/3 or int(i/5) == i/5:
            sum += i
    return sum

print(three_or_five(1000))
