"""10 4
2 5 3 6"""

def matrixDP():
    memory = []
    for i in range(0, 1000):
        filas = []
        for i in range(0, 1000):
            filas.append(-1)
        memory.append(filas)
    return memory

def coinChange(index, value):
    if value == 0:
        return 1

    if value < 0:
        return 0

    if index == numberOfCoins:
        return 0

    if memory[index][value] != -1:
        return memory[index][value]
    
    memory[index][value] = coinChange(index, value-coins[index]) + coinChange(index+1, value)
    return memory[index][value]


memory = matrixDP()
coins = []

firstLine = input().split()
targetValue = int(firstLine[0])
numberOfCoins = int(firstLine[1])

secondLine = input().split()
for coin in secondLine:
    coins.append(int(coin))

print(coinChange(0,targetValue))