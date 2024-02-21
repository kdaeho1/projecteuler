# input 1: 1, 2, 3, ... n, n>1 and n<5
# input 2: integer
# output: max 9 digit number

#for n(1, 2) and 5000 up to 9999: 999919998
#for n(1, 2, 3) and 100 up to 333: 333666999
#for n(1, 2, 3, 4) and 25 up to 33: 336699132
#for n(1, 2, 3, 4, 5) and 9: 918273645 (highest value for n(1, 2, 3, 4, 5))
#for n(1,2,3,4,5,6) and 3: 369121518 - not pandigital
#for n(1,2,3,4,5,6,7) and above : does not have any possible 9 digit values
max = 0
pandigital = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
for i in range(5000, 10000):
    candidate_set = set()
    candidate = i*100002
    for ch in str(candidate):
        candidate_set.add(int(ch))
    if pandigital == candidate_set and max < candidate:
        max = candidate
for i in range(100, 334):
    candidate_set = set()
    candidate = i*1002003
    for ch in str(candidate):
        candidate_set.add(int(ch))
    if pandigital == candidate_set and max < candidate:
        max = candidate

for i in range(25, 34):
    candidate_set = set()
    candidate = i*10203004
    for ch in str(candidate):
        candidate_set.add(int(ch))
    if pandigital == candidate_set and max < candidate:
        max = candidate

for i in range(25, 34):
    candidate_set = set()
    candidate = i*10203004
    for ch in str(candidate):
        candidate_set.add(int(ch))
    if pandigital == candidate_set and max < candidate:
        max = candidate

if max < 918273645:
    max = 918273645

print(max)