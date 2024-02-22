def abcbalancer(p):
    count = 0
    for b in range(int(p/3), int(p/2)):
        for c in range(b+1, int(p/2)+1):
            a = p-b-c
            if a**2 + b**2 == c**2:
                print(a, b, c)
                count += 1
    return count

def solution(p):
    max = 0
    for i in range(int(p/2), p+1):
        abc = abcbalancer(i)
        print("p: " + str(i) + "\ncount: " + str(abc))
        if abc > max:
            max = abc
            ans = i
    return ans
    

print(solution(1000))
