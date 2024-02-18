ans = []

for i in range(11, 100):
    if i % 10 != 0:
        for j in range(i, 100):
            if j % 10 != 0 and i != j:
                idig1 = int(i / 10)
                idig2 = i % 10
                jdig1 = int(j / 10)
                jdig2 = j % 10
                if idig1 == jdig2 and i/j == idig2/jdig1:
                    #ans.append([i,j])
                    ans.append(i/j)
                elif idig2 == jdig1 and i/j == idig1/jdig2:
                    #ans.append([i,j])
                    ans.append(i/j)

print(1/(ans[0]*ans[1]*ans[2]*ans[3]))