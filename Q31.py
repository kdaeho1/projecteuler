

coins = [1, 2, 5, 10, 20, 50, 100, 200]
table = [1] + [0]*201

for coin in coins:
    for i in range(1, 201):
        if coin <= i: 
            table[i] += table[i-coin]

print(table[200])