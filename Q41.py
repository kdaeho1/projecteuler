def pan_generate(n):
    #n = 9
    pan_list = [i for i in range(1,n+1)]
    current_list = pan_list
    #return pan_list                #1 2 3 4 5 6 7 8 9  
    for i in range(2, n):           # 2 3 4 5 6 7 8 9
        for j in range(n-1):        # 0 1 2 3 4 5 6 7 8
        current_list = pan_list[:n-i] + pan_list[:]
print(pan_generate(9))