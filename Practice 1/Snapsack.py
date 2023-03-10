
import io,os
import sys
 
#Define the limit of the recusion
sys.setrecursionlimit(4000000)

itemsSize = []
itemsValues = []


def matrixDP(capacity, numberItems):
    DP = []
    for i in range(0, numberItems+1):
        filas = []
        for j in range(0, capacity+1):
            filas.append(-1)
        DP.append(filas)
    return DP

def KnapsackDP (capacity: int, pos: int) -> int:
    if pos <= -1 or capacity <= 0:
        return 0

    if memory[pos][capacity] != -1:  #if i already calculate
        return memory[pos][capacity]
    
    if itemsSize[pos]  <= capacity:
        memory[pos][capacity] = max( itemsValues[pos]+ KnapsackDP(capacity-itemsSize[pos], pos-1) , KnapsackDP(capacity, pos-1) ) 
        
        return memory[pos][capacity]

    elif itemsSize[pos] > capacity:
        memory[pos][capacity] = KnapsackDP (capacity, pos-1)
        return memory[pos][capacity]


input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
capacity, numberItems = input().decode().split()
capacity = int(capacity)
numberItems = int(numberItems)
memory = matrixDP(capacity, numberItems)


for i in range (0, numberItems):
    s, val = input().decode().split()
    s = int(s)
    val = int(val)
    itemsSize.append(s)
    itemsValues.append(val)


print(KnapsackDP(capacity, numberItems-1))
