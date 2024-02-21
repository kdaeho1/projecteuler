#make 10000 array of 0's, ignore index 0
#iterate from 1st index to find amicable pairs
#update amicable pairs and change array 0->1
#if array[i] == 1, skip
#add entire array

MAX_NUM = 10000

def divisor_sum(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    return sum
    
amicable_numbers = [0]*MAX_NUM
count = 0
for i in range(2, MAX_NUM):
    if amicable_numbers[i] == 0:
        amicable_candidate = divisor_sum(i)
        if amicable_candidate == 1 or amicable_candidate <= i:
            continue
        elif i == divisor_sum(amicable_candidate):
            amicable_numbers[i] = 1
            amicable_numbers[amicable_candidate] = 1
            count += i + amicable_candidate
            #print(count)

print(count)
        
    