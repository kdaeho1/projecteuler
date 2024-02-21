f = open("names.txt", "r")
data = f.read()
data = data.strip('\"')
data = data.split('\",\"')
names = []
for i, name in enumerate(data):
    names.append(name)
names.sort()
nameScoreSum = 0
for i, name in enumerate(names):
    nameScore = 0
    for ch in name:
        nameScore += ord(ch) - 64
        #print("score: " + str(nameScore))
    nameScore *= i+1
    nameScoreSum += nameScore
"""    if name == 'COLIN':
        print("name: " + name)
        print("Score: " + str(nameScore))"""
print(nameScoreSum)