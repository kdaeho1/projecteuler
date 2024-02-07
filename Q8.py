f = open("digits.txt", "r")

digits = []

for i in range(100):
    f.seek(i)
    

for line in f:
    for ch in line:
        digits.append(int(ch))
        
