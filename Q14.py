MAX_START_NUM = 1000000
collatz_sequence_length = [0]*(MAX_START_NUM*3)
#print(collatz_sequence_length)

def find_collatz_sequence_length(start_num):
    count = 0
    while start_num != 1:
       # start_num = int(start_num)
        if start_num > MAX_START_NUM or collatz_sequence_length[int(start_num)] == 0:
            if start_num % 2 == 1:
                start_num = start_num*3+1
            else:
                start_num /= 2
        else:
            count += collatz_sequence_length[int(start_num)]
            return count
        count += 1
    return count
    
    
max, index = 0, 0
for i in range(2, MAX_START_NUM-1):
    collatz_sequence_length[i] = find_collatz_sequence_length(i)
    if collatz_sequence_length[i] > max:
        max = collatz_sequence_length[i]
        index = i
        #print(collatz_sequence_length)
    #print(i, ": ", max)

print(index, max)
    