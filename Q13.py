f = open("sum.txt", "r")
ans = 0
for line in f:
    ans += int(line)
ans = str(ans)[0:10]
print(ans)
    
    