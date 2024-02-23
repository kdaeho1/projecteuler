import csv

def triangle_numbers():
    triangle_list = []
    for i in range(1,100):
        triangle_list.append(int(i*(i+1)/2))
    return triangle_list

def triangle_word(word):
    value = 0
    for ch in word:
        value += ord(ch) - 64
    
    return value
        
triangle_list = triangle_numbers()
ans = 0

with open('words.txt', newline='') as f:
    reader = csv.reader(f, delimiter=',')
    for lst in reader:
        for word in lst:
            word.strip("\"")
            value = triangle_word(word)
            if value in triangle_list:
                ans += 1
        
print(ans)