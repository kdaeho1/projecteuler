import math

MAX_DIGIT_RANGE = 1000
ADJACENT_DIGIT_SIZE = 13
f = open("digits.txt", "r")
newstr = ""
for line in f:
    line = line.rstrip("\n")
    newstr += line
f.close()
#print(newstr)
candidate = 0
for pointer in range(MAX_DIGIT_RANGE - ADJACENT_DIGIT_SIZE):
    digits = []
    for i in range(ADJACENT_DIGIT_SIZE):
        if int(newstr[pointer+i]) == 0:
            break
        digits.append(int(newstr[pointer+i]))
    if candidate < math.prod(digits):
        candidate = math.prod(digits)

print(candidate)
    
    
    
for line in f:
    for ch in line:
        digits.append(int(ch))
        
