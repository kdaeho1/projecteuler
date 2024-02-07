sqofsum = sum(x for x in range(1,101))
sqofsum = sqofsum * sqofsum
#print(sqofsum)
sumofsq = sum(x*x for x in range(1,101))
#print(sumofsq)
print(sqofsum-sumofsq)