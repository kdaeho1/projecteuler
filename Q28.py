#1
#3 5 7 9
#13 17 21 25
#31 37 43 49

#spiral 1001x1001
#500 iterations excluding the initial 1

print("start")

sum = 1 #start with 1

counter = 2
currentNumber = 1

for i in range(500):
    for j in range(4):
        currentNumber = currentNumber + counter
        sum += currentNumber
    counter += 2

print(sum)
